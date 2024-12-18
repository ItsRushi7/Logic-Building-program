#################################################################################
#   Problem Statement :  write a program which accept file name from user and
#   open that file and display that content file on screen
#################################################################################
import os

#################################################################################
#   Function Name   :   OpenFile
#   Input           :   String
#   Output          :   String
#   Description     :   Open file and display in console
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def OpenFile(String):

    if os.path.exists(String):
        
        fObj = open(String, "r")
        print("File is succesfully open...!")
        
        Data = fObj.read()

        print(Data)
        
        fObj.close()
        
    else:
        print("That file is not exit in diectory...!")


#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the file name :", end="")
    FileName = input()

    OpenFile(FileName)

    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the file name :Demo.txt
#       File is succesfully open...!
#       Hello from Demo......!
#################################################################################
