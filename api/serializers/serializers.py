from api.models import NavBarItems, Service, Doctor
from rest_framework import serializers

class NavBarItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBarItems
        fields = ['name']

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['name','description','image']
