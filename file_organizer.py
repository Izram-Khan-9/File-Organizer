# Importing necessary modules
import os
import shutil

def file_organizer(path):
    print('\n')
    """Organizes files in the given path into folders by extension."""
    print('\n')
    
    # Checking if the path exists
    if os.path.exists(path):

        # Storing all the files present in specified path in a variable name files in the form of a list
        files = os.listdir(path)

        # Running a for loop on the list (files)
        for file in files: 
            full_path = os.path.join(path, file)

            # Skip directories, only organize files
            if os.path.isdir(full_path):
                continue
              
            # Removing the filename and extension because the extension will be the folder name
            filename, extension = os.path.splitext(file)
            # .pdf ---> PDF 
            extension = extension[1:].title()

            # Skip files without an extension
            if not extension:
                continue

            folder_path = os.path.join(path, extension)

            # If a folder name is already present just move the files using shutil.move
            if os.path.exists(folder_path):
                shutil.move(full_path, os.path.join(folder_path, file))
                print(f'\n[{file}] is moved from [{full_path}] to [{os.path.join(folder_path, file)}]')

            # If the folder does not exist create a folder with extension name then move the files
            else:
                os.makedirs(folder_path)
                shutil.move(full_path, os.path.join(folder_path, file))
                print(f'\n[{file}] is moved from [{full_path}] to [{os.path.join(folder_path, file)}]')

    # If user enters an invalid path
    else:
        print('\nFileNotFoundError: Path does not exists!')


# Asking user for path
user_path = input('\nEnter the path: ')
file_organizer(user_path)

#____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 12-Nov-25 [Wednesday](9:00 pm)
# Reference: "https://www.youtube.com/watch?v=KBjBPQExJLw"
# All credit goes to Izram Khan and (Reference)

# What does the program do?

# When you enter the path if path exists it will first store all the files in the path in a list 
# using listdir. Then filename and extension will be separated because a new folder will be created
# with extension name and all the files of specific extension will go the folder. 
# If folder with similar extension name already exists it will move the file to that folder.
# Files without extensions and subdirectories are skipped.
# If the path is wrong it will show FileNotFoundError
