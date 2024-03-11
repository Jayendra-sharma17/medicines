from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.contrib import messages
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
# Create your views here.
from .serializers import *
from rest_framework.views import APIView
from .models import Medicine
from pymongo import MongoClient
from django.http import HttpResponse
from .db_conn import conn
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import os

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['Medicine_data']
collection = db['Medicine_collection']

#database for medicine and connectivity with mongodb 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class MedicineAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    
    def post(self,request):
        data=request.data
        serializer=MedicineSerializer(data=data)
        print(data)
        
       
        if not serializer.is_valid():
              
              print(serializer.errors)
              return Response({'status':403,'erorors':serializer.errors,'message':'something went wrong ❌ '})
        
        serializer.save()
            # print(data)
        # Medicine.objects.create(serializer.data)
        collection.insert_one(serializer.data)
        return Response({'status':200,'payload':serializer.data,'message':'your Medicine data is saved successfully 🎊'})
            

    def get(self, request, id=None):
        if id is not None:
            
            data=collection.find_one({"id":id})
            serializer=MedicineSerializer(data)
            return Response({'payload':serializer.data})
 
        else:    
            data = collection.find()
            serializer = MedicineSerializer(data, many=True)
            return Response({'status': 200, 'payload': serializer.data})
      


    def put(self,request,id):
        prev_data=collection.find_one({"id":id})
        
        print(prev_data)
        data=request.data
        serializer=MedicineSerializer(data=data)
        if not serializer.is_valid():

            return Response({"status":403,"message":serializer.errors})
        
        new_data={"$set":serializer.data}
        collection.update_one(prev_data,new_data)

        return Response({"data":serializer.data,'message':'your Medicine data is updated successfully 🎊'})
    

    def delete(self,request,id):
        query_set =collection.find_one({"uuid":id})
        serializer = MedicineSerializer(query_set)
        collection.delete_one({"uuid":id})
        return Response({"data" : serializer.data,'message':"data is deleted"})
    
# database for customer and connectivity with postgresql Customer_data
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
class CustomerAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data
        serializer=Customer_dataSerializer(data=data)
        if not serializer.is_valid():

              
            print(serializer.errors)
            return Response({'status':403,'erorors':serializer.errors,'message':'something went wrong'})
            
        serializer.save()
       
        return Response({'status':200,'payload':serializer.data,'message':'your data is saved successfully'})
    
    def put(self,request,id):
        
        data = request.data
        query_set = Customer_data.objects.get(id=id)
        serializer = Customer_dataSerializer(query_set , data = data)
        if not serializer.is_valid():
            return Response({"status" : 400 , "message" : serializer.errors})

        serializer.save()
        return Response({"data" : serializer.data})
    
    def delete(self,request,id):
        query_set = Customer_data.objects.get(id = id)
        serializer = Customer_dataSerializer(query_set)
        query_set.delete()
        return Response({"data" : serializer.data,'message':"data is deleted"})
    

    def get(self, request,id=None):
        if id is not None:
            query_set = Customer_data.objects.get(id=id)
            serializer = Customer_dataSerializer(query_set)
            return Response({"data" : serializer.data})
 
        else:    
            obj=Customer_data.objects.all()
            serializer = Customer_dataSerializer(obj , many=True)
            return Response({"data" : serializer.data}) 

    