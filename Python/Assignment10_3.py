#######################################################################################################
#   Problem Statement : Design automation script which accept two directory names. Copy all 
#   files from first directory into second directory. Second directory should be created at run time
#######################################################################################################
import sys
import os
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
def DirectoryWatcher(DirName1, DirName2):

    Flag1 = os.path.isabs(DirName1)

    if (Flag1 == False):
        
        DirName1 = os.path.abspath(DirName1)
    
    Exist = os.path.isdir(DirName1) 
    
    if (Exist == True):
        
        print("Directory is exits.....!") 
        
        path =os.path.join(DirName1,DirName2)
     
        os.mkdir(path) 
        
        DirName2 = os.path.join(DirName1,DirName2)
        
        DirName2 = os.path.abspath(DirName2) 
        
        for FolderName, SubFolderName, FileName in os.walk(DirName1):
            for Name in FileName:
                Copy = os.path.join(FolderName,Name)
                shutil.copy(Copy,DirName2)
    else:
        print("Directory does not exits")   

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
            print("Name_Of_File  Name_Of_Directory  File_extension1  File_extension2")
            exit()

    if (len(sys.argv) == 3):

        try:
            Starttime = time.time()
            DirectoryWatcher(sys.argv[1], sys.argv[2])
            Endtime = time.time()
            print("Time required to execute the script is : ", Starttime - Endtime)

        except Exception as Obj:
            print("Unable to perform the task due to ", Obj)

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
#       ---------------------- Directory Watcher ----------------------
#       Directory is exits.....!
#       Time required to execute the script is :  -0.008968830108642578
#       --------------- Thank you for using our script ----------------
#######################################################################################################
