from temperature.temperature import Temperature
from fractions import Fraction

import pytest

near_absolute_hot  = Temperature(1e32)
near_absolute_cold = Temperature(1)
room_temperature   = Temperature(294)

def test_lt():
    assert (near_absolute_cold < room_temperature) == True


def test_add():
    assert (room_temperature + room_temperature) == Temperature(588)


def test_add_too_hot():
    with pytest.raises(ValueError):
        near_absolute_hot + near_absolute_hot


def test_add_fractions():
    assert Temperature(Fraction(1, 2)) + Temperature(Fraction(1, 2)) == Temperature(1)


def test_mult():
    assert (room_temperature * room_temperature) == Temperature(86436)


def test_mult_too_hot():
    with pytest.raises(ValueError):
        near_absolute_hot * near_absolute_hot


def test_sub():
    assert (room_temperature - room_temperature) == Temperature(0)


def test_sub_too_cold():
    with pytest.raises(ValueError):
        near_absolute_cold - room_temperature


def test_to_kelvin():
    assert room_temperature.kelvin == 294


def test_to_celsius_floats():
    assert pytest.approx(room_temperature.celsius, 0.1) == 20.85


def test_to_farenheit():
    assert pytest.approx(room_temperature.farenheit) == 69.53


def test_to_rankine():
    assert room_temperature.rankine == 529.2