from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Apartment
from .serializers import ApartmentSerializer
from users.models import User


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