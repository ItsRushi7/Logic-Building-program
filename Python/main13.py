#################################################################################
#   Problem Statement :  Calling function from arithmetic module
#################################################################################
import Arithmetic

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the first number : ",end="")
    Value1 = int(input())
    
    print("Enter the first number : ",end="")
    Value2 = int(input())
    
    Result = Arithmetic.Add(Value1,Value2)
    print("Addition of two number : ",Result)
    
    Result = Arithmetic.Sub(Value1,Value2)
    print("Addition of two number : ",Result)
    
    Result = Arithmetic.Muilt(Value1,Value2)
    print("Addition of two number : ",Result)
    
    Result = Arithmetic.Div(Value1,Value2)
    print("Addition of two number : ",Result)
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the first number : 10
#       Enter the first number : 20
#       Addition of two number :  30
#       Addition of two number :  -10
#       Addition of two number :  200
#       Addition of two number :  0.5
#################################################################################
 