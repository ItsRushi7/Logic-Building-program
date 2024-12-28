#################################################################################
#   Problem Statement : Write a program which contains Riter(), map() and
# reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter
# out all such numbers which are even. Map function will calculate
# Reduce will return addition of all that numbers.
#################################################################################
from functools import reduce

#################################################################################
#   Function Name   :   CheckEven
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check the even number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckEven(Arr):
    return (Arr % 2 == 0)

#################################################################################
#   Function Name   :   Square
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Calulate the square
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Square(Arr):
    return (Arr * Arr)

#################################################################################
#   Function Name   :   Addition
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Product that number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Addition(A, B):
    return (A + B)

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number of element :", end="")
    Value = int(input())

    Data = []

    print("Enter the elements :")
    for i in range(Value):
        Num = int(input())
        Data.append(Num)

    FData = list(filter(CheckEven, Data))
    print("List after filter : ", FData)

    MData = list(map(Square, FData))
    print("List after map : ", MData)

    RData = reduce(Addition, MData)
    print("List after reduce : ", RData)

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       List after filter :  [2, 4, 4, 2, 8, 10]
#       List after map :  [4, 16, 16, 4, 64, 100]
#       List after reduce :  26214400
#################################################################################
