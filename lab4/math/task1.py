import math

def convert_to_radian(deg):
    return round(deg * (math.pi/180), 6)

degree = float(input('Input degree: '))
print('Output radian:', convert_to_radian(degree))