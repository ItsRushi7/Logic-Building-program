#################################################################################
#   Problem Statement :  Design python application which creates two threads
#   as evenfactor and oddfactor. Both the thread accept one parameter integer.
#   Evenfactor thread will display addition of even factors of given number 
#   and oddfactor will display addition of odd factors of given number. 
#   After execution of both the thread gets completed main thread should 
#   display message as "exit from main",
#################################################################################
import threading

#################################################################################
#   Function Name   :   CheckEven
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Even number and addition of number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckEven(No):

    Even = 2
    Sum = 0
    
    for i in range(No):
        print(Even, end=" ")
        Sum = Sum + Even
        Even = Even + 2
        
    print("Addition of EvenFactors :",Sum)
    
#################################################################################
#   Function Name   :   CheckOdd
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Odd number  and addition of number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckOdd(No):

    Odd = 1
    Sum = 0 
    for i in range(No):
        print(Odd, end=" ")
        Sum = Sum + Odd
        Odd = Odd + 2
        
    print("Addition of OddFactors :",Sum)

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
    
    print(".....Exit from main.....")
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number :5
#       2 4 6 8 10 Addition of EvenFactors : 30
#       1 3 5 7 9 Addition of OddFactors : 25
#       .....Exit from main.....
#################################################################################
