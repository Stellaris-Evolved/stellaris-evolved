import os
from typing import Optional, TextIO, BinaryIO

from yaml import FullLoader

from .types import Config, ResourceStr
import yaml
import codecs

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

def load_config(path: str) -> Config:
    with open(path, 'r', encoding='utf8') as f:
        return yaml.load(f, FullLoader)


def generate_localization(loc_key: str, loc_str: str, number: Optional[int] = None):
    return f" {loc_key}:{number if number is not None else ''} \"{loc_str}\""


def generate_resource_loc(resource: ResourceStr):
    if isinstance(resource, str):
        return f"£{resource}£ ${resource}$"
    else:
        return resource[1]


class Writer:
    def __init__(self, file: str):
        self.file = file
        self._spacer = WriterSpacer(self)

    def __enter__(self):
        self.io: BinaryIO = open(self.file, 'wb')
        self.io.write(codecs.BOM_UTF8)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.io.close()

    def write(self, s: str):
        self.io.write(s.encode("utf-8"))

    def write_language(self, lang_key: str):
        self.write(f"l_{lang_key}:\n")

    def write_localization(self, loc_key: str, loc_str: str, number: Optional[int] = None):
        self.write(generate_localization(loc_key, loc_str, number) + '\n')

    def write_comment(self, comment: str):
        self.write(f" # {comment}\n")

    def write_spacer(self):
        self.write('\n')

    def with_spacer(self):
        return self._spacer


class WriterSpacer:
    def __init__(self, writer: Writer):
        self.writer = writer

    def __enter__(self):
        self.writer.write_spacer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
