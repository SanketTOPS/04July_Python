a=23
print("A=",a)

def getvalue():
    global a
    a+=1
    print("A=",a)

getvalue()
