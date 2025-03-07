import re

def to_camel(s):
    pattern = r'(?:^|_)(\w)'
    result = re.sub(pattern, lambda x: x.group(1).upper(), s)
    return result

snake_inp = str(input())
print(to_camel(snake_inp))