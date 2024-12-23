from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url="https://restcountries.com/v3.1/all"
    req=requests.get(url)
    data=req.json()
    #print(data)

    """for i in data:
        print("Name:",i["name"]["official"])
        print("Region:",i["region"])
        print("Flag:",i["flags"]["png"])
        print("Maps:",i["maps"]["googleMaps"])"""
    return render(request,'index.html',{'data':data})