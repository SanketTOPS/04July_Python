class master:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class home(master):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)

class about(master):
    def getdata(self, id, name):
        return super().getdata(id, name)


hm=home()
ab=about()

hm.getdata(101,'Sanket')
ab.getdata(102,'Nirav')
