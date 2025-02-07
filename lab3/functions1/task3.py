heads = 35
legs = 94
''' 
x - num of rabbits y - num of chickens

x + y = 35 -> x = 35 - y
4x + 2y = 94 -> x = (94 - 2y)/4

35 - y = (94 - 2y)/4 -> 2y = 35*4 - 94 -> y = (35*4 - 94)/2 -> y = 23

x = 35 - y -> x = 12
'''

def solve(numheads, numlegs):
    chicken = (numheads*4 - legs)/2
    rabbit = heads - chicken 
    print(rabbit)
    print(chicken)

solve(heads, legs)