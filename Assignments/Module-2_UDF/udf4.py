def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)


n=int(input("Enter number of students:"))

for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter a name:")
    stcity=input("Enter a city:")

    getdata(stid,stnm,stcity)