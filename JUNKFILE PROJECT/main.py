from stat import ST_SIZE
import argparse
import os
import bysize
import bydate
import byext


def main():
    parameter = argparse.ArgumentParser()

    # To get the path and options from the command line.

    parameter.add_argument('--path', default="E:\\experiment\\dumpy4", 
                           help='path to organize')
    parameter.add_argument('-o', default='ext', help='Organize by', 
                           choices=['ext', 'size', 'date', 'count'])

    args = parameter.parse_args()
    organize(args)


# recursively list out all the files.
file_Data = []


def get_Data(path):
    for file in os.scandir(path):
        if not file.is_dir():
            fileName = file.name
            filePath = file.path
            fileExtension = fileName.split('.')[-1]
            fileSize = os.stat(filePath)[ST_SIZE]
            file_Data.append([fileName, filePath, fileExtension, fileSize])
        else:
            file_Data + [data for data in (get_Data(file.path))]
    return file_Data


def countFiles(path, Data, organizedPath):
    total = 0
    for base, dirs, files in os.walk(path):
        print('Looking in : ', base)
        for Files in files:
            total += 1
            print(Files)
    print('Number of files', total)
    print(dirs)    


def organize(args):
    path = args.path
    organizeBy = args.o

    # For exception handling during wrong path input
    try:
        Data = get_Data(path)
    except FileNotFoundError:
        print('Invalid path directory')
        return

    if not os.path.exists(path + '/Arrange'):
        os.makedirs(path + '/Arrange')
    organizedPath = path + '/Arrange/'

    if organizeBy == 'ext':
        byext.byExtension(path, Data, organizedPath)
    elif organizeBy == 'size':
        bysize.bySize(path, Data, organizedPath)
    elif organizeBy == 'date':
        bydate.bydate(path, Data, organizedPath)
    elif organizeBy == 'count':
        countFiles(path, Data, organizedPath)


print('Done')

# Driver code


if __name__ == '__main__':
    main()
