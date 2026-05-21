import os
import shutil
from pathlib import Path

def file_organizer(path):
    '''Organize files in the given directory'''

    if not os.path.exists(path):
        return
    
    files = os.listdir(path)
    
    for filename in files:
        file = Path(path) / filename
         
        if file.is_dir():
            continue
        
        suffix = file.suffix
        
        if not suffix:
            continue
        
        folder = Path(path) / suffix[1:].upper()
        
        if not folder.exists():
            folder.mkdir(parents=True)
            
        shutil.move(str(file), str(folder))
        print(f'\n{file} is moved to {folder}')
    
    
path = input('\nEnter path: ')
file_organizer(path=path)

# Date created: 21-May-2026
