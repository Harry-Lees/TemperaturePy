from temperature import Temperature

room_temp_celsius: int = 25

print(Temperature.ctok(room_temp_celsius)) # Temperature in Kelvin
print(Temperature.ctof(room_temp_celsius)) # Temperature in Farenheit
print(Temperature.ctor(room_temp_celsius)) # Temperature in Rankine