string = str(input())

def isPolindrom(stirng):
    reversed_string = ''.join(c for c in reversed(string))
    if reversed_string == string:
        return 'Polindrom'
    else:
        return 'Not polindrom'

print(isPolindrom(string))