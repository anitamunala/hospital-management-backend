from api.models import NavBarItems, Service, Doctor
from rest_framework import serializers

class NavBarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBarItems
        fields = ['name']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['name','description','image']
