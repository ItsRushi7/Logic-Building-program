#################################################################################
#   Problem Statement :  Display * on screen
#################################################################################


#################################################################################
#   Function Name   :   Display
#   Input           :   Integer
#   Output          :   String
#   Description     :   Display * on screen
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Display(No):

    for i in range(No):
        print("*",end="\t")

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number :",end="")
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
#       Enter the number :5
#       *       *       *       *       *
#################################################################################
    