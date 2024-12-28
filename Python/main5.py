#################################################################################
#   Problem Statement :  Addition of two number 
#################################################################################


#################################################################################
#   Function Name   :   Add
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Addition of two number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/04/2024
#################################################################################
def Add(No1, No2):

    Ans = 0
    Ans = No1 + No2
    return Ans

#################################################################################
#   Entery Point Function
#################################################################################
def main():
    
    print("Enter the first number :",end="")
    Value1 = int(input())

    print("Enter the second number :",end="")
    Value2 = int(input())

    Result = Add(Value1, Value2)

    print("Addion of two number :",Result)

    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the first number :11
#       Enter the second number :5
#       Addion of two number : 16
#################################################################################
 