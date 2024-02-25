import os

def analyze_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print("Path exists.")
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")


path = input()
analyze_path(path)
