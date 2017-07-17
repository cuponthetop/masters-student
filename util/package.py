"""
"""


def import_package_from_config(config):
    """
    :param config: the configuration file specifying package path and class name to import
                    configuration must have "name" field and "package" field
    :return: imported class (specified by config["name"]) from specified package (by config["package"])
    """
    import util.constant as const
    import importlib

    try:
        class_name = config[const.CFG_NAME]
    except KeyError:
        raise KeyError('Field named "name" was not found from configuration')

    try:
        package_name = config[const.CFG_PACKAGE]
    except KeyError:
        raise KeyError('Field named "package" was not found from configuration')

    mod = importlib.import_module(package_name)

    return getattr(mod, class_name)
