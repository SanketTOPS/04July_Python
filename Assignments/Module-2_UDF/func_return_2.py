"""def getsum(a,b):
    return a+b

x=getsum(34,67)
print(x)
"""


def getdata(id,name):
    return id,name

def studinfo():
    x=getdata(101,'Sanket')
    print("ID:",x[0])
    print("Name:",x[1])

studinfo()