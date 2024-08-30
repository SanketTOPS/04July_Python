class studinfo:
    stid=12
    stnm="Nirav"

    def myfunc(self):
        print("This is class!")


#Object
st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()

