def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n - 1)  #recursion
n = int(input("Enter a number to find its factorial: "))
print(factorial(n))