#################################################################################
#   Problem Statement :  Accept n number of user and store in list
#   return Maximum of list
#################################################################################


#################################################################################
#   Function Name   :   Maximum
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Return Maximum of list
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Maximum(Brr):

    Max = Brr[0]

    for i in Brr:
        if (Max < i):
            Max = i

    return Max

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

    Result = Maximum(Arr)

    print("maximum number of element :", Result)

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
#       maximum number of element :  56
#################################################################################
