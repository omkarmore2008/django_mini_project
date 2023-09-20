'''
        Class Based View 
'''
# asdasd
from django.shortcuts import render
from django.http import Http404
# model
from products.models import Products
from products.serializers import Product_Serializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics, mixins
'''
    Class to perform GET & POST operations on Products

class ProductsList(APIView):

    def get(self, request) :
        products = Products.objects.all()
        serializer = Product_Serializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Product_Serializer(data= request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        #else: 

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ProductsDetail(APIView) :

    def get_object(self, pk) :
        try:
            return Products.objects.get(pk = pk)
        
        except Products.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        products = self.get_object(pk)
        serializer = Product_Serializer(products)
        return Response(serializer.data)

    def put(self, request, pk) :
        products = self.get_object(pk)
        serializer = Product_Serializer(products, data= request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response (serializer.data)
        
        #else

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) :
        products = self.get_object(pk)
        products.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

'''
#################
'''
Generics And Mixins


class ProductsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = Product_Serializer

    def get(self, request) :
        return self.list(request)
    
    def post(self, request) :
        return self.create(request)

class ProductsDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView) :
    queryset = Products.objects.all()
    serializer_class = Product_Serializer

    def get(self, request, pk) :
        return self.retrieve(request,pk)

    def put(self, request, pk) :
        return self.update(request, pk)
    
    def delete(self, request, pk) :
        return self.destroy(request, pk)

'''
#################
'''
Generics

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = Product_Serializer

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Products.objects.all()
    serializer_class = Product_Serializer

    
'''
#################
'''
    Using View Set
'''
class ProductsViewSet(viewsets.ModelViewSet) :
    queryset = Products.objects.all()
    serializer_class = Product_Serializer
