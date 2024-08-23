fl=open('stdata.txt','r')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[1])
#print(fl.readlines()[0:4])


"""for i in fl:
    print(i)"""


if fl.readable():
    print("Yes...")
else:
    print("Noo")