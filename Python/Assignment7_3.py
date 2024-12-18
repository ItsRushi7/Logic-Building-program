#################################################################################
#   Problem Statement : Write a program which contains one class named as
#   Arithematic
#################################################################################


#################################################################################
#   Class Name      :   Arithematic
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class Arithematic:

    def __init__(self):
        self.No1 = 0
        self.No2 = 0

    def Accept(self):
        print("Enter first numbner")
        self.No1 = int(input())

        print("Enter second numbner")
        self.No2 = int(input())

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):
        Ans = self.No1 * self.No2
        return Ans

    def Division(self):
        Ans = self.No1 % self.No2
        return Ans

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    Obj1 = Arithematic()
    Obj2 = Arithematic()
    Obj3 = Arithematic()
    Obj4 = Arithematic()

    Obj1.Accept()
    Result = Obj1.Addition()
    print("Addition is : ", Result)
    
    Obj2.Accept()
    Result = Obj2.Substraction()
    print("Addition is : ", Result)
    
    Obj3.Accept()
    Result = Obj3.Multiplication()
    print("Addition is : ", Result)
    
    Obj4.Accept()
    Result = Obj4.Division()
    print("Addition is : ", Result)
    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Entar the value of readius : 5
#       Radius of circle is  5
#       Area of circle is  78.5
#       Circumference of circle is  157.0
#################################################################################
