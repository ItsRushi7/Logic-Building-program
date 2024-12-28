#######################################################################################################
#   Problem Statement :  Design automation script which accept directory name and two file
#   extensions from user Rename all files with first file extension with the second file extenntion
#######################################################################################################
import sys
import os
import time

#######################################################################################################
#   Function Name   :   DirectoryWatcher
#   Input           :   Connamd Line Argument
#   Output          :
#   Description     :   Rename all files with first file extension with the second file extenntion.
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#######################################################################################################
def DirectoryWatcher(DirName, Extension1, Extension2):

    Flag = os.path.isabs(DirName)

    if (Flag == False):
        
        DirName = os.path.abspath(DirName)
        
    Exist = os.path.isdir(DirName) 
    
    if (Exist == True):
        
        print("Directory is exits.....!") 
        
        for FolderName, SubFolderName, FileName in os.walk(DirName):
            for Name in FileName: 
                if Name.lower().endswith(Extension1):
                    Rename = os.path.splitext(Name)[0]
                    os.rename(os.path.join(FolderName,Name), os.path.join(FolderName,Rename+Extension2))        
                
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

    if (len(sys.argv) == 4):

        try:
            Starttime = time.time()
            DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])
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
#       D:\Marvellous  Python Machine Learning & Automation\Marvellous Assignment\Solve>
#       python Assignment10_2.py Code .txt .c
#       ---------------------- Directory Watcher ----------------------
#       Directory is exits.....!
#       Time required to execute the script is :  -0.0020008087158203125
#       --------------- Thank you for using our script ----------------
#######################################################################################################
