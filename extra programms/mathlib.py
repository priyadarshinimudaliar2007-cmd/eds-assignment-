import math
n = int(input("enter a number: "))

if (n>=0) and (n<=9):
    print(pow(n , 2))
elif (n>=10) and (n<=99):
    print(math.sqrt(round(n,2)))
elif (n>=100) and (n<999):
    print(math.cbrt(round(n,2)))