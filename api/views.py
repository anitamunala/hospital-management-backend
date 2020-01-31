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
        serialize_all_services = serializers.Service(all_services, many = True)
        return Response({
            'status':status.HTTP_200_OK,
            'all_services':serialize_all_services.data
            
        })

@api_view['GET'])
def all_doctors(request):
    all_doctors_items = Doctor.objects.all()
    processed_doctors = []
    for doctor in all_doctors_items:
        temporary_doctor = {
            'name': doctor.name,
            'profile_picture': f'{doctor.profile_picture}',
            'specialization': doctor.specialization.name,

        }
        processed_doctors.append(temporary_doctor)
    print(processed_doctors)
    return Response({
        'status':  HTTP_200_OK,
        'data': processed_doctors

    })
    



