def nums_from_n_to_0(n):
    while n >= 0:
        yield n
        n = n-1

n = int(input())
nums = nums_from_n_to_0(n)

for num in nums:
    print(num)