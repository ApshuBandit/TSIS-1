import os

def delete_file(file_path):
    
    if not os.path.exists(file_path):
        print("File does not exist")
        return
    

    if not os.access(file_path, os.W_OK):
        print("No permission")
        return


    try:
        os.remove(file_path)
        print("File deleted")
    except OSError as e:
        print(f"Error: {e}")


file_path = input()
delete_file(file_path)
