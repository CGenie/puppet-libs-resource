#!/usr/bin/env python

from fabric import api as fabric_api
import os
import yaml


GIT_REPO = 'https://github.com/stackforge/fuel-library'
TMP_DIR = '/tmp/fuel-library'
MANIFESTS_DIR = 'deployment/puppet'
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))


META_YAML_TEMPLATE = {
    'id': '{name}',
    'handler': 'puppet',
    'puppet_module': '{name}',
    'version': '1.0.0',
    'input': {
        'ip': {
            'schema': 'str!',
            'value': '',
        },
        'ssh_key': {
            'schema': 'str!',
            'value': '',
        },
        'ssh_user': {
            'schema': 'str!',
            'value': '',
        },
    },
    'tags': [],
}


def clone_stackforge():
    if not os.path.exists(TMP_DIR):
        fabric_api.local('git clone {} {}'.format(GIT_REPO, TMP_DIR))
    else:
        with fabric_api.lcd(TMP_DIR):
            fabric_api.local('git pull')


def analyze_manifest(name):
    print 'Analyzing manifest {}'.format(name)

    resource_dir = os.path.join(LOCAL_DIR, name)
    actions_dir = os.path.join(resource_dir, 'actions')
    resource_manifests_dir = os.path.join(resource_dir, 'puppet')
    manifests_dir = os.path.join(TMP_DIR, MANIFESTS_DIR, name, 'manifests')

    meta_path = os.path.join(resource_dir, 'meta.yaml')
    if not os.path.exists(manifests_dir):
        return

    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir)

    if not os.path.exists(meta_path):
        meta_content = yaml.dump(META_YAML_TEMPLATE, default_flow_style=False)
        meta_content = meta_content.format(name=name)

        with open(meta_path, 'w') as f:
            f.write(meta_content)

    if not os.path.exists(actions_dir):
        os.makedirs(actions_dir)

        with open(os.path.join(actions_dir, 'run.pp'), 'w') as f:
            f.write('')

        with open(os.path.join(actions_dir, 'remove.pp'), 'w') as f:
            f.write('')

    if not os.path.exists(resource_manifests_dir):
        os.makedirs(resource_manifests_dir)

    fabric_api.local(
        'cp -R {}/* {}'.format(manifests_dir, resource_manifests_dir)
    )


def main():
    clone_stackforge()

    for name in os.listdir(os.path.join(TMP_DIR, MANIFESTS_DIR)):
        analyze_manifest(name)


if __name__ == '__main__':
    main()
