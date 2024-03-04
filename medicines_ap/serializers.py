from .models import *
from rest_framework import serializers
import re
from django.contrib.auth.models import User

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

    def validate_name(self,data):
        if not data.isalpha():
            raise serializers.ValidationError("name only contains character field please enter again")

        else:
            return data


   