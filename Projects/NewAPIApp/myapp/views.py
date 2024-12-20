from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serail=studSerail(stdata,many=True)
    return Response(serail.data)


@api_view(['GET'])
def getstid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serail=studSerail(stid)
    return Response(serail.data,status=status.HTTP_200_OK)
      

@api_view(['DELETE','GET'])
def deletestid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serail=studSerail(stid)
        return Response(serail.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


