# TemperaturePy
![Workflow](https://github.com/Harry-Lees/TemperaturePy/actions/workflows/workflow.yaml/badge.svg)

A Simple temperature conversion library for Python 3.

## Installation

This package is available for download on PyPi

```python
python3 -m pip install temperaturepy
```

## Examples

Easy Conversions
```python
>> from temperature import Temperature
>> celsius: int = 25
>> kelvin: Temperature = Temperature.ctok(celsius)
>> kelvin
298.15
```

Simple maths and comparisons built in
```python
>> from temperature import Temperature
>> start_temp: Temperature = Temperature(150)
>> end_temp: Temperature = Temperature(100)
>> delta_t = start_temp - end_temp
>> delta_t
Temperature(kelvin=50, celsius=-223.15, farenheit=-369.67, rankine=90.0)
```

Clamped to real bounds
```python
>> from temperature import Temperature
>> impossible = Temperature(-1)
ValueError: Temperature cannot be below Absolute Zero
```

For more examples, please see the examples folder.

## License

This project is released under the MIT license
