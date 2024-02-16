import re

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)


test_string = "ThisIsAStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(test_string)
print("Original string:", test_string)
print("Modified string:", result)
