from django.contrib import admin

# Register your models here.
from . models import Department,Doctors_details,Patient_details

admin.site.register(Department)
admin.site.register(Doctors_details)
admin.site.register(Patient_details)
