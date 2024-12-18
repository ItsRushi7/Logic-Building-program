#################################################################################
#   Problem Statement :  Check wether number is positive or negative
#################################################################################


#################################################################################
#   Function Name   :   ChKPosNeg
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Number is negative or positive
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def ChKPosNeg(No):

    if (No < 0):
        print("The number is negative")

    elif ( No == 0):
        print("Zero")

    else:
        print("The number is positive")

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number :",end="")
    Value = int(input())

    ChKPosNeg(Value)

    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the number :11
#       The number is positive
#       Enter the number :-8
#       The number is negative
#       Enter the number :0
#       Zero
#################################################################################
 