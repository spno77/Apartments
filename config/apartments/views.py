from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Apartment,Availability
from .serializers import ApartmentSerializer,AvailabilitySerializer
from users.models import User
from django.shortcuts import get_object_or_404
from . import models

from .permissions import IsOwnerOrAdmin,IsOwner,IsAvailable
from rest_framework import permissions


class ApartmentList(generics.ListAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ApartmentCreate(generics.CreateAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ApartmentDetail(generics.RetrieveAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer


class ApartmentUpdate(generics.UpdateAPIView):
	permission_classes = [IsOwner,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer


class ApartmentDelete(generics.DestroyAPIView):
	permission_classes = [IsOwner,]
	queryset = Apartment.objects.all()
	serializer_class = ApartmentSerializer



class AvailabilityList(generics.ListCreateAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = Availability.objects.all()
	serializer_class = AvailabilitySerializer


class AvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAvailable,]
	queryset = Availability.objects.all()
	serializer_class = AvailabilitySerializer







		
