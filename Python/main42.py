#################################################################################
#   Problem Statement :  Design python application which creates two threads
#   as evenlist and oddlist. Both the threads accept list of integers as
#   parameter. Evenlist thread add all even elements from input list and
#   display the addition. Oodlist thread add all odd elements from
#   input list and display the addition.
#################################################################################
import threading

#################################################################################
#   Function Name   :   CheckEvenList
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Even number form list and addition
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckEvenList(Arr):

    Sum = 0
    
    for i in Arr:
        if (i % 2 == 0):
             print(i, end=" ")
             Sum = Sum + i 
             
    print("Addition of even form list ",Sum)

#################################################################################
#   Function Name   :   CheckOddList
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check Odd number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckOddList(Arr):

    Sum = 0

    for i in Arr:
        if (i % 2 == 0):
            sum = 0
        else:
            print(i, end=" ")
            Sum = Sum + i 
            
    print("Addition of odd form list ",Sum)

#################################################################################
#   Entery Point Function
#################################################################################


def main():

    print("Enter the element :", end="")
    Value = int(input())

    Data = list()

    print("Element of number :")
    for i in range(Value):
        Num = int(input())
        Data.append(Num)

    Thread1 = threading.Thread(target=CheckEvenList, args=[Data,])
    Thread2 = threading.Thread(target=CheckOddList, args=[Data,])

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
#       Enter the element :10
#       Element of number :
#       1
#       2
#       3
#       4
#       5
#       6
#       7
#       8
#       9
#       10
#       2 4 6 8 10 Addition of even form list  30
#       1 3 5 7 9 Addition of odd form list  25
#       .....Exit from main.....
#################################################################################
