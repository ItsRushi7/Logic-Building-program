#################################################################################
#   Problem Statement : Write a program which contains one class named as
#   BookStore
#################################################################################


#################################################################################
#   Class Name      :   BookStore
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   -
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
class BookStore:

    NoOfBook = 1

    def __init__(self, string1, string2):
        self.Name = string1
        self.Author = string2

    @staticmethod
    def Increase():
        BookStore.NoOfBook = BookStore.NoOfBook + 1
        
    def Display(self):
        print("Name of book :", self.Name)
        print("Name of author :", self.Author)
        print("Number of book :", BookStore.NoOfBook)
          
#################################################################################
#   Entery Point Function
#################################################################################
def main():

    Obj1 = BookStore("Linux system programing", "Robert love")
    Obj1.Display()
    BookStore.Increase()

    Obj2 = BookStore("C programing by ", "Dennis Ritchie")
    Obj2.Display()
    BookStore.Increase()

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Name of book : Linux system programing
#       Name of author : Robert love
#       Number of book : 1
#       Name of book : C programing by
#       Name of author : Dennis Ritchie
#       Number of book : 2
#################################################################################
