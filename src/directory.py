import os, shutil
import itertools


"""
Move all files from folder1 to folder2
    - folder1: string, path of soure folder
    - folder2: string, path of destination folder
"""
def moveBetweenFolders(folder1, folder2):
    for root, subdirs, files in os.walk(folder1):
        for file in files:
            path = os.path.join(root, file)
            shutil.move(path, os.path.join(folder2, os.path.relpath(path, folder1)))
