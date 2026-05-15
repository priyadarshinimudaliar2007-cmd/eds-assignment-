#fn to convert far to celc
n = int(input("enter temprature: "))
def far_to_cel(temp):
    return round((temp-32)*5/9,2)
print(far_to_cel(n))