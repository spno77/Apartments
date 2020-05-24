from django.contrib import admin
from users.models import User
from .models import Apartment,Availability

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Availability)