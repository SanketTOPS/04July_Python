class student:
    @staticmethod
    def myfunc():
        print("This is class!")
    
    @staticmethod
    def getsum(a,b):
        print("Sum:",a+b)

st=student()
st.myfunc()
st.getsum(12,23)