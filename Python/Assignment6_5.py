#################################################################################
#   Problem Statement :  Design python application which contains two threads
#   named as threads and thread2. Thread1 display 1 to 50 on screen and thread2
#   display 50 to 1 in reverse order on screen. After execution of threädi gets
#   completed then schedule thread2
#################################################################################
import threading

#################################################################################
#   Function Name   :   DisplayForward
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display 1 to 50
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def DisplayForword(No):

    for i in range(1, No+1):
        print(i, end=" ")
        
    print()


#################################################################################
#   Function Name   :   DisplayBackward
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Display 50 to 1
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def DisplayBackword(No):

    for i in range(No, 0, -1):
        print(i, end=" ")

    print()

#################################################################################
#   Entery Point Function
#################################################################################
def main():

    print("Enter the number :", end="")
    Value = int(input())

    Thread1 = threading.Thread(target=DisplayForword, args=(Value,))
    Thread2 = threading.Thread(target=DisplayBackword, args=(Value,))

    Thread1.start()
    Thread2.start()

    return 0


#################################################################################
#   Starter
#################################################################################
if __name__ == "__main__":
    main()

#################################################################################
#   Output :
#       Enter the number :50
#       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 
#       28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
#       50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 
#       26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
#################################################################################
