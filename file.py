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

        # If the folder does not exist create a folder with extension name. (Line: 19) then move the files
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file,  path+'/'+extension+'/'+file)
            print(f'\n[{file}] is moved from [{path+'/'+file}] to [{path+'/'+extension+'/'+file}]')

# If user enters an invalid path
else:
    print('\nFileNotFoundError: Path does not exists!')


