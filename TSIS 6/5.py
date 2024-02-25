import os

def write_list_to_file(filename, lists):
    with open(filename, 'w') as file:
        for item in lists:
            file.write(str(item) + '\n')


filename = "example.txt"
lists = ["apple", "banana", "orange", "grape"]
write_list_to_file(filename, lists)
