mytuple = (True, False, True, True)
mytuple1 = (1, 1, 1, 1, 1, 1)

def f(mytuple):
    return all(mytuple)

print(f(mytuple))
print(f(mytuple1))