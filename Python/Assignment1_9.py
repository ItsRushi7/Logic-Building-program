#################################################################################
#   Problem Statement :  Display first 10 even number
#################################################################################


#################################################################################
#   Function Name   :   Even
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display first 10 even number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def Even(No):

    for i in range(2, (No+1), 2):
        print(i,end="\t")

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number :",end="")
    Value = int(input())

    Even(Value)

    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################   
#   Output :
#       Enter the number :20
#       2       4       6       8       10      12      14      16      18      20
#################################################################################
    