import math

def areaCircle(radio):
    return math.pi * (radio ** 2)

def volumCircle(area, height):
    return areaCircle(radio) * height

radio = 2
print(volumCircle(radio, 4))
