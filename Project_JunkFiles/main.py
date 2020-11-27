from stat import ST_SIZE
import argparse
import os
import Size
import Date
import Ext


def main():
    parameter = argparse.ArgumentParser()

    # To get the path and options from the command line.

    parameter.add_argument('--path', default='.', help='path to organize')
    parameter.add_argument('-c', default='ext', help='ChoiceBy', 
                           choices=['ext', 'size', 'date', 'count'])

    args = parameter.parse_args()
    Arrange(args)


# recursively list out all the files.
file_Data = []


def Get_Data(path):
    for file in os.scandir(path):
        if not file.is_dir():
            fileName = file.name
            filePath = file.path
            fileExtension = fileName.split('.')[-1]
            fileSize = os.stat(filePath)[ST_SIZE]
            file_Data.append([fileName, filePath, fileExtension, fileSize])
        else:
            file_Data + [data for data in (Get_Data(file.path))]
    return file_Data


def CountFiles(path, Data, organizedPath):
    total = 0
    for base, dirs, files in os.walk(path):
        print('Looking in : ', base)
        for Files in files:
            total += 1
            print(Files)
    print('Number of files', total)
    print(dirs)


def Arrange(args):
    path = args.path
    ChoiceBy = args.c

    # For exception handling during wrong path input
    try:
        Data = Get_Data(path)
    except FileNotFoundError:
        print('Invalid path directory')
        return

    if not os.path.exists(path + '/Arrange'):
        os.makedirs(path + '/Arrange')
    organizedPath = path + '/Arrange/'

    OBJ_MAP = {
        "ext": Ext.Extension,
        "size": Size.Size,
        "date": Date.Date,
        "count": CountFiles
        }
    OBJ_MAP.get(ChoiceBy)(path, Data, organizedPath)


print('Done')


# Driver code


if __name__ == '__main__':
    main()
