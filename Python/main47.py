#################################################################################
#   Problem Statement : Write a program which contains one class named as Circle 
#################################################################################


#################################################################################
#   Class Name      :   Circle
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class Circle:

    PI = 3.14

    def __init__(self, No1, No2, No3):
        self.Radius = No1
        self.Area = No2
        self.Circumference = No3

    def Accept(self):
        print("Entar the value of readius : ", end="")
        self.Radius = int(input())

    def CalculateArea(self,):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        Ans = 2 * Circle.PI * self.Radius * self.Radius
        self.Circumference = Ans

    def Display(self):
        print("Radius of circle is ", self.Radius)
        print("Area of circle is ", self.Area)
        print("Circumference of circle is ", self.Circumference)


#################################################################################
#   Entery Point Function
#################################################################################
def main():

    Num1 = 0
    Num2 = 0.0
    Num3 = 0.0

    Obj = Circle(Num1, Num2, Num3)

    Obj.Accept()
    Obj.CalculateArea()
    Obj.CalculateCircumference()
    Obj.Display()

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
