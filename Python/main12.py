#######################################################################################################
#   Problem Statement : Design automation script which accept directory name
#   and flie extension from user. Display all files with that extension.
#######################################################################################################
import sys
import os
import time

#######################################################################################################
#   Function Name   :   DirectoryWatcher
#   Input           :   Connamd Line Argument
#   Output          :
#   Description     :   Display all files with that extension.
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#######################################################################################################
def DirectoryWatcher(DirName, Extension):
     
    Flag = os.path.isabs(DirName)

    if (Flag == False):
        
        DirName = os.path.abspath(DirName)
        
    Exist = os.path.isdir(DirName) 
    
    if (Exist == True):
        
        print("Directory is exits.....!") 
        
        for FolderName, SubFolderName, FileName in os.walk(DirName):
            for Name in FileName: 
                if Name.endswith(Extension):
                    print(Name)        
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

        if (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_File  Name_Of_Directory  File_extension")
            exit()

    if (len(sys.argv) == 3):
        try:
            Starttime = time.time()
            DirectoryWatcher(sys.argv[1], sys.argv[2])
            Endtime = time.time()

            print("Time required to execute the script is : ", Starttime-Endtime)

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
#       program1.c
#       program2.c
#       program3.c
#       program4.c
#       Time required to execute the script is :  0.0
#       --------------- Thank you for using our script ----------------
#######################################################################################################
