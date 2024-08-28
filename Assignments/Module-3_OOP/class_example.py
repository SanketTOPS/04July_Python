class studinfo:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is studinfo class!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


#Object of class
st=studinfo() #class object
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.getsum(12,34)

