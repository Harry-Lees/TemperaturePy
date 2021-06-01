from temperature import Temperature

start_temp: Temperature = Temperature.fromcelsius(100)

delta_t: Temperature = start_temp - Temperature(50)
print(delta_t)

delta_t += Temperature.fromrankine(100)
print(delta_t)

delta_t *= Temperature.fromfarenheit(500)
print(delta_t)