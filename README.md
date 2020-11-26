Python-Project - JUNK FILES ORGANIZER
Python Project based on Junk File Organizer.


NEED :
I made this Project to simplify my file Organization in a specific folder, it takes a lot of time 
to organize the different files in my system.
----------------------------------------------------------------------------------------------------

Technology Stack Used
​This project uses a number of open source tools, technologies and frameworks to work properly:​
Visual Studio Code - A code editor redefined and optimized for building and debugging modern web 
and cloud applications.Flake8 - static analysis of source code checking for symantec discrepancies


Built using:
Python language
The code is built according to the standard pep8 rules and regulations.


LIBRARIES USED :
import os - to get all the files from the directories,to create directories.
import shutil - to move the files from one directory to another.
import datetime - to get the datetime the files are deployed in that directory.

---------------------------------------------------------------------------------------------------------

APPROACH USED :
For Extension based organization - For the Extension based organization we have created a file types and saved all 
the possible extensions I can think of to access the extensions and afterwords moving the files to their specified 
directories. Checking the extension of the file in the computer directory and then compairing it with the dictionary 
values of extensions if matched then creating the new directory and inside it moving the different files according to 
the specified new directories.

For date/Time based organization - Fetching the date/time for the files stored inside the directories. After finding
out the days it is bin stored, the files are then moved to different directories according to the number of days by 
comparing it using the condition statements.

For SIZE based organization - I have used a variable(size) to store the size of the file and then checking the file 
size by using the if and elif conditions and then arranging the files into their specific folders by creating new 
directories as per the size of the files. All the files are first moved into (Organized Directory) then inside this 
folder all the other directories are created accordingly. files are arranged in the subsequent folders(BYTES,KB,MB,GB)

-----------------------------------------------------------------------------------------------------------------------

How To Run This Project File :
1.Store the junk file in main.py file in your system anywhere you want.
2.Go to terminal type python3 main.py "add path" "add option"example : extension,date,size.
3.Hit the Enter and run button



By default, the directory will be the current directory path and option will be extension.
- python3 main.py --path /E:/../ -c extension           ---- Organize byExtension wise
- python3 main.py --path /E:/../ -c date                ----- Organize by date wise
- python3 main.py --path /E:/../ -c size                ------ Organize by size wise
- python3 main.py --path /E:/../ -c countfile           ------ User can count file in directory