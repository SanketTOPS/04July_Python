"""stdata={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    k=input("Enter your Key's:")
    v=input("Enter your Value's:")

    stdata[k]=v

print(stdata)"""

#-------------------------------#

stdata={}
k=['id','name','sub']

for i in range(len(k)):
    v=input("Enter value's:")
    stdata[k[i]]=v

print(stdata)


