from .models import *
from rest_framework import serializers
import re
from django.contrib.auth.models import User

from django.contrib.auth.models import User

# class User_srializer(serializers.ModelSerializer ):
#     class Meta :
#         model = User
#         fields = ["username" , "password"]

#     def create(self, validated_data):
#         user = User.objects.create(username = validated_data['username'] )
#         user.set_password(validated_data['password']) 
#         user.save()
#         return user

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        # fields=['name','age']
        # exclude=['id']
        fields='__all__'
        


    
    def validate_name(self,data):
        if not data.isalpha():
            raise serializers.ValidationError("name only contains character field please enter again")

        else:
            return data
        

    def validate_price(self,med_price):

        if med_price <0:
            raise serializers.ValidationError("price must be in positive")

        else:
            return med_price
        

class Customer_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer_data
        fields='__all__'        
    # cust_name = serializers.CharField()
    def validate_cust_name(self,cust_name):
        if not cust_name.isalpha():
            raise serializers.ValidationError("name only contains character field please enter again")

        else:
            return cust_name
        
    cust_age = serializers.IntegerField()

    def validate_cust_age(self, cust_age):
        if cust_age < 18:
            raise serializers.ValidationError("Age must be greater than or equal to 18")
        return cust_age
    

    def validate_cust_phone(self,cust_phn):
       
       regex = r'^\+?1?\d{9,15}$'

       if not re.match(regex, cust_phn):
            raise serializers.ValidationError("Invalid phone number format.")

       return cust_phn

   