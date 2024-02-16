import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)


test_string = "ThisIsA_TestString_withSomeSequencesLikeThisOneAndThisAlso"
sequences = find_sequences(test_string)
print("Sequences found:")
for seq in sequences:
    print(seq)
