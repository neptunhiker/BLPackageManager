from .. import database
from ..utils import sorting


def test_sort_modules():

    a_module = database.Module(name="Final module",
                               description="module description",
                               order=3)

    b_module = database.Module(name="Middle module",
                               description="module description",
                               order=2)

    c_module = database.Module(name="Start module",
                               description="module description",
                               order=1)

    d_module = database.Module(name="Some Start module",
                               description="module description",
                               order=1)

    e_module = database.Module(name="One more final module",
                               description="module description",
                               order=3)

    modules = [a_module, b_module, c_module, d_module, e_module]

    sorted_modules = sorting.sort_modules(modules)

    # check that the first two modules start are in the beginning of the list
    assert sorted_modules[0].order== 1
    assert sorted_modules[1].order == 1

    # check that the third module is a middle module
    assert sorted_modules[2].order == 2

    # check that the last two modules are final orders
    assert sorted_modules[3].order == 3
    assert sorted_modules[4].order == 3
