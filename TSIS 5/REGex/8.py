import re

def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)

# Test the function
test_string = "SplitThisStringAtUpperCaseLetters"
result = split_at_uppercase(test_string)
print("Original string:", test_string)
print("Split result:", result)
