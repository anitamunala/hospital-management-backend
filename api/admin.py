from django.contrib import admin
from api import models

# Register your models here.
admin.site.register(models.NavBarItems)
admin.site.register(models.Doctor)
admin.site.register(models.Specialist)
admin.site.register(models.Patient)
admin.site.register(models.Service)

admin.site.site_header = "SHIS ADMIN"