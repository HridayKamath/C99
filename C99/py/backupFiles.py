import shutil
import os
import shutil

source = input("Enter name of source folder: ")
destination = input("Enter name of destination folder: ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)