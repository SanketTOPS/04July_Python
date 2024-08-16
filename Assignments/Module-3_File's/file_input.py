x=open('stdata.txt','a')

n=int(input("Enter nummber of students:"))

for i in range(n):
    id=input("Enter an ID:")
    nm=input("Enter your Name:")
    ct=input("Enter your City:")

    x.write(f"ID:{id}\nName:{nm}\nCity:{ct}\n")