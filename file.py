# Importing necessary modules
import os
import shutil

# Asking user for path
path = input('\nEnter the path: ')

# Checking if the path exists
if os.path.exists(path):

    # Storing all the files present in specified path in a variable name files in the form of a list
    files = os.listdir(path)

    # Running a for loop on the list (files)
    for file in files: 
        # Removing the filename and extension because the extension will be the folder name
        filename, extension = os.path.splitext(file)
        # .pdf ---> PDF 
        extension = extension[1:].title()

        # If a folder name is already present just move the files using shutil.move
        if os.path.exists(path+'/'+ extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            print(f'\n[{file}] is moved from [{path+'/'+file}] to [{path+'/'+extension+'/'+file}]')

        # If the folder does not exist create a folder with extension name(Line: 19) then move the files
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file,  path+'/'+extension+'/'+file)
            print(f'\n[{file}] is moved from [{path+'/'+file}] to [{path+'/'+extension+'/'+file}]')

# If user enters an invalid path
else:
    print('\nFileNotFoundError: Path does not exists!')

#____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 12-Nov-25 [Wednesday](9:00 pm)
# Reference: "https://www.youtube.com/watch?v=KBjBPQExJLw"
# All credit goes to Izram Khan and (Reference)

# What does the program do?

# When you enter the path if path exists it will first store all the files in the path in a list 
# using listdir. Then filename and extension will be separated because a new folder will be created
# with extension name and all the files of specific extnsion will go the folder If folder with 
# similar extension name already exists it will move the file to that folder.
# If the path is wrong it will show FileNotFoundError
