import os

def rename_files():
    file_list = os.listdir("/Users/christopherreece/Documents/Github/Python/fs_nano_degree/prank")
    current_directory = os.getcwd()

    # Create translation table
    translation_table = dict.fromkeys(map(ord, '0123456789'), None)

    os.chdir("/Users/christopherreece/Documents/Github/Python/fs_nano_degree/prank")

    for file_name in file_list:
        new_name = file_name.translate(translation_table)
        print('Old name: ' + file_name)
        print('New name: ' + new_name)
        os.rename(file_name, file_name.translate(translation_table))

    os.chdir(current_directory)
