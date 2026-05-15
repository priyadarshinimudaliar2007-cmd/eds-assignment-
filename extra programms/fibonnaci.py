def fibonnaci(n):
    if n == 0: # checks if the input is 0, if it is then it will return 0
        return 0
    elif n == 1: # checks if the input is 1, if it is then it will return 1
        return 1
    else:
        temp = fibonnaci(n-1) + fibonnaci(n-2) # if the input is greater than 1, it will call the function recursively to calculate the Fibonacci number by summing the two preceding numbers in the sequence 
        return temp
n = int(input("Enter the position of the Fibonacci sequence: "))
for i in range(n):
    print(fibonnaci(i), end=' ') #see how its internally working