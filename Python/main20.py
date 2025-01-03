#################################################################################
#   Problem Statement :  Display below pattern
#################################################################################


#################################################################################
#   Function Name   :   Display
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display pattern
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Display(No):
    
    for i in range(1 ,No+1):
        for j in range(1 ,No+1):
            print(j ,end=" ")
        print()

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number : ",end="")
    Value = int (input())
    
    Display(Value)
    
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the number : 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#################################################################################