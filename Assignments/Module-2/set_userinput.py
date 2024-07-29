"""data=set()

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter a value:")
    data.add(x)


print(data)"""



data=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter a value:")
    data.append(x)


print(tuple(data))


