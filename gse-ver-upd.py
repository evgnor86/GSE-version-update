import os
import json


def run(base_dir: str, shell_version: str) -> None:

    dirs: list = [dir_name for dir_name in os.listdir(base_dir) if dir_name[0] != '.']

    print(f'\n{"GNOME Shell Extension name:":50} {"Extension version:":25} GNOME Shell versions:\n')
    for dir_name in dirs:
        metadata = json.load(open(f'{base_dir}/{dir_name}/metadata.json'))
        metadata['shell-version'].append(shell_version) if shell_version not in metadata['shell-version'] else None
        version = str(metadata['version']) if 'version' in metadata.keys() else ''
        print(f'{metadata["name"]:50} {version:25} {metadata["shell-version"]}')
        json.dump(metadata, open(f'{base_dir}/{dir_name}/metadata.json', 'w'), indent=4)


if __name__ == '__main__':
    run('./extensions/', '43')
