#######################################################################################################
#   Problem Statement : Design automation script which accept two directory names. Copy all
#   files from first directory into second directory. Second directory should be created at run time
#######################################################################################################
import os
import sys
import time
import shutil

#######################################################################################################
#   Function Name   :   DirectoryWatcher
#   Input           :   Connamd Line Argument
#   Output          :
#   Description     :   Copy all files from first directory into second directory
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#######################################################################################################


def DirectoryWatcher(DirNmae1, DirName2, Extention):

    Flag = os.path.isabs(DirNmae1)

    if (Flag == False):

        DirNmae1 = os.path.abspath(DirNmae1)

    Exits = os.path.exists(DirNmae1)

    if (Exits == True):

        Path = os.path.join(DirNmae1, DirName2)

        os.mkdir(Path)

        Path = os.path.abspath(Path)

        for FolderName, SubFolderName, FileName in os.walk(DirNmae1):
            for Name in FileName:
                if Name.endswith(Extention):
                    shutil.copy(os.path.join(DirNmae1, Name), Path)

    else:

        print("This directory is not present")
        
#######################################################################################################
#   Entery Point Function
#######################################################################################################


def main():

    print("---------------------- Directory Watcher ----------------------")

    if (len(sys.argv) == 2):

        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This script is used to perform Directory traversal")
            exit()

        if ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Usage of the script : ")
            print("Name_Of_File  Name_Of_Directory  Name_Of_Directory  File_extension")
            exit()

    if (len(sys.argv) == 4):

        try:
            Starttime = time.time()
            DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3],)
            Endtime = time.time()
            print("Time required to execute the script is : ", Starttime - Endtime)

        except Exception as Obj:
            print("Exception for : ", Obj)

    else:
        print("Invalid input")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

    print("--------------- Thank you for using our script ----------------")

    return 0


#######################################################################################################
#   Starter
#######################################################################################################
if __name__ == "__main__":
    main()

#######################################################################################################
#   Output :
#
#######################################################################################################
