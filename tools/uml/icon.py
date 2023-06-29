from pathlib import Path

from wand import image

from tools.uml.utils import BASE_PATH
from .uml_types import Paths, ResourceStr, Jobs, Job


def resolve_path(path: str, sources: Paths) -> Path:
    for source in sources:
        if (source / path).exists():
            return source / path
    raise Exception(f"{path} not found in any of the sources")


def find_resource_icon(resource: str, sources: Paths) -> image.Image:
    path = resolve_path(f"gfx/interface/icons/resources/{resource}.dds", sources)
    with image.Image(filename=path) as img:
        return img.clone()


def find_job_icon(job: str, sources: Paths) -> image.Image:
    try:
        path = resolve_path(f"gfx/interface/icons/jobs/job_{job}.dds", sources)
        with image.Image(filename=path) as img:
            return img.clone()
    except:
        print(f"Using default job icon since {job} is missing")
        path = resolve_path(f"gfx/interface/icons/jobs/default.dds", sources)
        with image.Image(filename=path) as img:
            return img.clone()


def get_icon(icon: str):
    with image.Image(filename=Path(f"{BASE_PATH}/icons/{icon}.png")) as img:
        return img.clone()


ADD = get_icon('add')
COST = get_icon('cost')
MULT = get_icon('mult')
MULT_YELLOW = get_icon('mult_yellow')
UPKEEP = get_icon('upkeep')


def generate_resource_modifier_icons(resource: str, sources: Paths, base_mod_path: Path):
    res_icon: image.Image

    def create_icon(offset_x: int, offset_y: int, icons: list[image.Image], preffix: str, suffix: str):
        with image.Image(width=25, height=25) as img:
            with res_icon.clone() as res:
                res.resize(18, 18)
                img.options['dds:mipmaps'] = '0'
                img.compression = 'no'
                img.composite(res, left=offset_x, top=offset_y)
                for icon in icons:
                    img.composite(icon)
                img.save(filename=(base_mod_path / f"gfx/interface/icons/modifiers/mod_{preffix}{resource}{suffix}.dds"))

    try:
        res_icon = find_resource_icon(resource, sources)

        create_icon(3, 0, [COST, ADD],  '', '_cost_add')
        create_icon(3, 0, [COST, MULT], '', '_cost_mult')
        create_icon(2, 2, [ADD], '', '_produces_add')
        create_icon(2, 2, [MULT], '', '_produces_mult')
        create_icon(2, 2, [ADD], 'resource_', '_add')
        create_icon(2, 2, [MULT_YELLOW], 'resource_', '_mult')
        create_icon(0, 3, [UPKEEP, ADD], '', '_upkeep_add')
        create_icon(0, 3, [UPKEEP, MULT], '', '_upkeep_mult')

    except Exception as e:
        print(e)


def generate_resource_icons(resources: list[ResourceStr], paths: Paths, base_mod_path: Path):
    for resource in resources:
        if isinstance(resource, list) and len(resource) >= 4 and resource[3]:
            generate_resource_modifier_icons(resource[0], paths, base_mod_path)


def generate_job_modifier_icons(job: str, actual_job_icon: str, sources: Paths, base_mod_path: Path):
    job_icon: image.Image

    def create_icon(offset_x: int, offset_y: int, icons: list[image.Image]):
        with image.Image(width=25, height=25) as img:
            with job_icon.clone() as res:
                res.resize(25, 25)
                img.options['dds:mipmaps'] = '0'
                img.compression = 'no'
                img.composite(res, left=offset_x, top=offset_y)
                for icon in icons:
                    img.composite(icon)
                img.save(filename=(base_mod_path / f"gfx/interface/icons/modifiers/mod_job_{job}_add.dds"))

    try:
        job_icon = find_job_icon(actual_job_icon, sources)

        create_icon(0, 0, [ADD])

    except Exception as e:
        print(e)


def generate_job_icons(jobs: Jobs, paths: Paths, base_mod_path: Path):
    for key, job in jobs.items():
        generate_job_modifier_icons(key, key if len(job) == 1 else job[1], paths, base_mod_path)