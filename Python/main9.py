#################################################################################
#   Problem Statement :  Check wether number is Divisible by 5
#################################################################################


#################################################################################
#   Function Name   :   Divsible
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Number is divisible by 5 or not
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Divsible(No):

    if ((No % 5) == 0):
        return True

    else:
        False

#################################################################################
#   Entery Point Function
#################################################################################


def main():

    print("Enter the number :", end="")
    Value = int(input())

    Result = Divsible(Value)

    if (Result == True):
        print("True")

    else:
        print("False")

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number :8
#       False
#       Enter the number :25
#       True
#################################################################################
