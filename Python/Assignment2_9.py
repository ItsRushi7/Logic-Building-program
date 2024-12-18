#################################################################################
#   Problem Statement :  Display length of Digit
#################################################################################


#################################################################################
#   Function Name   :   Display
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display length of string
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Display(Digit):

    length = len(Digit)

    print("length of Digit is ", length)

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the Digit : ",end="")
    Value = int(input())

    Display(Value)

    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#        Enter the Digit : 5187934
#        length of Digit is  7
#################################################################################
 