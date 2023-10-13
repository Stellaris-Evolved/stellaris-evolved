# UML

UML is a tool for automatically generating economic category modifiers and a few other goodies (such as modifiers for fake resources etc) ensuring consistency of modifiers

## Installing Dependencies

### Python

Python can be installed from `https://www.python.org/downloads/` or be installed by running the shortcut `python` in Powershell to install it form Windows Store

### Python Dependencies

Run in therminal the following command, from root folder:

```
pip install -r ./tools/uml/requirements.txt
```

## Running the Tool

Run in terminal the following command, from root folder:

```
python -m tools.uml.cli generate-loc
```

or if ya wanna use non defaults

```
python -m tools.uml.cli generate-loc --config <path to config> --output <path to output>
```

For Stellaris Evolved I would recommand doing:

```
python -m tools.uml.cli generate-loc --config ./tools/uml/config.yml --output ./localisation/english/replace/zzzz_uml_modifier_l_english.yml --base-mod-path . --missing-sprites-output
```

or for linux

```bash
python -m tools.uml.cli generate-loc --config ./tools/uml/config.yml --output ./localisation/english/replace/zzzz_uml_modifier_l_english.yml --base-mod-path . --missing-sprites-output "./interface/\!\!_missing_sprites_cleanup.gfx"
```
## Generating moddability support

```bash
python -m tools.uml.cli create-compat-inlines --config ./tools/uml/config.yml  
```