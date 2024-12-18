#################################################################################
#   Problem Statement :  write a program which accept file name from user and
#   check whether that file exit in current directory or not
#################################################################################
import os

#################################################################################
#   Function Name   :   CheckFile
#   Input           :   String
#   Output          :   String
#   Description     :   Check file in directory 
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckFile(String):
    
    if os.path.exists(String):
        print("That file is exit in diectory...!")
        
    else: 
        print("That file is not exit in diectory...!")
    

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the file name :",end="")
    FileName = input()
    
    CheckFile(FileName)
        
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the file name :Demo.py
#       That file is exit in diectory...!
#       Enter the file name :Hello.py
#       That file is not exit in diectory...!
#################################################################################