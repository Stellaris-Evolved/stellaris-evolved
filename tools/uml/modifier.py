from typing import Optional, List

from .types import LanguageConfig, ModifierType, ResourceStr, PRODUCES_ADD, PRODUCES_MULT, \
    UPKEEP_MULT, UPKEEP_ADD, EconomicCategoryKey, COST_MULT, COST_ADD
from .utils import Writer, generate_resource_loc


def _unpack_resource_id(resource: ResourceStr):
    return resource if isinstance(resource, str) else resource[0]


def _get_loc_from_args(economic_category_loc: str, modifier_type: ModifierType, args: list):
    if len(args) and isinstance(args[-1], dict):
        if modifier_type.split('_')[-1] in args[-1]:
            return args[-1][modifier_type.split('_')[-1]]
    return economic_category_loc


def _should_write_custom_add(args: list, resource: ResourceStr, modifier_type: ModifierType):
    if isinstance(resource, list) and len(resource) == 3:
        if not modifier_type.replace('add', 'mult') in resource[2]:
            return True
    return 'mult' in args[-1] if len(args) and isinstance(args[-1], dict) else False


def _generate_modifier_localization_key(economic_category: EconomicCategoryKey, modifier_type: ModifierType,
                                        resource: Optional[ResourceStr] = None):
    return f"mod_{economic_category}_{_unpack_resource_id(resource) + '_' if resource else ''}{modifier_type}"


def _resource_has_modifier_type(resource: ResourceStr, modifier_type: ModifierType):
    if isinstance(resource, list) and len(resource) == 3:
        return modifier_type in resource[2]
    return True


def _generate_resource_mult_modifier(
        writer: Writer, economic_category: EconomicCategoryKey, modifier_type: ModifierType,
        template: str, economic_category_loc: str, args: list, resource: Optional[ResourceStr] = None):
    writer.write_localization(
        _generate_modifier_localization_key(economic_category, modifier_type, resource),
        template.format(
            *args,
            resource=generate_resource_loc(resource) if resource else None,
            category=_get_loc_from_args(economic_category_loc, modifier_type, args)
        ),
    )


def _generate_resource_add_modifier(
        writer: Writer, economic_category: EconomicCategoryKey, modifier_type: ModifierType,
        template: str, economic_category_loc: str, args: list, resource: Optional[ResourceStr] = None):
    if _should_write_custom_add(args, resource, modifier_type):
        writer.write_localization(
            _generate_modifier_localization_key(economic_category, modifier_type, resource),
            template.format(
                *args,
                resource=generate_resource_loc(
                    resource),
                category=_get_loc_from_args(economic_category_loc, modifier_type, args)
            ),
        )
    else:
        writer.write_localization(
            _generate_modifier_localization_key(economic_category, modifier_type, resource),
            f"${_generate_modifier_localization_key(economic_category, modifier_type.replace('add', 'mult'), resource)}$",
        )


def _get_resources(resources: List[ResourceStr], args: list):
    if len(args) and isinstance(args[-1], dict):
        if 'resources' in args[-1]:
            return [r for r in resources if r in args[-1]['resources'] or isinstance(r, list) and r[0] in args[-1]['resources']]
    return resources


def generate_modifiers(writer: Writer, config: LanguageConfig, resources: list[ResourceStr]):
    for economic_category, (economic_category_loc, template_key, *args) in config['economic_categories'].items():
        template = config['templates'][template_key]
        with writer.with_spacer():
            writer.write_comment(
                f"{economic_category} - {economic_category_loc}{f' - {args}' if len(args) > 0 else ''}")

            writer.write_localization(
                f"mod_base_{economic_category}",
                f"{economic_category_loc}",
            )

            with writer.with_spacer():
                for key in template:
                    if 'generic' in key:
                        _generate_resource_mult_modifier(
                            writer, economic_category, key.split('_')[-1] + '_mult',
                            template[key], economic_category_loc, args
                        )
        for key in template:
            if 'resource' in key:
                modifier_type: ModifierType = key.split('_')[-1] + '_mult'
                with writer.with_spacer():
                    for resource in _get_resources(resources, args):
                        if _resource_has_modifier_type(resource, modifier_type):
                            _generate_resource_mult_modifier(
                                writer, economic_category, modifier_type,
                                template[key], economic_category_loc, args, resource
                            )

                modifier_type: ModifierType = key.split('_')[-1] + '_add'
                with writer.with_spacer():
                    for resource in _get_resources(resources, args):
                        if _resource_has_modifier_type(resource, modifier_type):
                            _generate_resource_add_modifier(
                                writer, economic_category, modifier_type,
                                template[key], economic_category_loc, args, resource
                            )
