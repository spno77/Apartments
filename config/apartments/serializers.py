from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model

from .models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
	
	owner = serializers.PrimaryKeyRelatedField(source='owner.username',queryset=get_user_model().objects.all())

	class Meta:
		model = Apartment
		fields = ['id','description','price','garage','wifi','rooms','owner']

