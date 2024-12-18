#################################################################################
#   Problem Statement :  Accept n number of user and store in list
#   return addition of list
#################################################################################


#################################################################################
#   Function Name   :   Addition
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Return addition of list
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Addition(Brr):

    Sum = 0

    for i in Brr:
        Sum = Sum + i

    return Sum

#################################################################################
#   Entery Point Function
#################################################################################


def main():

    Arr = list()

    print("Number of element :", end="")
    Value = int(input())

    print("Enter the element :")

    for i in range(Value):
        Num = int(input())
        Arr.append(Num)

    Result = Addition(Arr)

    print("Addition of element :", Result)

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Number of element : 6
#       Enter the element :
#       13
#       5
#       45
#       7
#       4
#       56
#       Addition of element :  130
#################################################################################
