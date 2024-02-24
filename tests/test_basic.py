import pytest
from src.factorial import factorial
from src.fibonacci import fibonacci

@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (6, 720)
])
def test_factorial(input, expected):
    assert factorial(input) == expected

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55)
])
def test_fibonacci(input, expected):
    assert fibonacci(input) == expected