#################################################################################
#   Problem Statement :  Create lamda function and return Muiltiplication of 
#   number 
#################################################################################


#################################################################################
#   Function Name   :   Muiltiplication
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Muiltiplication of two number 
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Muiltiplication(Num1, Num2):
    
    return  lambda No1 , No2 : No1 * No2

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the first number : ",end="")
    Value1 = int(input())
    
    print("Enter the second number : ",end="")
    Value2 = int(input())
    
    Result = Muiltiplication(Value1,Value2)
    
    print("Power of number : ",Result(Value1,Value2))
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#        Enter the first number : 4
#        Enter the second number : 3
#        Power of number :  12
#################################################################################