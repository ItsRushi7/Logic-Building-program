#######################################################################################################
#   Problem Statement :  Design automation script which accept directory name and 
#   display checksum of all files.
#######################################################################################################
import os
import sys
import time
import hashlib

#######################################################################################################
#   Function Name   :   Calculate_CheckSum
#   Input           :   FileName
#   Output          :   HexaDigit
#   Description     :   Display all CheckSum
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#######################################################################################################
def Calculate_CheckSum(Path):

    Open_File = open(Path, "rb")

    Read_File = Open_File.read()

    MD5 = hashlib.md5()

    MD5.update(Read_File)

    Open_File.close()

    return MD5.hexdigest()

#######################################################################################################
#   Function Name   :   DirectoryWatcher
#   Input           :   Connamd Line Argument
#   Output          :   In Log File
#   Description     :   Copy all files from first directory into second directory
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#######################################################################################################
def DirectoryWatcher(DirName):

    Flag = os.path.isabs(DirName)

    if (Flag == False):

        DirName = os.path.abspath(DirName)

    Exist = os.path.isdir(DirName)

    if (Exist == True):

        print("Directory is exits.....!")

        for FolderName, SubFolderName, FileName in os.walk(DirName):
            for Name in FileName:
                Path = os.path.join(DirName, Name)
                HashFile = Calculate_CheckSum(Path)
                print("Checksum of file ", Name, HashFile)
                print()

    else:
        print("Directory does not exits")
        
#######################################################################################################
#   Entery Point Function
#######################################################################################################
def main():

    print("------------------------------ Directory Watcher ------------------------------")

    if (len(sys.argv) == 2):

        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This script is used to perform Directory traversal")
            exit()

        if ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Usage of the script : ")
            print("Name_Of_File  Name_Of_Directory  Name_Of_Directory  File_extension")
            exit()

        try:
            Starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            Endtime = time.time()
            print("Time required to execute the script is : ", Starttime - Endtime)

        except Exception as Obj:
            print("Exception for : ", Obj)

    else:
        print("Invalid input")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

    
    print("------------------------------ Directory Watcher ------------------------------")

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
