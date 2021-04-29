############################################################################
# This is the path where you want to search
path = r'C:\'

# This is the extension you want to detect
extension = '.sav'

for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
            print(file_name)
            print(file_name_path)
