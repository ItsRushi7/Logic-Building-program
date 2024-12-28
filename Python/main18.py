#################################################################################
#   Problem Statement :  Check prime number
#################################################################################


#################################################################################
#   Function Name   :   CheckPrime
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check prime
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckPrime(No):

    Flag = True

    for i in range(2, No):
        if ((No % i) == 0):
            Flag = False

    if (Flag == True):

        return True

    else:

        return False

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number : ", end="")
    Value = int(input())

    Result = CheckPrime(Value)

    if (Result == True):
        print("This is prime number !")

    else:
        print("This is not prime number !")

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number : 5
#       This is prime number !
#################################################################################
