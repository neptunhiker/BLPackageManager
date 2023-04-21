import pytest
from ..utils import placement

def test_module_placement():
    assert placement.module_placement(nr_of_modules=3) == {0: 3, 1: 0, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=4) == {0: 4, 1: 0, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=5) == {0: 5, 1: 0, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=6) == {0: 3, 1: 3, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=7) == {0: 4, 1: 3, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=8) == {0: 4, 1: 4, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=9) == {0: 5, 1: 4, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=10) == {0: 5, 1: 5, 2: 0, 3:0}
    assert placement.module_placement(nr_of_modules=11) == {0: 4, 1: 4, 2: 3, 3:0}
    assert placement.module_placement(nr_of_modules=12) == {0: 4, 1: 4, 2: 4, 3:0}
    assert placement.module_placement(nr_of_modules=13) == {0: 5, 1: 4, 2: 4, 3:0}
    assert placement.module_placement(nr_of_modules=14) == {0: 5, 1: 5, 2: 4, 3:0}
    assert placement.module_placement(nr_of_modules=15) == {0: 5, 1: 5, 2: 5, 3:0}
    assert placement.module_placement(nr_of_modules=16) == {0: 4, 1: 4, 2: 4, 3:4}
    assert placement.module_placement(nr_of_modules=17) == {0: 5, 1: 4, 2: 4, 3:4}
    assert placement.module_placement(nr_of_modules=18) == {0: 5, 1: 5, 2: 4, 3:4}
    assert placement.module_placement(nr_of_modules=19) == {0: 5, 1: 5, 2: 5, 3:4}
    assert placement.module_placement(nr_of_modules=20) == {0: 5, 1: 5, 2: 5, 3:5}

def test_module_placement_for_overview():
    """
    Test the placement algo for placing modules onto the overview page nicely
    """
    assert placement.module_place_overview(nr_of_modules=1) == {0: 1, 1: 0}
    assert placement.module_place_overview(nr_of_modules=2) == {0: 2, 1: 0}
    assert placement.module_place_overview(nr_of_modules=3) == {0: 3, 1: 0}
    assert placement.module_place_overview(nr_of_modules=4) == {0: 4, 1: 0}
    assert placement.module_place_overview(nr_of_modules=5) == {0: 5, 1: 0}
    assert placement.module_place_overview(nr_of_modules=6) == {0: 3, 1: 3}
    assert placement.module_place_overview(nr_of_modules=7) == {0: 4, 1: 3}
    assert placement.module_place_overview(nr_of_modules=15) == {0: 8, 1: 7}
    assert placement.module_place_overview(nr_of_modules=16) == {0: 8, 1: 8}


if __name__ == "__main__":
    pytest.main()