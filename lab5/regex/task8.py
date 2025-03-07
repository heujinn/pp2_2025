import re

def f(s):
    pattern = r'[A-Z][a-z]*'
    with_splint = re.findall(pattern, s)
    result = ' '.join(with_splint)
    return result

s = str(input())
print(f(s))