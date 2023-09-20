'''
    Function Based View
'''
from django.shortcuts import render

from users.models import Users
from users.serializers import User_Serializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

@api_view(['GET', 'POST'])
def Users_List(request) :
    '''
        API to perform GET & POST operations on users withour primary key

    '''
    if request.method == 'GET' :
        users = Users.objects.all()
        serializer = User_Serializer(users , many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = User_Serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

'''
    API to perform GET & POST operations on users with primary key

'''

@api_view(['GET', 'PUT', 'DELETE'])
def Users_Detail(request,pk):
    
    try:
        users = Users.objects.get(pk = pk)
    except Users.DoesNotExist :
        raise Http404
    
    if request.method == 'GET':

        serializer = User_Serializer(users)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = User_Serializer(users,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    