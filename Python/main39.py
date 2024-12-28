#################################################################################
#   Problem Statement :  Recursive program to return its factorial
#################################################################################

Cnt = 1
Fact = 1
#################################################################################
#   Function Name   :   Factorial
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Factorial of its number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Factorial(No):

    global Cnt
    global Fact

    if (Cnt <= No):
        Fact = Fact * Cnt
        Cnt = Cnt + 1
        Factorial(No)

    return Fact

#################################################################################
#   Entery Point Function
#################################################################################


def main():

    print("Enter the number :", end="")
    Value = int(input())

    Result = Factorial(Value)

    print("Factorial of number is :", Result)
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number :5
#       Factorial of number is : 120
#################################################################################
