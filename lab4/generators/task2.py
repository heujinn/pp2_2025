def evennumbers(n):
    num = 0
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1

n = int(input("Enter the number n: "))
evens = evennumbers(n)

print(", ".join(map(str, evens)))
