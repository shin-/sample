import pytest

from sample import adder, multiplier, concatenator, ArgException


def test_adder():
    assert adder(1, 2, 3) == 6
    assert adder() == 0

    with pytest.raises(ArgException):
        adder(1, '2', 3)


def test_multiplier():
    assert multiplier(2, 5, 3) == 30
    assert multiplier() == 1

    with pytest.raises(ArgException):
        multiplier(1, 2.5, 4)


def test_concatenator():
    assert concatenator('a', 'b', 'c') == 'abc'
    assert concatenator() == ''
    assert concatenator('a', 10, int, 3.5) == "a10<class 'int'>3.5"
