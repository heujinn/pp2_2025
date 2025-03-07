import re

def to_snake(s):
    result = re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()
    return result

camel_inp = str(input())
print(to_snake(camel_inp))

