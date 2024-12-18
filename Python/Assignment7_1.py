#################################################################################
#   Problem Statement :  Write a program which contains one class named as Demo 
################################################################################

#################################################################################
#   Class Name      :   Demo
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class Demo:

    Num = 11

    def __init__(self, No1, No2):
        self.Value1 = No1
        self.Value2 = No2

    def Fun(self):
        print("The value of instance variable :", self.Value1)
        print("The value of instance variable :", self.Value2)

    def Gun(self):
        print("The value of instance variable :", self.Value1)
        print("The value of instance variable :", self.Value2)

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()
    
    return 0

#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       The value of instance variable : 11
#       The value of instance variable : 21
#       The value of instance variable : 51
#       The value of instance variable : 101
#       The value of instance variable : 11
#       The value of instance variable : 21
#       The value of instance variable : 51
#       The value of instance variable : 101
#################################################################################
