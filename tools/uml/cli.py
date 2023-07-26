# -*- coding: utf-8 -*-
import os
from pathlib import Path

import click as click

from tools.uml.icon import generate_resource_icons, generate_job_icons
from .modifier import generate_modifiers, generate_buildings_loc, generate_jobs_loc
from .utils import load_config, Writer, BASE_PATH, create_sprites_for_cleanup


@click.group()
def cli():
    pass


@cli.command()
@click.option('--config', default=Path(BASE_PATH) / 'config.yml')
@click.option('--local-config', default=Path(BASE_PATH) / 'local_config.yml')
@click.option('--output', default=Path(BASE_PATH) / f'../../localisation/{{language}}/replace/zzzz_uml_modifier_l_{{language}}.yml')
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


if __name__ == '__main__':
    cli()
