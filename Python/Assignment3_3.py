#################################################################################
#   Problem Statement :  Accept n number of user and store in list
#   return Minimum of list
#################################################################################


#################################################################################
#   Function Name   :   Minimum
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Return Maximum of list
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Minimum(Brr):

    Min = Brr[0]

    for i in Brr:
        if (Min > i):
            Min = i

    return Min

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

    Result = Minimum(Arr)

    print("Minimum number of element :", Result)

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
#       Minimum number of element : 5
#################################################################################
