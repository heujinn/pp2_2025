import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r'^a.*b$'
test(pattern, "afjjfddfdfjagdjb", "test1", True)
test(pattern, "abababababbbb", "test2", True)
test(pattern, "ajnfdjkdfvfdhv", "test6", True)
test(pattern, "AAkmdkab", "test3", True)
test(pattern, "jdfjsdfhjdshf", "test4", True)
test(pattern, "appleMandarin", "test5", True)