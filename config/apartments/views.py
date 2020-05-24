from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Apartment,Availability
from .serializers import ApartmentSerializer,AvailabilitySerializer
from users.models import User
from django.shortcuts import get_object_or_404
from . import models

class ApartmentList(generics.ListCreateAPIView):
	#permission_classes = [permissions.IsAdminUser,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [IsOwnerOrAdmin,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer


class AvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [IsOwnerOrAdmin,]
	queryset = Availability.objects.all()
	serializer_class = AvailabilitySerializer

class AvailabilityList(generics.ListCreateAPIView):
	#permission_classes = [IsOwnerOrAdmin,]
	queryset = Availability.objects.all()
	serializer_class = AvailabilitySerializer






		
