import pytest
from recursion.factorial import factorial

def test_one():
    actual = factorial(1)
    expected = 1

    assert  actual == expected

def test_two():
    actual = factorial(2)
    expected = 2

    assert  actual == expected

def test_three():
    actual = factorial(3)
    expected = 6

    assert  actual == expected

def test_zero():
    actual = factorial(0)
    expected = 1

    assert  actual == expected