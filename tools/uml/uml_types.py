from pathlib import Path
from typing import TypeAlias, TypedDict, Literal, Optional

TemplateKey: TypeAlias = str
TemplateStr: TypeAlias = str
LanguageStr: TypeAlias = str
AuthorityStr: TypeAlias = str
ResourceStr: TypeAlias = str | tuple[str, Optional[str], Optional[str], Optional[str]]
EconomicCategoryKey: TypeAlias = str
EconomicCategory: TypeAlias = tuple[str, TemplateKey]
EconomicCategories: TypeAlias = dict[EconomicCategoryKey, EconomicCategory]
ResourcesConfig: TypeAlias = dict[ResourceStr, str]
DistrictsAndBuildings: TypeAlias = dict[str, tuple[str, TemplateKey]]
Job: TypeAlias = tuple[TemplateKey, Optional[str]]
Jobs: TypeAlias = dict[str, Job]
Paths: TypeAlias = list[Path]

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
    add: TemplateStr | None
    per_pop: TemplateStr | None
    per_pop_short: TemplateStr | None


Templates = dict[TemplateKey, TemplateConfig]


class LanguageConfig(TypedDict):
    templates: Templates
    economic_categories: EconomicCategories
    districts_and_buildings: DistrictsAndBuildings
    jobs: Jobs


class MissingSpritesConfig(TypedDict):
    default: str
    errors: str


class Addons(TypedDict):
    scripted_trigger_defaults: list[str]
    suffixes: list[str]

class Config(TypedDict):
    languages: dict[LanguageStr, LanguageConfig]
    resources: list[ResourceStr]
    authorities: list[AuthorityStr]
    paths: Paths
    mod_paths: Paths
    missing_sprites: Optional[MissingSpritesConfig]
    addons: Addons

