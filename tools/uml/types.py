from typing import TypeAlias, TypedDict, Literal, Optional

TemplateKey: TypeAlias = str
TemplateStr: TypeAlias = str
LanguageStr: TypeAlias = str
ResourceStr: TypeAlias = str | tuple[str, str]
EconomicCategoryKey: TypeAlias = str

EconomicCategory: TypeAlias = tuple[str, TemplateKey]
EconomicCategories: TypeAlias = dict[EconomicCategoryKey, EconomicCategory]
ResourcesConfig: TypeAlias = dict[ResourceStr, str]
DistrictsAndBuildings: TypeAlias = dict[str, tuple[str, TemplateKey]]

PRODUCES_ADD = 'produces_add'
PRODUCES_MULT = 'produces_mult'
UPKEEP_ADD = 'upkeep_add'
UPKEEP_MULT = 'upkeep_mult'
COST_ADD = 'cost_add'
COST_MULT = 'cost_mult'

ModifierType: TypeAlias = Literal['produces_add', 'produces_mult', 'upkeep_add', 'upkeep_mult', 'cost_add', 'cost_mult']


class TemplateConfig(TypedDict):
    generic_produces: TemplateStr | None
    generic_upkeep:  TemplateStr | None
    generic_cost: TemplateStr | None
    resource_produces: TemplateStr | None
    resource_upkeep: TemplateStr | None
    resource_cost: TemplateStr | None
    build_speed: TemplateStr | None
    max_add: TemplateStr | None


Templates = dict[TemplateKey, TemplateConfig]


class LanguageConfig(TypedDict):
    templates: Templates
    economic_categories: EconomicCategories
    districts_and_buildings: DistrictsAndBuildings


class Config(TypedDict):
    languages: dict[LanguageStr, LanguageConfig]
    resources: list[ResourceStr]

