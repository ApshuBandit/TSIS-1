import os


def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count


filename = "example.txt"  
lines = count_lines(filename)
print("Number of lines in the file:", lines)
