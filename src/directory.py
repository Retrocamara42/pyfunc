import os


def moveBetweenFolders(folder1, folder2):
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                img = Image.open(basepath+entry.name)
