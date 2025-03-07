
import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r'ab*'
test(pattern, "12345", "test1", True)
test(pattern, "123ab45as", "test2", True)
test(pattern, "123ab452", "test3", True)
test(pattern, "123abb452", "test4", True)
test(pattern, "abbb452", "test5", True)