#!/usr/bin/env python

import sys
from graphviz import Digraph
from glob import glob
import yaml

dot = Digraph(comment='Ansible Roles',format='png')

# load all roles
index = 0
role_nodes = {}
for path in glob('roles/*'):
    role = path.split('/')[1]
    index += 1
    role_nodes[role] = str(index)
    dot.node(str(index), role)

# add role dependencies
for path in glob('roles/*/meta/main.yml'):
    role = path.split('/')[1]
    with open(path, 'r') as file:
        for dependency in yaml.load(file, Loader=yaml.FullLoader)['dependencies']:
            depended_role = dependency['role']
            dot.edge(role_nodes[role], role_nodes[depended_role])

dot.render('doc/ansible-roles') 