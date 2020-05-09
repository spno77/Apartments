from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
	
	#role = serializers.CharField(source='get_role_display')

	class Meta:
		model = get_user_model()
		fields = ['id','username','email','firstname','lastname','phone','image','role']

