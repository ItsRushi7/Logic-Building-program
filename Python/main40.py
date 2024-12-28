#################################################################################
#   Problem Statement : Design python application which creates two thread named 
#   as even and odd. Even thread will display first 10 even numbers and odd 
#   thread  will display first 10 odd numbers.
#################################################################################
import threading

#################################################################################
#   Function Name   :   CheckEven
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Even number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckEven(No):

    Even = 2
    for i in range(No):
        print(Even, end=" ")
        Even = Even + 2
        
    print()


#################################################################################
#   Function Name   :   CheckOdd
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Odd number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckOdd(No):

    Odd = 1
    for i in range(No):
        print(Odd, end=" ")
        Odd = Odd + 2
        
    print()


#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number :", end="")
    Value = int(input())

    Thread1 = threading.Thread(target=CheckEven, args=(Value,))
    Thread2 = threading.Thread(target=CheckOdd, args=(Value,))

    Thread1.start()
    Thread2.start()
    
     
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number :10
#       2 4 6 8 10 12 14 16 18 20
#       1 3 5 7 9 11 13 15 17 19
#################################################################################
