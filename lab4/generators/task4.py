def squares_a_b(a, b):
    number = a
    while number <= b:
        yield number**2
        number+=1

a = int(input("Enter the number (a): "))
b = int(input("Enter the number (b): "))
squares = squares_a_b(a, b)

for square in squares:
    print(square)