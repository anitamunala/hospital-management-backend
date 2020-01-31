from django.shortcuts import render
from rest_framework import viewsets
from api.models import NavBarItems, Service, Doctor
from api.serializers.serializers import NavBarItemsSerializer, ServicesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# Create your views here.
class NavBarItemsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  NavBarItems.objects.all()
    serializer_class = NavBarItemsSerializer
class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer


@api_view(['GET'])
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
    



