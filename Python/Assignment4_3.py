#################################################################################
#   Problem Statement :  Write a program which contains filter(), map() and
# reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from Filter should filter out
# all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by ID. Reducie will retum product
# of all that numbers
#################################################################################
from functools import reduce

#################################################################################
#   Function Name   :   MinMax
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check the number is greater than or Less than
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def MinMax(Arr):
    return ((Arr >= 70) and (Arr <= 90))

#################################################################################
#   Function Name   :   Increase
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Increase by 10
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Increase(Arr):
    return (Arr + 10)

#################################################################################
#   Function Name   :   Product
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Product that number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Product(A, B):
    return (A * B)

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

    FData = list(filter(MinMax, Data))
    print("List after filter : ", FData)
    
    MData = list(map(Increase, FData))
    print("List after map : ", MData)

    RData = reduce(Product, MData)
    print("List after reduce : ", RData)
    
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       List after filter :  [76, 89, 86, 90, 70]
#       List after map :  [86, 99, 96, 100, 80]
#       List after reduce :  6538752000
#################################################################################
