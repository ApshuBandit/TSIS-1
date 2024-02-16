import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)


input_text = "This is a test, with some spaces. And, some commas too."
output_text = replace_with_colon(input_text)
print("Original text:", input_text)
print("Modified text:", output_text)
