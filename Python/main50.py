#################################################################################
#   Problem Statement : Write a program which contains one class named as
#   BankAccount
#################################################################################


#################################################################################
#   Class Name      :   BankAccount
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class BankAccount:

    ROI = 10.5

    def __init__(self, String1):
        self.Name = String1
        self.Amount = 0

    def Deposit(self):
        print("How much amount you want to Deposit :", end="")
        self.Amount = int(input())
        print("Your Deposit amount is :",self.Amount)
        print("---------------------------------------------------------------")

    def withdraw(self):
        print("How much amount you want to withdraw :", end="")
        WithDraw = int(input())

        if (WithDraw > self.Amount):
            print("Your amount is grater than Deposit.....!")

        else:
            self.Amount = self.Amount - WithDraw
            print("After withdraw your amount is :", self.Amount)
            print("---------------------------------------------------------------")

    def CalculateIntrest(self):
        Year = int(input("Enter the year :"))
        SimpleIntrest = (self.Amount * BankAccount.ROI * Year / 100)
        print("Simple intrest is : ", SimpleIntrest)
        
    def Display(self):
        print("Your name is :",self.Name)
        print("Your amount is :",self.Amount)
        print("Rate of intrest is :",BankAccount.ROI)

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    Name = input("Enter your name :")
    print("---------------------------------------------------------------")
    Obj = BankAccount(Name)
    
    Obj.Display()
    Obj.Deposit()
    Obj.withdraw()
    Obj.CalculateIntrest()
    
    print("-------------------------- thnak you --------------------------")
    
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter your name :Rushikesh
#       ---------------------------------------------------------------
#       Your name is : Rushikesh
#       Your amount is : 0
#       Rate of intrest is : 10.5
#       How much amount you want to Deposit :8000
#       Your Deposit amount is : 8000
#       ---------------------------------------------------------------
#       How much amount you want to withdraw :4000
#       After withdraw your amount is : 4000
#       ---------------------------------------------------------------
#       Enter the year :5
#       Simple intrest is :  2100.0
#       -------------------------- thnak you --------------------------
#################################################################################
