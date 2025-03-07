import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r'\b[A-Z]{1}([a-z]+)+\b'
pattern = r'\b[A-Z]{1}[a-z]+\b'
test(pattern, "Applebananmandarin", "test1", True)
test(pattern, "APplemandarin", "test2", True)
test(pattern, "APPlemandarin", "test6", True)
test(pattern, "applemandarin", "test3", True)
test(pattern, "applemandariN", "test4", True)
test(pattern, "appleMand9arin", "test5", True)