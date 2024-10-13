import pytest
from my_math import add_numbers

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(3, 5) == 8
    assert add_numbers(0, 0) == 0
    assert add_numbers(-2, 4) == 2

def test_add_numbers_typeerror():
    """Test if TypeError is raised when invalid types are passed."""
    with pytest.raises(TypeError):
        add_numbers("a", 1)
