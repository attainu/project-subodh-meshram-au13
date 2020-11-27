import os
import shutil


def Size(path, Data, organizedPath):
    for data in Data:
        fileName = data[0]
        filePath = data[1]
        size = data[3]

        if 0 <= size < 1000:  # bytes
            if not os.path.exists(organizedPath + 'BYTES'):
                os.makedirs(organizedPath + 'BYTES')

            shutil.move(filePath, organizedPath + 'BYTES/' + fileName)

        elif 1000 < size < 1000000:  # KiloBytes
            if not os.path.exists(organizedPath + 'KB'):
                os.makedirs(organizedPath + 'KB')

            shutil.move(filePath, organizedPath + 'KB/' + fileName)

        elif 1000000 < size < 100000000:  # MegaBytes
            if not os.path.exists(organizedPath + 'MB'):
                os.makedirs(organizedPath + 'MB')

            shutil.move(filePath, organizedPath + 'MB/' + fileName)

        # If any file more than 100 MB
        else:
            if not os.path.exists(organizedPath + 'more than MB'):
                os.makedirs(organizedPath + 'more than MB')

            shutil.move(filePath, organizedPath + 'more than MB/' + fileName)
