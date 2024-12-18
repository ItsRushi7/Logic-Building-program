#################################################################################
#   Problem Statement :  Write a program which contains one class named as
#   Number
#################################################################################


#################################################################################
#   Class Name      :   Number
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class Number:

    def __init__(self,No):
        self.Value = No

    def CheckPrime(self):

        Flag = True

        for i in range(2, self.Value):
            if ((self.Value % i) == 0):
                Flag = False

        if (Flag == True):
            print("This is prime number !")

        else:
            print("This is not prime number !")

    def Factors(self):

        Fact = 1

        for i in range(1, self.Value+1):
            Fact = Fact * i

        print("Factorial is :", Fact)

    def CheckPrefect(self):

        Sum = 0

        for i in range(1, self.Value+1):
            if ((self.Value % i) == 0):
                Sum = Sum + i

        if (Sum == self.Value):
            print("This is prfect number !")

        else:
            print("This is not prfect number !")


#################################################################################
#   Entery Point Function
#################################################################################

def main():

    print("Enter the value :",end="")
    Value = int(input())

    Obj1 = Number(Value)
    
    Obj1.CheckPrime()
    Obj1.CheckPrefect()
    Obj1.Factors()
    
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the value :11
#       This is prime number !
#       This is not prfect number !
#       Factorial is : 39916800
#################################################################################
