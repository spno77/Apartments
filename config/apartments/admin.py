from django.contrib import admin
from users.models import User
from .models import Apartment

# Register your models here.
admin.site.register(Apartment)