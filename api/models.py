from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NavBarItems(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        

class Specialist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    email_address= models.EmailField()
    gender = models.CharField(max_length=10, default='male')
    profile_picture=models.ImageField(upload_to='media/', blank=True,null=True)
    specialization = models.ForeignKey(Specialist, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=15)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    doctors_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Doctor"


class Patient(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField()
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Patient"

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
