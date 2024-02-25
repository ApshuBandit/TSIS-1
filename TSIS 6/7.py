import os
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())


source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
