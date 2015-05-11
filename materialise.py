import ast
import os
import os.path

with open('setup.py') as f:
    tree = ast.parse(f.read(), f.name)

pil_modules = []

for child in ast.iter_child_nodes(tree):
    try:
        if child.value.func.id != 'setup':
            continue
        for keyword in child.value.keywords:
            if keyword.arg != 'packages':
                continue
            for element in keyword.value.elts:
                pil_modules.append(element.s)
    except AttributeError as e:
        continue

for module in pil_modules:
    try:
        os.mkdir(module)
    except OSError:
        pass
    with open(os.path.join(module, '__init__.py'), 'w') as f:
        f.write('"""Compatibility shim for PIL\'s `{module}`."""\n'.format(module=module))
        f.write('from PIL.{module} import *\n'.format(module=module))

with open('.git/info/exclude', 'w') as f:
    for line in pil_modules:
        f.write(line + '\n')
