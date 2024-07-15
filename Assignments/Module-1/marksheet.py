s1=int(input("Enter subject1 mark:"))
s2=int(input("Enter subject2 mark:"))
s3=int(input("Enter subject3 mark:"))
s4=int(input("Enter subject4 mark:"))

total=s1+s2+s3+s4
print("Total:",total)


pr=total/4
print("PR:",pr)

if pr>=70:
    print("Result:A+")
elif pr>=60:
    print("Result:A")
elif pr>=50:
    print("Result:B")
elif pr>=40:
    print("Result:C")
else:
    print("Result:FAIL")


