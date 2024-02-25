import os



def checkk(path):
    exist = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writeable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK )

    print(f"Path: {path}")
    print(f"Exists: {exist}")
    print(f"Readable: {readable}")
    print(f"Writable: {writeable}")
    print(f"Executable: {executable}")


path = input()
checkk(path)