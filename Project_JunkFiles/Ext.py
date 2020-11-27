import shutil
import os


def Extension(path, Data, organizedPath):
    for data in Data:
        fileName = data[0]
        filePath = data[1]
        extension = data[2]

        if not os.path.exists(organizedPath + extension):
            os.makedirs(organizedPath + extension)

        shutil.move(filePath, organizedPath + extension + '/' + fileName)
