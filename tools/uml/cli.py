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
from tools.uml.utils import load_config, Writer, BASE_PATH, create_sprites_for_cleanup


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
def create_compat_inlines(config: str, local_config: str, base_mod_path: str):
    cfg = load_config(config)
    local_cfg = load_config(local_config)
    cfg |= local_cfg
    base_mod_path = Path(base_mod_path).resolve()

    inlines = []

    for filename in glob.iglob(str(base_mod_path / f"common/inline_scripts/**/**"), recursive=True):
        if ('inline_evolved' in filename
                and '.txt' in filename
                and 'evolved_support' not in filename
                and 'mod_support/tec_inlines_include' not in filename):
            with open(filename, 'r') as f:
                for line in f.readlines():
                    matches = re.match(f"\\s*include_script\\s*=\\s*\"?([a-z_A-Z\\d/]*)\"?", line)
                    if matches and matches.group(1):
                        inlines.append(matches.group(1))

    inlines = list(set(inlines))
    inlines.sort()

    scripted_triggers = {}

    for filename in glob.iglob(str(base_mod_path / f"common/scripted_triggers/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_triggers = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match("\\s*tec_trigger_mod_support\\s*=\\s*{", line)
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
                            scripted_triggers[s] = (filename[len(str(base_mod_path)) + 1:], i + 1)

    scripted_effects = {}

    for filename in glob.iglob(str(base_mod_path / f"common/scripted_effects/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                should_look_for_trigger = False
                lines = f.readlines()
                found_effects = []
                for i, line in enumerate(lines):
                    if not should_look_for_trigger:
                        matches = re.match("\\s*tec_effect_mod_support\\s*=\\s*{", line)
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
                            scripted_effects[s] = (filename[len(str(base_mod_path)) + 1:], i + 1)

    councilor_checks = []

    for filename in glob.iglob(str(base_mod_path / f"common/**/**"), recursive=True):
        if '.txt' in filename:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    matches = re.match("\\s*tec_has_councilor\\s*=\\s*{\\s*COUNCILOR\\s*=\\s*\"?([a-z_A-Z\\d]*)\"?", line)
                    if matches and matches.group(1):
                        councilor_checks.append(matches.group(1))
                    matches = re.match(".*value:tec_councilor_level_multiplier.*\|COUNCILOR\|([a-z_A-Z\\d]*)", line)
                    if matches and matches.group(1):
                        councilor_checks.append(matches.group(1))
                    matches = re.match(".*value:tec_councilor_level_multiplier.*\|COUNCILOR_2\|([a-z_A-Z\\d]*)", line)
                    if matches and matches.group(1):
                        councilor_checks.append(matches.group(1))

    councilor_checks = list(set(councilor_checks))
    councilor_checks.sort()

    suffixes = cfg['addons']['suffixes']
    scripted_trigger_defaults = cfg['addons'].get('scripted_trigger_defaults', [])

    new_line = '\n'

    if (base_mod_path / f"common/inline_scripts/evolved_support").exists():
        shutil.rmtree(base_mod_path / f"common/inline_scripts/evolved_support")

    for inline, suffix in itertools.product(inlines, suffixes):
        os.makedirs(os.path.dirname(base_mod_path / f"common/inline_scripts/evolved_support/{inline}_{suffix}.txt"),
                    exist_ok=True)
        (base_mod_path / f"common/inline_scripts/evolved_support/{inline}_{suffix}.txt").touch()

    with open(base_mod_path / "common/inline_scripts/mod_support/tec_trigger_placeholders.txt", 'w') as f:
        f.write("# mod_support/tec_trigger_placeholders\n")
        f.write("# This file is autogenerated\n")

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

    with open(base_mod_path / "common/inline_scripts/mod_support/tec_effect_placeholders.txt", 'w') as f:
        f.write("# mod_support/tec_effect_placeholders\n")
        f.write("# This file is autogenerated\n")

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

    with open(base_mod_path / "common/inline_scripts/mod_support/tec_inlines_include.txt", 'w') as f:
        f.write("# mod_support/tec_inlines_include\n")
        f.write("# This file is autogenerated\n")

        for s in suffixes:
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = conditional/tec_number_inline
                    value = @tec_{s}_addon_present
                    equal = 1
                    inline = evolved_support/$include_script$_{s}
                    parameters = '
                        $parameters$
                    '
                }}
            """))

    with open(base_mod_path / "common/scripted_triggers/!!_evolved_addon_triggers.txt", 'w') as f:
        f.write("# This file is autogenerated\n")
        sub_string = new_line.join(textwrap.dedent(f"""
            inline_script = {{
                script = conditional/tec_number
                value = @tec_{s}_addon_present
                equal = 1
                code = "
                    $trigger$_{s} = yes
                "
            }}
        """) for s in suffixes)
        f.write(textwrap.dedent(f"""\
            tec_trigger_mod_support = {{
                optimize_memory
                OR = {{
                    {textwrap.indent(sub_string, "                    ", lambda x: x).strip()}
                    always = no
                }}
            }}
        """))
        for s in scripted_triggers:
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = mod_support/tec_trigger_placeholders
                    trigger = {s}
                    default = {'yes' if s in scripted_trigger_defaults else 'no'}
                }}
            """))

    with open(base_mod_path / "common/scripted_effects/!!_evolved_addon_effects.txt", 'w') as f:
        f.write("# This file is autogenerated\n")
        sub_string = new_line.join(textwrap.dedent(f"""\
            inline_script = {{
                script = conditional/tec_number
                value = @tec_{s}_addon_present
                equal = 1
                code = "
                    $effect$_{s} = [[parameters]{{ $parameters$ }}][[!parameters] yes]
                "
            }}
        """) for s in suffixes).strip()
        f.write(textwrap.dedent(f"""\
            tec_effect_mod_support = {{
                optimize_memory
                {textwrap.indent(sub_string, "                ", lambda x: x).strip()}
            }}
        """))
        for s in scripted_effects:
            f.write(textwrap.dedent(f"""\
                inline_script = {{
                    script = mod_support/tec_effect_placeholders
                    effect = {s}
                }}
            """))

    with open(base_mod_path / "common/scripted_variables/zzz_evolved_addon_variables.txt", 'w') as f:
        f.write("# This file is autogenerated\n")
        f.write(textwrap.dedent(f"""\
            {new_line.join(f"@tec_{s}_addon_present = 0" for s in suffixes).strip()}
        """))


    with open(base_mod_path / "README_MODDABILITY.md", 'w') as f:
        with open(base_mod_path / "tools/uml/README_MODDABILITY_TEMPLATE.md", 'r') as r:
            f.writelines(r.readlines())
        f.write(textwrap.dedent(f"""\
            ## Current suffixes
            
            {new_line.join(f"            * {s}" for s in suffixes).strip()}
            
            ## Current supported scripted_triggers
            
            {new_line.join(f"            * [{s}]({scripted_triggers[s][0]}#L{scripted_triggers[s][1]})" for s in sorted(scripted_triggers.keys())).strip()}
            
            ## Current supported scripted_effects
            
            {new_line.join(f"            * [{s}]({scripted_effects[s][0]}#L{scripted_effects[s][1]})" for s in sorted(scripted_effects.keys())).strip()}
            
            ## Current supported inline_scripts
            
            {new_line.join(f"            * [{s}](common/inline_scripts/{s}.txt)" for s in inlines).strip()}
        """))


if __name__ == '__main__':
    cli()
