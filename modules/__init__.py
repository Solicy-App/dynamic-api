import os
from importlib import import_module

available_modules = {}

for filename in os.listdir('modules'):
    if filename.endswith(".py") and not filename.startswith("_"):
        module_name = os.path.splitext(filename)[0]
        module = import_module('modules.' + module_name)
        available_modules[module_name] = {
            'process': module.process,
            'schema': module.schema,
        }
