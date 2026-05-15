n = int(input("num: "))
def check(n):
    if n==0:
        return "its zero"
    elif n>0:
        return "its positve"
    else:
        return "its negetive"
print(check(n))