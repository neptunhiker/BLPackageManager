def sort_modules(modules: list) -> list:
    """
    Sort the modules given in a list by their order
    :param modules: a list of modules
    :return sorted list of modules
    """
    sorted_modules = sorted(modules, key=lambda module: module.order)

    return sorted_modules

