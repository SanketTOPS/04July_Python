class studinfo:
    stid=23
    stnm="Ashok"

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object
"""st=studinfo()
st.printdata()
st.stid=40
st.stnm="Hitesh"
st.printdata()"""


#Instance
studinfo().printdata()
studinfo().stid=45
studinfo().stnm="Sanket"
studinfo().printdata()
