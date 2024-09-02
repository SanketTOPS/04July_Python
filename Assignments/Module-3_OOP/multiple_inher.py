class ashok:
    aid=0
    atech=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Tech.:")

class mitesh:
    mid=0
    mtech=""

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.mtech=input("Enter Mitesh's Tech.:")

class nirav:
    nid=0
    ntech=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.ntech=input("Enter Nirav's Tech.:")


class tops(ashok,mitesh,nirav):
    def printdata(self):
        print("--------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Tech.:",self.atech)
        print("--------Mitesh's Data--------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Tech.:",self.mtech)
        print("--------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Tech.:",self.ntech)


tp=tops()
tp.a_getdata()
tp.m_getdata()
tp.n_getdata()
tp.printdata()