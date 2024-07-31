stdata={'id':101,'name':'Sanket','city':'Rajkot'}
"""print(stdata)
print(stdata.get('name'))
print(stdata['city'])"""

"""print(len(stdata))
print(stdata.keys())
print(stdata.values())"""


"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'Sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""


"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

#-----------------------------------------------#
print(stdata)
#stdata['id']=102 #Value Update
#stdata['sub']='Python'
#stdata.pop('city')
#del stdata['sub']
#del stdata
#stdata.clear()
#print(stdata)

newdata=stdata.copy()
print(newdata)