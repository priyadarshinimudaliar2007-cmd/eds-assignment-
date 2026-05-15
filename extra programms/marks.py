# 40 - fail 
# 40 - 60 - second class
# 61 - 80 - first class
# greater than 80 - distinction

marks = int(input("enter your marks: "))

if marks < 40:
    print("fail")
elif (marks >= 40) and (marks <=60):
    print("second class")
elif (marks > 60) and (marks <=80):
    print("first class")
else:
    print("distinction")