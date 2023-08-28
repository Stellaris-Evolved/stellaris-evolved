import os
import re
from pathlib import Path


def extract_keys_to_replace(path: Path, replace_string: str, language: str):
    keys_to_replace = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            if f'l_{language}' in f:
                continue
            matches = re.match(f"^\\s*([a-zA-Z_\\d]*):\\d?\\s*\"{replace_string}\"", line)
            if matches and matches.group(1):
                keys_to_replace[matches.group(1)] = replace_string
    return keys_to_replace


def copy_locs_from_folder(path: Path, language: str, keys_to_search: set, replace_dict: dict):
    if not path.exists():
        return
    for loc_file in os.listdir(path):
        if not (path / loc_file).is_file():
            continue
        with open(path / loc_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not len(line):
                    continue
                if f'l_{language}' in f:
                    continue
                tmp = line.split(':')
                if tmp[0] in keys_to_search:
                    k = tmp[0]
                    matches = re.match(f"^{k}:\\d?\\s*\"(.*)\"", line)
                    if matches and matches.group(1):
                        replace_dict[k] = matches.group(1)
                        keys_to_search.remove(k)


def replace_keys(path: Path, replace_dict: dict, replace_string: str):
    with open(path, 'r') as f:
        s = f.readlines()
    for k, v in replace_dict.items():
        if v == replace_string:
            continue
        v = v.replace('\\', '\\\\')
        for i, line in enumerate(s):
            if not len(line):
                continue
            s[i] = re.sub(f"{k}:\\d*\\s*\"{replace_string}\"", f"{k}: \"{v}\"", line)

    with open(path, 'w') as f:
        f.write(''.join(s))
