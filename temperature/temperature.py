from __future__ import annotations

from numbers import Real

ABSOLUTE_ZERO: float = 0.0 # in Kelvin
ABSOLUTE_HOT: float = 1.416785e32 # in Kelvin

class Temperature:
    '''
    Simple Temperature class for converting between different units of temperature.
    Default temperature unit is Kelvin.
    '''

    def __init__(self, temp: Real) -> None:
        if not isinstance(temp, Real):
            raise TypeError('Temperature must be a Real number')

        if temp < ABSOLUTE_ZERO:
            raise ValueError('Temperature cannot be below Absolute Zero')
        elif temp > ABSOLUTE_HOT: # type: ignore
            raise ValueError('Temperature cannot be above Absolute Hot')
        self._t: Real = temp

    def __repr__(self) -> str:
        return f'Temperature(kelvin={round(self.kelvin, 2)}, celsius={round(self.celsius, 2)}, farenheit={round(self.farenheit, 2)}, rankine={round(self.rankine, 2)})'

    def __eq__(self, other) -> bool:
        return self._t == other._t

    def __lt__(self, other) -> bool:
        return self._t < other._t

    def __add__(self, other) -> Temperature:
        return Temperature(self._t + other._t)

    def __sub__(self, other) -> Temperature:
        return Temperature(self._t - other._t)

    def __mul__(self, other) -> Temperature:
        return Temperature(self._t * other._t)

    @classmethod
    def fromfarenheit(cls, temp: Real) -> Temperature:
        return cls(Temperature.ftok(temp))

    @classmethod
    def fromcelsius(cls, temp: Real) -> Temperature:
        return cls(Temperature.ctok(temp))

    @classmethod
    def fromrankine(cls, temp: Real) -> Temperature:
        return cls(Temperature.rtok(temp))

    @property
    def kelvin(self) -> Real:
        '''Return the temperature in Kelvin'''

        return self._t

    @kelvin.setter
    def kelvin(self, temp: Real) -> None:
        if temp < ABSOLUTE_ZERO:
            raise ValueError('Temperature cannot be below Absolute Zero')
        elif temp > ABSOLUTE_HOT: # type: ignore
            raise ValueError('Temperature cannot be above Absolute Hot')

        self._t = temp

    @property
    def celsius(self) -> Real:
        '''temperature in celsius'''

        return self.ktoc(self.kelvin)

    @celsius.setter
    def celsius(self, temp: Real) -> None:
        self.kelvin = self.ctok(temp)

    @property
    def farenheit(self) -> Real:
        '''temperature in farenheit'''

        return self.ktof(self.kelvin)

    @farenheit.setter
    def farenheit(self, temp: Real) -> None:
        self.kelvin = self.ftok(temp)

    @property
    def rankine(self) -> Real:
        '''temperature in Rankine'''

        return self.ktor(self.kelvin)

    @rankine.setter
    def rankine(self, temp) -> None:
        self.kelvin = self.rtok(temp)

    @staticmethod
    def ctok(c: Real) -> Real:
        '''convert Celsius to Kelvin'''
        return c + 273.15

    @staticmethod
    def ktoc(k: Real) -> Real:
        '''convert Kelvin to Celsius'''
        return k - 273.15

    @staticmethod
    def ktof(k: Real) -> Real:
        '''convert Kelvin to Farenheit'''
        return (k - 273.15) * 9/5 + 32

    @staticmethod
    def ftok(f: Real) -> Real:
        '''convert Farenheit to Kelvin'''
        return (f - 32) * 5/9 + 273.15

    @staticmethod
    def ktor(k: Real) -> Real:
        '''convert Kelvin to Rakine'''
        return k * 1.8

    @staticmethod
    def rtok(r: Real) -> Real:
        '''convert Rakine to Kelvin'''
        return r * 5/9

    @staticmethod
    def ftoc(f: Real) -> Real:
        '''convert Farenheit to Celsius'''
        return (f - 32) / 1.8

    @staticmethod
    def ctof(c: Real) -> Real:
        '''convert Celsius to Farenheit'''
        return 1.8 * c + 32

    @staticmethod
    def ctor(c: Real) -> Real:
        '''convert Celsius to Rankine'''
        return c * 9/5 + 491.67

    @staticmethod
    def rtoc(r: Real) -> Real:
        '''convert Rankine to Celsius'''
        return (r - 491.67) * 5/9