#################################################################################
#   Problem Statement :  Addition of Factorial
#################################################################################


#################################################################################
#   Function Name   :   Factorial
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Addition of Factorial
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Factorial(No):
    
    Sum = 0
    
    for i in range(1, No):
        
        if (No % i == 0):
            Sum = Sum + i
        
    return Sum

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number : ",end="")
    Value = int(input())
    
    Result = Factorial(Value)
    
    print("Addition of Factorial ",Value, ": ",Result)
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the number : 5
#       Factorial of  5 :  120
#################################################################################