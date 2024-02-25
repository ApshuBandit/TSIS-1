import os

path = "C:\Program Files"


def list_files(path):
    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
def list_all_contents(path):
    return os.listdir(path)

print(os.listdir(path))
print("Files:", list_files(path))
