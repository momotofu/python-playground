import os
import random

## TODO:
# Write a program that takes a secret message,
# And then arranges the pictures for you.
# Then shuffles or encodes the message.

def rename_files(directory):
    file_list = os.listdir(directory)
    current_directory = os.getcwd()

    # Create translation table
    translation_table = dict.fromkeys(map(ord, '0123456789'), None)
    os.chdir(directory)

    for file_name in file_list:
        new_name = file_name.translate(translation_table)
        print('Old name: ' + file_name)
        print('New name: ' + new_name)
        os.rename(file_name, file_name.translate(translation_table))

    os.chdir(current_directory)

def scramble_files(directory):
    file_dir = directory
    file_list = os.listdir(file_dir)
    working_dir = os.getcwd()

    os.chdir(file_dir)

    for file_name in file_list:
        random_num = random.randint(1, 1000)
        os.rename(file_name, str(random_num) + file_name)

    os.chdir(working_dir)
