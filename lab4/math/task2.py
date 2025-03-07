def area_trap(a, b, h):
    return (a+b)*h/2

h = float(input('Height: '))
a = float(input('Base, first value: '))
b = float(input('Base, second value: '))

print('Expected Output:', area_trap(a, b, h))