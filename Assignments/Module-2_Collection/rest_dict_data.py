import requests

"""url="https://restcountries.com/v3.1/all"

req=requests.get(url)

data=req.json()

#print(data)

for i in data:
    print(f"Country Name:{i["name"]["official"]}")
    print(f"Region Name:{i["region"]}")
    print(f"Flags:{i["flags"]["png"]}")
"""


# ----------------------------------------------- #

url="https://data.covid19india.org/data.json"

req=requests.get(url)

data=req.json()

#print(data)

for i in data["statewise"]:
    print(i["state"])







