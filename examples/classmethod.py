from temperature import Temperature

'''
Example of the boiling point of water from celsius to other units.
'''

boiling_point_celsius: int = 100

boiling_point = Temperature.fromcelsius(100)
print(boiling_point)