#################################################################################
#   Problem Statement :  Accept n number of user and store in list n Check the
#   prime number Addition of that number
#################################################################################
import MarvellousNum

#################################################################################
#   Function Name   :   Addition
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Addition of that prime number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Addition(Brr):

    Prime = MarvellousNum.CheckPrime(Brr)

    Sum = 0

    for i in Prime:

        Sum = Sum + i

    return Sum


#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Number of elements : ", end="")
    Value1 = int(input())

    Arr = list()
    print("Enter the elements ")

    for i in range(Value1):
        Num = int(input())
        Arr.append(Num)

    Result = Addition(Arr)

    print("Addition of that prime number : ", Result)

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Number of elements : 11
#       Enter the elements
#       13
#       5
#       45
#       7
#       56
#       10
#       34
#       2
#       5
#       8
#       3
#       prime number is :  [13, 5, 7, 2, 5, 3]
#       Addition of that prime number :  35
#################################################################################
