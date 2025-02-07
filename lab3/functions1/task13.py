import random

def guess_the_number(n, name):
    cnt = 0
    while True:
        print('Take a guess.\n')
        m = int(input())
        cnt += 1

        if m == n:
            print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
            break
        elif m > n:
            print('Your guess is too high.')
        elif m < n:
            print('Your guess is too low.')

print('Hello! What is your name?')
name = str(input())

print(f'Well, {name}, I am thinking of a number between 1 and 20.')

n = random.randint(1, 20)

guess_the_number(n, name)