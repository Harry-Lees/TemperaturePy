from temperature.temperature import Temperature
from fractions import Fraction

import pytest

near_absolute_hot  = Temperature(1e32)
near_absolute_cold = Temperature(1)
room_temperature   = Temperature(294)

def test_lt():
    assert (near_absolute_cold < room_temperature) is True

def test_mt():
    assert (near_absolute_cold > room_temperature) is False

def test_eq():
    assert room_temperature == room_temperature

def test_not_eq():
    assert near_absolute_hot != near_absolute_cold

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

def test_from_celsius():
    t = Temperature.fromcelsius(100)
    assert pytest.approx(t.celsius) == 100.0

def test_from_farenheit():
    t = Temperature.fromfarenheit(100)
    assert pytest.approx(t.farenheit) == 100.0

def test_from_rankine():
    t = Temperature.fromrankine(100)
    assert pytest.approx(t.rankine) == 100.0

def test_from_kelvin():
    t = Temperature(100)
    assert t.kelvin == 100.0

def test_ktoc():
    c = Temperature.ktoc(500)
    assert pytest.approx(c) == 226.85

def test_ctok():
    k = Temperature.ctok(500)
    assert pytest.approx(k) == 773.15

def test_ktor():
    r = Temperature.ktor(100)
    assert r == 180

def test_rtok():
    k = Temperature.rtok(180)
    assert k == 100

def test_rtoc():
    c = Temperature.rtoc(500)
    assert pytest.approx(c) == 4.62778

def test_ctor():
    r = Temperature.ctor(1)
    assert r == 493.47

def test_ctof():
    f = Temperature.ctof(1)
    assert f == 33.8

def test_ftoc():
    c = Temperature.ftoc(1)
    assert pytest.approx(c) == -17.22222222222222

def test_change_rankine():
    temp = Temperature(100)

    assert temp.rankine != 100
    temp.rankine = 100
    assert temp.rankine == 100

def test_change_celsius():
    temp = Temperature(100)

    assert temp.celsius != 100
    temp.celsius = 100
    assert temp.celsius == 100

def test_change_farenheit():
    temp = Temperature(100)

    assert temp.farenheit != 100
    temp.farenheit = 100
    assert pytest.approx(temp.farenheit) == 100

def test_change_kelvin():
    temp = Temperature(100)

    assert temp.kelvin != 150
    temp.kelvin = 150
    assert temp.kelvin == 150