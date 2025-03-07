def divisible_3_4(n):
    number = 0
    while number <= n:
        if number%3==0  and number%4==0:
            yield number
        number+=1

n = int(input("Enter the number n: "))
divisible = divisible_3_4(n)

for num in divisible:
    print(num)