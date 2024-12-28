#################################################################################
#   Problem Statement :  Accept n number of user and store in list n accepte
#   another number from user return Freqeuncy that number
#################################################################################


#################################################################################
#   Function Name   :   Frequency
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Frequency that number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Frequency(Brr, No):

    Number = 0

    for i in Brr:

        if (i == No):
            Number = Number + 1

    return Number


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

    print("Element that search : ", end="")
    value2 = int(input())

    Result = Frequency(Arr, value2)

    print("Frequency of that List : ", Result)

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
#       4
#       56
#       5
#       34
#       2
#       5
#       65
#       Element that search : 5
#       Frequency of that List :  3
#################################################################################
