#################################################################################
#   Problem Statement :  write a program which accept file name from user and
#   create new file Demo.txt and copy all the contents from existing file frome
#   new file accept file name through command line argument
#################################################################################
import os
import sys

#################################################################################
#   Function Name   :   CreateCopyFile
#   Input           :   String
#   Output          :   String
#   Description     :   Open file and display in console
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################

def CreateCopyFile(String):

    if os.path.exists(String):
        print("Unable to create file as file is already existing")

    else:
        Cobj = open(String, "x")
        print("File gets succesfully created")
        
        print("Enter the data to write in file : ",end="")
        Wdata = input()
        
        Cobj.write(Wdata)

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

    FileName = sys.argv[1]

    CreateCopyFile(FileName)
    OpenFile(FileName)
    
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#
#################################################################################
