from fizz_buzz.fizz_buzz import fizz_buzz
import pytest

def test_one():
    actual = fizz_buzz(1)
    expected = '1'

    assert actual == expected

def test_two():
    actual = fizz_buzz(2)
    expected = '2'

    assert actual == expected

def test_three():
    actual = fizz_buzz(3)
    expected = 'fizz'

    assert actual == expected

def test_four():
    actual = fizz_buzz(4)
    expected = '4'

    assert actual == expected

def test_five():
    actual = fizz_buzz(5)
    expected = 'buzz'

    assert actual == expected

def test_six():
    actual = fizz_buzz(6)
    expected = 'fizz'

    assert actual == expected

def test_fifteen():
    actual = fizz_buzz(15)
    expected = 'fizz buzz'

    assert actual == expected

def test_negative():
    actual = fizz_buzz(- 15)
    expected = 'fizz buzz'

    assert actual == expected

def test_string():
    actual = fizz_buzz('Hello')
    expected = 'Only integer values are allowed'

    assert actual == expected


# 3! = 3*2*1
# 5! = 5*4*3*2*1