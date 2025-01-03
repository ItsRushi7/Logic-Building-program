#################################################################################
#   Problem Statement :   Addition of Digit
#################################################################################


#################################################################################
#   Function Name   :   AddDigit
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display length of string
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def AddDigit(No):

    Sum = 0

    for i in str(No):
        Sum = Sum + int(i)

    return Sum


#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the Digit : ", end="")
    Value = str(input())

    Result = AddDigit(Value)

    print("Addition of digit : ", Result)

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the Digit : 5187934
#       Addition of digit :  37
#################################################################################
