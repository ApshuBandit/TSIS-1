import re

def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)


test_string = "This_is_a_test_string_with_some_sequences_like_this_one_and_this_also"
sequences = find_sequences(test_string)
print("Sequences found:")
for seq in sequences:
    print(seq)
