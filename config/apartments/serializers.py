from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model

from .models import Apartment,Availability


class AvailabilitySerializer(serializers.ModelSerializer):

	apartment = serializers.PrimaryKeyRelatedField(queryset=Apartment.objects.all())
	
	class Meta:
		model = Availability
		fields = ['from_date','to_date','apartment']



class ApartmentSerializer(serializers.ModelSerializer):
	
	owner = serializers.PrimaryKeyRelatedField(source='owner.username',queryset=get_user_model().objects.all())
	availability = serializers.StringRelatedField(many=True)

	class Meta:
		model = Apartment
		fields = ['id','description','price','garage','wifi','rooms','owner','availability']
