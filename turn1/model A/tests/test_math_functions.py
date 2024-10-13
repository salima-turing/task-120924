import pytest
from my_math_module import math_functions


def test_add_numbers():
    assert math_functions.add_numbers(10, 20) == 30


def test_subtract_numbers():
    assert math_functions.subtract_numbers(20, 10) == 10


if __name__ == "__main__":
    pytest.main()
