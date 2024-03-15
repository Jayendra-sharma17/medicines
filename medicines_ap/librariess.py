#here all the import necessary libraries will come which i need to use in my Medical store management project

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
from bson import json_util
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import os
import json
from bson import ObjectId
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['Medicine_data']
collection = db['Medicine_collection']
