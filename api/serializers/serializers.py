from .. import models 
from rest_framework import serializers
from django.contrib.auth.models import User

class NavBarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NavBarItems
        fields = ['name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ['name','description','image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',]


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True, many = False)
    class Meta:
        model =  models.Doctor
        fields = ['name','email_address','gender','profile_picture','specialization','phone_number','user','doctors_id']