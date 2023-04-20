# -*- coding: utf-8 -*-
import os

import click as click

from .modifier import generate_modifiers, generate_buildings_loc
from .utils import load_config, Writer, BASE_PATH


@click.group()
def cli():
    pass


@cli.command()
@click.option('--config', default=f'{BASE_PATH}/config.yml')
@click.option('--output', default=f'{BASE_PATH}/localisation/{{language}}/replace/zzzz_uml_modifier_l_{{language}}.yml')
def generate_loc(config: str, output: str):
    cfg = load_config(config)

    resources = cfg['resources']
    for language, lang_cfg in cfg['languages'].items():
        os.makedirs(os.path.dirname(output.format(language=language)), exist_ok=True)
        with Writer(output.format(language=language)) as writer:
            writer.write_language(language)

            with writer.with_spacer():
                generate_modifiers(writer, lang_cfg, resources)

            with writer.with_spacer():
                generate_buildings_loc(writer, lang_cfg)



if __name__ == '__main__':
    cli()

    
   