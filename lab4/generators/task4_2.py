def squares_a_b(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("Enter the number (a): "))
b = int(input("Enter the number (b): "))
squares = squares_a_b(a, b)

for square in squares:
    print(square)