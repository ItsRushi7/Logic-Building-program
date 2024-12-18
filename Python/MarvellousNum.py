#################################################################################
#   Function Name   :   CheckPrime
#   Input           :   Integer
#   Output          :   Integer
#   Description     :   Check the prime number
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   11/05/2024
#################################################################################
def CheckPrime(Arr):

    Brr = list()

    for i in Arr:
        Cnt = 0
        for j in range(2, i):
            if (i % j == 0):
                Cnt = 1
        if Cnt == 0:
            Brr.append(i)

    print("prime number is : ",Brr)

    return Brr
