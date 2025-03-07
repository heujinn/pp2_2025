def nums_from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
nums = nums_from_n_to_0(n)

for num in nums:
    print(num)