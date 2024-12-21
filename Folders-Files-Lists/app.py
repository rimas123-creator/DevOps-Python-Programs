import os

def get_files():
    folders = input("Enter the Folder name in spaces: \n").split()
    for folder in folders:
        try:
            files = os.listdir(folder)
            print(f" The Folder : {folder}")
            for file in files:
                print(f" ===== The FileName : {file} =====" )
        except FileNotFoundError:
            print(" The given folder does exists please give the valid folder "+ folder)
            break
        except PermissionError:
            print("Permission denied for the given folder "+ folder)
            break

get_files()