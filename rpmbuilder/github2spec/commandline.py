#!/usr/bin/env python3
"""
Create spec files from Github repos using the GithubRepo class
"""
import os
import yaml
from .githubrepo import GithubRepo

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def from_config():
    """
    Read a yaml config file and loop through repositories to create specs
    :return:
    """
    config_file = os.environ.get('GITHUB2SPEC_CONFIG',
                                 '/usr/rpmbuilder/conf/github2spec.yaml')
    dest = os.environ.get('GITHUB2SPEC_DEST', '/tmp')
    with open(config_file, encoding='utf-8') as config_data:
        config = yaml.load(config_data, Loader=Loader)
        repos = config['repositories']
        with open(config['template'], encoding='utf-8') as template_file:
            template = template_file.read()
        dest = config.get('dest', dest)
        for name, values in repos.items():
            values['name'] = name
            repo = GithubRepo(values)
            dest_file = os.path.join(dest,
                                     f'{name}-{repo["package_arch"]}.spec')
            print(f'Writing to {dest_file}')
            with open(dest_file, 'w', encoding='utf-8') as spec_file:
                spec_file.write(repo.recursive_render(template))


if __name__ == '__main__':
    from_config()
