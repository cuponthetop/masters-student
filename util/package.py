"""
"""


def import_name_from_package(package_path, name, target_name):
    """
    An approximate implementation of import.
    Import a name from package as a target_name
    """

    import importlib.util
    import sys

    if target_name in sys.modules:
        raise ImportError(
            'other module is already imported as %s' % target_name)

    absolute_name = importlib.util.resolve_name(name, package_path)

    if absolute_name in sys.modules:
        sys.modules[target_name] = sys.modules[absolute_name]
        return sys.modules[target_name]

    path = None

    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.spec.submodule_search_locations

    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        raise ImportError('No module named %s' % absolute_name)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    sys.modules[target_name] = module

    if path is not None:
        setattr(parent_module, child_name, module)

    return module
