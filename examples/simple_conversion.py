from temperature import Temperature

celsius: int = 25

print(Temperature.ctok(celsius)) # Temperature in Kelvin
print(Temperature.ctof(celsius)) # Temperature in Farenheit
print(Temperature.ctor(celsius)) # Temperature in Rankine