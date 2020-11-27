from datetime import datetime
import time
import shutil
import os


def Date(path, Data, organizedPath):

    name = os.listdir(path)
    name.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,
             f))]
    os.chdir(path)
    for x in files:

        # Get the creation time

        create_time = time.ctime(os.path.getmtime(os.path.join(path, x)))
        create_dt = datetime.strptime(create_time, '%a %b %d %H:%M:%S %Y')
        modified_date = str(create_dt.day) + '-' + str(
                        create_dt.month) + '-' + str(create_dt.year)

        if(os.path.isdir(organizedPath + modified_date)):
            shutil.move(os.path.join(path, x), organizedPath + modified_date)

        else:

            os.makedirs(organizedPath + modified_date)
            shutil.move(os.path.join(path, x), organizedPath + modified_date)
