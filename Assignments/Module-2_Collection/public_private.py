class studinfo:
    #private
    __stid=12
    __stnm="Sanket"

    def getdata(self): #public method
        print("This is getdata!")
    
    def __printdata(self): #private method
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def result(self): #public
        self.__printdata()

st=studinfo()
#print("ID:",st.stid)
#print("Name:",st.stnm)

st.getdata()
#st.printdata()
st.result()