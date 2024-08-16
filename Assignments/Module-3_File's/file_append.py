x=open('test.txt','a')

id=input("Enter your ID:")
nm=input("Enter your Name:")
ct=input("Enter your City:")


x.write(f"\nID={id}\nName={nm}\nCity={ct}\n")