import re

mystr="This is Python!8484896"


#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
x=re.findall('\S',mystr)
print(x)