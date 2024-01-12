# test_my_module.py
from my_module import add_numbers

def test_add_numbers():
    # Test case 1
    result = add_numbers(3, 5)
    assert result == 8

    # Test case 2
    result = add_numbers(-2, 7)
    assert result == 5

    # Test case 3
    result = add_numbers(-4, -6)
    assert result == -10
