import math 
def area_r_p(n, r):
    return round((n*r*r)/(4*math.tan(math.pi/n)))

n = int(input('Input number of sides: '))
r = int(input('Input the length of a side: '))

print('The area of the polygon is:', area_r_p(n, r))
