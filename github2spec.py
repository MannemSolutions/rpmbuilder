#!/usr/bin/env python
import requests
import re
import os.path
import yaml

from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class githubrepo(dict):
    __site = "github.com"
    __organization = ""
    __repository = ""
    __release = ""
    __asset_filter = None

    def __init__(self, values):
        self.__organization = values.get('organization')
        self.__repository = values.get('repository')
        self.__release = values.get('release', 'latest')
        self.__asset_filter = re.compile(values.get('asset_filter', '.'))
        self['url'] = 'https://{}/{}/{}'.format(self.__site, self.__organization, self.__repository)
        self.get_release_info()
        self.update(values)

    def get_repo_info(self):
        url = 'https://api.{}/repos/{}/{}'.format(self.__site, self.__organization, self.__repository)
        result = requests.get(url)
        data = result.json()
        repo_info = {}
        repo_info['name'] = data['name']
        repo_info['description'] = data['description']
        repo_info['license'] = data['license']['spdx_id']
        self.update(repo_info)
        return repo_info
    
    def get_release_info(self):
        self.get_repo_info()
        url = 'https://api.{}/repos/{}/{}/releases/{}'.format(self.__site, self.__organization, self.__repository, self.__release)
        result = requests.get(url)
        data = result.json()

        self['release_info'] = release_info = {}
        release_info['version'] = data['tag_name'].replace('-', '.')
        release_info['changelog'] = data['body']
        release_info['assets'] = release_assets = []
        for asset in data['assets']:
            if self.__asset_filter.search(asset['name']):
                release_assets.append({ 'name': asset['name'], 'url': asset['browser_download_url']})
        self.update(release_info)
        return release_info


def main():
    repos = yaml.load(open('github2spec.yaml'), Loader=Loader)
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    for name, values in repos.items():
        repo = githubrepo(values)
        template = env.get_template("spec.j2")
        with open(os.path.join('specs', name+'.spec'), 'w') as specfile:
            specfile.write(template.render(repoinfo=repo))


if __name__ == '__main__':
    main()

