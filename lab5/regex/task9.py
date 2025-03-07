import re

def replF(match_obj):
    return match_obj.group('X') + " " + match_obj.group('Y')

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern,replF, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r'(?P<X>[a-zA-Z])(?P<Y>[A-Z])'
pattern2 = r'(\w)([A-Z])'
test(pattern, "MySuperTest", "test1", "My Super Test")
test(pattern, " MySuperTest IAmRobot", "test2", " My Super Test I Am Robot")