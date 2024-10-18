# -*- coding: utf-8 -*-
import glob
import itertools
import os, shutil
import re
import textwrap
from pathlib import Path

import click as click

from tools.uml.copy_locs import extract_keys_to_replace, copy_locs_from_folder, replace_keys
from tools.uml.icon import generate_resource_icons, generate_job_icons
from tools.uml.modifier import generate_modifiers, generate_buildings_loc, generate_jobs_loc
from tools.uml.utils import load_config, Writer, BASE_PATH, create_sprites_for_cleanup, AUTH_SWAPS_INLINE_NAME, \
    AUTH_SWAPS_INLINE_NAME_TEMPLATE, SUPPORT_FOLDER, INLINE_FOLDER, SCRIPTED_TRIGGERS, SCRIPT_VALUES, SCRIPTED_EFFECTS, \
    SCRIPTED_VARIABLES, AUTH_SWAPS_INLINE_NAME_TEMPLATE_SUFFIX, SUFFIX_PLACEHOLDER, TRAIT_INLINE_NAME, \
    TRAIT_INLINE_NAME_TEMPLATE_SUFFIX, TRAIT_INLINE_NAME_TEMPLATE, HOARDER_BUTTONS_TEMPLATE


@click.group()
def cli():
    pass


@cli.command()
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--output',
              default=Path(BASE_PATH) / f'../../localisation/{{language}}/replace/zzzz_uml_modifier_l_{{language}}.yml')
@click.option('--base-mod-path', default=Path(BASE_PATH) / '../..')
@click.option('--missing-sprites-output', default=Path(BASE_PATH) / '../../interface/!!_missing_sprites_cleanup.gfx')
def generate_loc(config: str, local_config: str, output: str, base_mod_path: str, missing_sprites_output: str):
    base_mod_path = Path(base_mod_path).resolve()
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg

    resources = cfg['resources']
    index = 0
    for language, lang_cfg in cfg['languages'].items():
        path = Path(output.format(language=language)).resolve()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with Writer(str(path)) as writer:
            writer.write_language(language)

            with writer.with_spacer():
                generate_modifiers(writer, lang_cfg, resources)

            with writer.with_spacer():
                generate_buildings_loc(writer, lang_cfg)

            with writer.with_spacer():
                generate_jobs_loc(writer, lang_cfg)


        if index == 0:
            generate_job_icons(lang_cfg['jobs'], cfg['paths'], base_mod_path)
        index += 1

    generate_resource_icons(resources, cfg['paths'], base_mod_path)
    if 'missing_sprites' in cfg:
        missing_sprites_output = Path(missing_sprites_output).resolve()
        os.makedirs(os.path.dirname(missing_sprites_output), exist_ok=True)
        with Writer(str(missing_sprites_output), has_bom=False) as writer:
            create_sprites_for_cleanup(writer, cfg['missing_sprites'])


@cli.command()
@click.option('--placeholder-file')
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--replace-string', default='REPLACE_ME')
def copy_placeholder_loc(placeholder_file: str, config: str, local_config: str, replace_string: str):
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg

    for language, lang_cfg in cfg['languages'].items():
        keys_to_replace = extract_keys_to_replace(
            Path(placeholder_file.format(language=language)).resolve(),
            replace_string, language
        )
        keys_needed = set(keys_to_replace.keys())

        for mod_folder in cfg['mod_paths']:
            if len(keys_needed) == 0:
                break
            print(f"Analyzing mod folder: {mod_folder}")
            print(f"Searching for {len(keys_needed)} loc keys")
            lang_folder = mod_folder / 'localisation' / language
            copy_locs_from_folder(lang_folder, language, keys_needed, keys_to_replace)
            lang_folder = mod_folder / 'localisation' / language / 'replace'
            copy_locs_from_folder(lang_folder, language, keys_needed, keys_to_replace)
        replace_keys(
            Path(placeholder_file.format(language=language)).resolve(), keys_to_replace, replace_string
        )


