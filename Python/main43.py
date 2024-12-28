#################################################################################
#   Problem Statement :  Design python application which creates three threads
#   as small, capital, digits. All the threads accepts string as parameter.
#   Small thread display number of small characters, capital thread display
#   number of capital characters and digits thread display number of
#################################################################################
import threading
import os

#################################################################################
#   Function Name   :   Small
#   Input           :   String
#   Output          :   String
#   Description     :   Check small letter in String
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Small(String):

    Count = 0
    
    for i in String:
        if(i >= 'a' and i <= 'z'):
            Count = Count + 1

    print("Small latter in string :",Count)
    
    print("PID of small process ",os.getpid())
    print("TID of small thread ",threading.get_ident())
    

#################################################################################
#   Function Name   :   Capital
#   Input           :   String
#   Output          :   String
#   Description     :   Check capital letter in String
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Capital(String):

    Count = 0
    
    for i in String:
        if(i >= 'A' and i <= 'Z'):
            Count = Count + 1

    print("Capital latter in string :",Count)
    
    print("PID of Capital process ",os.getpid())
    print("TID of Capital thread ",threading.get_ident())
 
#################################################################################
#   Function Name   :   Digit
#   Input           :   String
#   Output          :   String
#   Description     :   Check Digit in String
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Digit(String):

    Count = 0
    
    for i in String:
        if(i >= '0' and i <= '9'):
            Count = Count + 1

    print("Small latter in string :",Count)
    
    print("PID of Digit process ",os.getpid())
    print("TID of Digit thread ",threading.get_ident())
   
#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the string :", end="")
    String = input()

    Thread1 = threading.Thread(target=Small, args=(String,))
    Thread2 = threading.Thread(target=Capital, args=(String,))
    Thread3 = threading.Thread(target=Digit, args=(String,))

    Thread1.start()
    Thread2.start()
    Thread3.start()
    
    
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the string :RushikeshHESJJ5556
#       Small latter in string : 8
#       PID of small process  20428
#       TID of small thread  15088
#       Capital latter in string : 6
#       Small latter in string : 4
#################################################################################
