import re

mystr="That is Python!"

#x=re.search('Python',mystr)
x=re.search('This',mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")