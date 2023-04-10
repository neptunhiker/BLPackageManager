def module_placement(nr_of_modules) -> dict:
    """
    Determine how many modules shall be placed in rows and columns
    :return dict: a dictionary that contains the number of columns in the values and the respective row as key
    """
    if nr_of_modules <= 5:
        return {0: nr_of_modules, 1: 0, 2: 0}
    elif nr_of_modules == 6:
        return {0: 3, 1: 3, 2: 0}
    elif nr_of_modules in [7, 8]:
        return {0: 4, 1: nr_of_modules - 4, 2: 0}
    elif nr_of_modules in [9, 10]:
        return {0: 5, 1: nr_of_modules - 5, 2: 0}
    elif nr_of_modules in [11, 12]:
        return {0: 4, 1: 4, 2: nr_of_modules - 8}
    elif nr_of_modules == 13:
        return {0: 5, 1: 4, 2: 4}
    elif nr_of_modules == 14:
        return {0: 5, 1: 5, 2: 4}
    elif nr_of_modules == 15:
        return {0: 5, 1: 5, 2: 5}
    