from rest_framework import viewsets
from . import models
from .serializers import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class NavBarItemsViewSet(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        all_navbar_items = models.NavBarItems.objects.all()
        serialize_all_navbar_items = serializers.NavBarItemSerializer(all_navbar_items, many = True)
        return Response({
            'status': status.HTTP_200_OK,
            'all_navbar_items': serialize_all_navbar_items.data
        })


class ServicesViewSet(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        all_services = models.Service.objects.all()
        serialize_all_services = serializers.ServiceSerializer(all_services, many = True)
        return Response({
            'status':status.HTTP_200_OK,
            'all_services':serialize_all_services.data
        })


class  AllDoctors(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request):
        all_doctors = models.Doctor.objects.all()
        serialize_all_doctors = serializers.DoctorSerializer(all_doctors, many= True)
        return Response({
            'status' : status.HTTP_200_OK,
            'all_doctors': serialize_all_doctors.data
        })
    
    



