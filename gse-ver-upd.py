import os
import json


def run(base_dir: str, version: str) -> None:

    dirs: list = [dir_name for dir_name in os.listdir(base_dir) if dir_name[0] != '.']

    for dir_name in dirs:
        metadata = json.load(open(f'{base_dir}/{dir_name}/metadata.json'))
        metadata['shell-version'].append(version) if version not in metadata['shell-version'] else None
        print(f'{dir_name} {metadata["shell-version"]}')
        json.dump(metadata, open(f'{base_dir}/{dir_name}/metadata.json', 'w'), indent=4)


if __name__ == '__main__':
    run('./extensions/', '43')
