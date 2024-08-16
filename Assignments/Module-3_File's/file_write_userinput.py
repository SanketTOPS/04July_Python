x=open('test.txt','w')

id=input("Enter your ID:")
nm=input("Enter your Name:")
ct=input("Enter your City:")

"""x.write(id)
x.write(nm)
x.write(ct)"""

x.write(f"ID={id}\nName={nm}\nCity={ct}")