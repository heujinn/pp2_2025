import re

def f(s):
    pattern = r'[ .,]'
    s1 = re.sub(pattern,':', s)
    return s1

s = str(input())
print(f(s))