@cli.command()
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--base-mod-path', default=Path(BASE_PATH) / '../..')
@click.option('--generate-placeholder-and-include', default=True)
@click.option('--prefix', default='evolved')
def create_compat_inlines(config: str, local_config: str, base_mod_path: str, generate_placeholder_and_include: bool, prefix: str):
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg
    base_mod_path = Path(base_mod_path).resolve()

    inlines = {}

    for filename in glob.iglob(str(base_mod_path / f"common/inline_scripts/**/**"), recursive=True):
        if ('tec_' in filename
                and '.txt' in filename
                and 'evolved_support' not in filename
                and 'mod_support/tec_inlines_include' not in filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    matches = re.match(f"\\s*include_script\\s*=\\s*\"?([a-z_A-Z\\d/]+\s)\"?", line)
                    if matches and matches.group(1) and 'iterators' not in matches.group(1):
                        inlines[matches.group(1).strip()] = (os.path.relpath(filename, base_mod_path).replace('\\', '/'), i + 1)

    scripted_triggers = {}

    for filename in glob.iglob(str(base_mod_path / f"common/scripted_triggers/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_triggers = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match("\\s*script\\s*=\\s*mod_support/tec_trigger_include", line)
                        should_look_for_trigger = matches
                    else:
                        should_look_for_trigger = False
                        matches = re.match(f"\\s*trigger\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                        if matches and matches.group(1):
                            found_triggers.append(matches.group(1))

                for i, line in enumerate(lines):
                    for s in found_triggers:
                        matches = re.match(f"\\s*{s}\\s*=\\s*{{", line)
                        if matches:
                            scripted_triggers[s] = (filename[len(str(base_mod_path)) + 1:].replace('\\', '/'), i + 1)

    script_values = {}

    for filename in glob.iglob(str(base_mod_path / f"common/script_values/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                should_look_for_parameters = False
                lines = f.readlines()
                found_values = []
                value_name = None
                for i, line in enumerate(lines):
                    if not (should_look_for_trigger or should_look_for_parameters):
                        matches = re.match("\\s*script\\s*=\\s*mod_support/tec_value_include", line)
                        should_look_for_trigger = matches
                    elif not should_look_for_parameters:
                        should_look_for_trigger = False
                        should_look_for_parameters = True
                        matches = re.match(f"\\s*value\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                        if matches and matches.group(1):
                            value_name = matches.group(1)
                    else:
                        should_look_for_trigger = False
                        should_look_for_parameters = False
                        matches = re.match(f"\\s*parameters\\s*=\\s*\"?([a-z_A-Z\\d|$@]*)\"?", line)
                        if matches and matches.group(1):
                            found_values.append([value_name, matches.group(1)])
                        else:
                            found_values.append([value_name, ''])


                for i, line in enumerate(lines):
                    for s, params in found_values:
                        matches = re.match(f"\\s*{s}\\s*=\\s*{{", line)
                        if matches:
                            script_values[s] = (filename[len(str(base_mod_path)) + 1:].replace('\\', '/'), i + 1, params)

    scripted_effects = {}

    for filename in glob.iglob(str(base_mod_path / f"common/scripted_effects/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_effects = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match("\\s*script\\s*=\\s*mod_support/tec_effect_include", line)
                        should_look_for_trigger = matches
                    else:
                        should_look_for_trigger = False
                        matches = re.match(f"\\s*effect\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                        if matches and matches.group(1):
                            found_effects.append(matches.group(1))

                for i, line in enumerate(lines):
                    for s in found_effects:
                        matches = re.match(f"\\s*{s}\\s*=\\s*{{", line)
                        if matches:
                            scripted_effects[s] = (filename[len(str(base_mod_path)) + 1:].replace('\\', '/'), i + 1)

    authorities_with_swaps = {}

    for filename in glob.iglob(str(base_mod_path / f"common/governments/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_authorities = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match(f"\\s*script\\s*=\\s*{AUTH_SWAPS_INLINE_NAME}", line)
                        should_look_for_trigger = matches
                    else:
                        should_look_for_trigger = False
                        matches = re.match(f"\\s*authority\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                        if matches and matches.group(1):
                            found_authorities.append(matches.group(1))

                for i, line in enumerate(lines):
                    for s in found_authorities:
                        matches = re.match(f"\\s*{s}\\s*=\\s*{{", line)
                        if matches:
                            authorities_with_swaps[s] = (filename[len(str(base_mod_path)) + 1:].replace('\\', '/'), i + 1)

    extendable_traits = {}

    for filename in glob.iglob(str(base_mod_path / f"common/traits/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_traits = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match(f"\\s*script\\s*=\\s*{TRAIT_INLINE_NAME}", line)
                        should_look_for_trigger = matches
                    else:
                        should_look_for_trigger = False
                        matches = re.match(f"\\s*trait\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                        if matches and matches.group(1):
                            found_traits.append(matches.group(1))

                for i, line in enumerate(lines):
                    for s in found_traits:
                        matches = re.match(f"\\s*{s}\\s*=\\s*{{", line)
                        if matches:
                            extendable_traits[s] = (filename[len(str(base_mod_path)) + 1:].replace('\\', '/'), i + 1)

    suffixes = cfg['addons']['suffixes']
    scripted_trigger_defaults = cfg['addons'].get('scripted_trigger_defaults', [])

    new_line = '\n'

    if (base_mod_path / INLINE_FOLDER / SUPPORT_FOLDER).exists():
        for root, dirs, files in os.walk(base_mod_path / INLINE_FOLDER / SUPPORT_FOLDER):
            for file in files:
                if os.stat(Path(root) / file).st_size == 0:
                    os.remove(Path(root) / file)
        # shutil.rmtree(base_mod_path / INLINE_FOLDER / SUPPORT_FOLDER)

    for inline, suffix in itertools.product(inlines.items(), suffixes):
        if '$' not in inline:
            os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/{SUPPORT_FOLDER}/{inline[0]}_{suffix}.txt"),
                        exist_ok=True)
            (base_mod_path / f"{INLINE_FOLDER}/{SUPPORT_FOLDER}/{inline[0]}_{suffix}.txt").touch()

    doc_inlines = dict(inlines)
    auth_inlines = {}
    trait_inlines = {}

    for authority, suffix in itertools.product(authorities_with_swaps.items(), suffixes):
        path = base_mod_path / INLINE_FOLDER / SUPPORT_FOLDER / AUTH_SWAPS_INLINE_NAME_TEMPLATE_SUFFIX.format(authority[0], suffix)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        path.touch()
        doc_inlines[AUTH_SWAPS_INLINE_NAME_TEMPLATE.format(authority[0])] = authority[1]
        auth_inlines[authority[0]] = (*authority[1], f"use inline {SUPPORT_FOLDER / (AUTH_SWAPS_INLINE_NAME_TEMPLATE_SUFFIX.format(authority[0], SUFFIX_PLACEHOLDER))}")


    for trait, suffix in itertools.product(extendable_traits.items(), suffixes):
        path = base_mod_path / INLINE_FOLDER / SUPPORT_FOLDER / TRAIT_INLINE_NAME_TEMPLATE_SUFFIX.format(trait[0], suffix)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        path.touch()
        doc_inlines[TRAIT_INLINE_NAME_TEMPLATE.format(trait[0])] = trait[1]
        trait_inlines[trait[0]] = (*trait[1], f"use inline {SUPPORT_FOLDER / (TRAIT_INLINE_NAME_TEMPLATE_SUFFIX.format(trait[0], SUFFIX_PLACEHOLDER))}")


    if generate_placeholder_and_include:
        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_trigger_placeholders.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_trigger_placeholders.txt", 'w') as f:
            f.write("# mod_support/tec_trigger_placeholders\n")
            f.write("# This file is autogenerated\n")


            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    scripted_trigger = $trigger$
                    bool = $default$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                    inline_script = {{
                        script = conditional/tec_number
                        value = @tec_{s}_addon_present
                        equal = 1
                        code = "
                            $trigger$_{s} = {{
                                optimize_memory
                                always = $default$
                            }}
                        "
                    }}
                """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_trigger_include.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_trigger_include.txt", 'w') as f:
            f.write("# mod_support/tec_trigger_include\n")
            f.write("# This file is autogenerated\n")


            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    scripted_trigger = $trigger$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                        inline_script = {{
                            script = conditional/tec_number
                            value = @tec_{s}_addon_present
                            equal = 1
                            code = "
                                $trigger$_{s} = yes
                            "
                        }}
                    """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_effect_placeholders.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_effect_placeholders.txt", 'w') as f:
            f.write("# mod_support/tec_effect_placeholders\n")
            f.write("# This file is autogenerated\n")


            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    scripted_effect = $effect$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                    inline_script = {{
                        script = conditional/tec_number
                        value = @tec_{s}_addon_present
                        equal = 1
                        code = "
                            $effect$_{s} = {{
                                optimize_memory
                            }}
                        "
                    }}
                """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_effect_include.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_effect_include.txt", 'w') as f:
            f.write("# mod_support/tec_effect_include\n")
            f.write("# This file is autogenerated\n")


            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    scripted_effect = $effect$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                        inline_script = {{
                            script = conditional/tec_number
                            value = @tec_{s}_addon_present
                            equal = 1
                            code = "
                                $effect$_{s} = {{
                                    $parameters$
                                }}
                            "
                        }}
                    """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_value_placeholders.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_value_placeholders.txt", 'w') as f:
            f.write("# mod_support/tec_value_placeholders\n")
            f.write("# This file is autogenerated\n")

            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    script_value = $value$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                        inline_script = {{
                            script = conditional/tec_number
                            value = @tec_{s}_addon_present
                            equal = 1
                            code = "
                                $value$_{s} = {{
                                    $parameters$
                                    base = 0
                                }}
                            "
                        }}
                    """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_value_include.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_value_include.txt", 'w') as f:
            f.write("# mod_support/tec_value_include\n")
            f.write("# This file is autogenerated\n")

            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    script_value = $value$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                        inline_script = {{
                            script = conditional/tec_number
                            value = @tec_{s}_addon_present
                            equal = 1
                            code = "
                                add = value:$value$_{s}$parameters$
                            "
                        }}
                    """))

        os.makedirs(os.path.dirname(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_inlines_include.txt"), exist_ok=True)
        with open(base_mod_path / f"{INLINE_FOLDER}/mod_support/tec_inlines_include.txt", 'w') as f:
            f.write("# mod_support/tec_inlines_include\n")
            f.write("# This file is autogenerated\n")

            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = tec_type_hint
                    inline = $include_script$
                }}
            """))

            for s in suffixes:
                f.write(textwrap.dedent(f"""\
                    inline_script = {{
                        script = conditional/parts/tec_step
                        x = @tec_{s}_addon_present
                        code = "
                            inline_script = {{
                                script = {SUPPORT_FOLDER}/$include_script$_{s}
                                $parameters$
                            }}
                        "
                    }}
                """))

    os.makedirs(os.path.dirname(base_mod_path / f"{SCRIPTED_TRIGGERS}/!!_{prefix}_addon_triggers.txt"), exist_ok=True)
    with open(base_mod_path / f"{SCRIPTED_TRIGGERS}/!!_{prefix}_addon_triggers.txt", 'w') as f:
        f.write("# This file is autogenerated\n")

        for s in scripted_triggers:
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = mod_support/tec_trigger_placeholders
                    trigger = {s}
                    default = {'yes' if s in scripted_trigger_defaults else 'no'}
                }}
            """))


    os.makedirs(os.path.dirname(base_mod_path / f"{SCRIPT_VALUES}/!!_{prefix}_addon_script_values.txt"), exist_ok=True)
    with open(base_mod_path / f"{SCRIPT_VALUES}/!!_{prefix}_addon_script_values.txt", 'w') as f:
        f.write("# This file is autogenerated\n")
        for s in script_values:
            params = re.sub('\|\$([a-zA-Z_\d]+)\|[a-zA-Z_\d]+\$\|', r"|$\1$|", script_values[s][2]).split('|')[1:-1:2]
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = mod_support/tec_value_placeholders
                    value = {s}
                    parameters = "
                        {' '.join(f"[[{p}]]" for p in params)}
                    "
                }}
            """))

    os.makedirs(os.path.dirname(base_mod_path / f"{SCRIPTED_EFFECTS}/!!_{prefix}_addon_effects.txt"), exist_ok=True)
    with open(base_mod_path / f"{SCRIPTED_EFFECTS}/!!_{prefix}_addon_effects.txt", 'w') as f:
        f.write("# This file is autogenerated\n")

        for s in scripted_effects:
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = mod_support/tec_effect_placeholders
                    effect = {s}
                }}
            """))

    if generate_placeholder_and_include:
        with open(base_mod_path / f"{SCRIPTED_VARIABLES}/zzz_{prefix}_addon_variables.txt", 'w') as f:
            f.write("# This file is autogenerated\n")
            f.write(textwrap.dedent(f"""\
                {new_line.join(f"@tec_{s}_addon_present = 0" for s in suffixes).strip()}
            """))


    with open(base_mod_path / "README_MODDABILITY.md", 'w') as f:
        with open(BASE_PATH / "README_MODDABILITY_TEMPLATE.md", 'r') as r:
            f.writelines(r.readlines())
        f.write(textwrap.dedent(f"""\
            ## Current suffixes
            
            {new_line.join(f"            * {s}" for s in suffixes).strip()}
            
            ## Current supported scripted_triggers
            
            {new_line.join(f"            * [{s}]({scripted_triggers[s][0]}#L{scripted_triggers[s][1]})" for s in sorted(scripted_triggers.keys())).strip()}
            
            ## Current supported scripted_effects
            
            {new_line.join(f"            * [{s}]({scripted_effects[s][0]}#L{scripted_effects[s][1]})" for s in sorted(scripted_effects.keys())).strip()}
            
            ## Current supported scripted_effects
            
            {new_line.join(f"            * [{s}]({script_values[s][0]}#L{script_values[s][1]})" for s in sorted(script_values.keys())).strip()}
            
            ## Current supported inline_scripts
            
            {new_line.join(f"            * [{s[0]}]({s[1][0]}#L{s[1][1]})" for s in sorted(doc_inlines.items())).strip()}
            
            ## Authorities with extendable swaps without overwrites
            
            {new_line.join(f"            * [{s[0]}]({s[1][0]}#L{s[1][1]}) - {s[1][2]}" for s in sorted(auth_inlines.items())).strip()}
            
            ## Traits that can be extended without overwrites
            
            {new_line.join(f"            * [{s[0]}]({s[1][0]}#L{s[1][1]}) - {s[1][2]}" for s in sorted(trait_inlines.items())).strip()}
        """))


@cli.command()
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--base-mod-path', default=Path(BASE_PATH) / '../..')
def generate_tags(config: str, local_config: str, base_mod_path: str):
    base_mod_path = Path(base_mod_path).resolve()
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg

    with open(base_mod_path / "common/scripted_modifiers/zz_evolved_autogenerated_tags_scripted_modifiers.txt", 'w') as f:
        for economic_category, (economic_category_loc, template_key, *args) in cfg['languages']['english']['economic_categories'].items():
            f.write(textwrap.dedent(f"""\
                tec_economic_category_{economic_category}_tag = {{
                    icon = mod_tec_blank
                    neutral = yes
                    category = pop
                    percentage = no
                    localize_with_value_key = yes
                }}
            """))

@cli.command()
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--base-mod-path', default=Path(BASE_PATH) / '../..')
def generate_hoarder_autogen_files(config: str, local_config: str, base_mod_path: str):
    base_mod_path = Path(base_mod_path).resolve()
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg

    cults = []

    haorder_template = ""
    resources = [
        'minerals',
        'food',
        'alloys',
        'consumer_goods',
        'rare_crystals',
        'exotic_gases',
        'volatile_motes',
        'minor_artifacts'
    ]
    with open(base_mod_path / HOARDER_BUTTONS_TEMPLATE) as f:
        haorder_template = f.read().rstrip()

    with open(base_mod_path / "interface/zzz_evolved_autogenerated_hoarder_buttons.gui", 'w') as f:
        f.write('guiTypes = {\n')
        f.write("""
@tec_cui_vault_width = 600
@tec_cui_vault_height = 400
@tec_cui_vault_y = 240
@tec_cui_vault_margin = 15
@tec_cui_vault_margin_internal = 7
@tec_cui_vault_resource = 120
@tec_cui_vault_minerals = 1
@tec_cui_vault_food = 2
@tec_cui_vault_alloys = 3
@tec_cui_vault_consumer_goods = 4
@tec_cui_vault_rare_crystals = 5
@tec_cui_vault_exotic_gases = 6
@tec_cui_vault_volatile_motes = 7
@tec_cui_vault_minor_artifacts = 8
@tec_cui_vault_100_w = 36
@tec_cui_vault_500_w = 36
@tec_cui_vault_1000_w = 44
@tec_cui_vault_10000_w = 52
@tec_cui_vault_M_w = 20
\n""")
        for r in resources:
            f.write(
                haorder_template.replace('$resource$', r) + '\n'
            )
        f.write('\n}')

if __name__ == '__main__':
    cli()
