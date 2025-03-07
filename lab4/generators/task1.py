def sqr_N(n):
    number = 1
    while number <= n:
        yield number**2
        number+=1
N = int(input("Enter the number N: "))
squares = sqr_N(N)

for square in squares:
    print(square) 