# apartments/urls.py
from django.urls import path
from . import views

from .views import ApartmentList,ApartmentDetail,AvailabilityList,AvailabilityDetail

urlpatterns = [
	path('apartments/',views.ApartmentList.as_view()),
	path('apartments/<int:pk>/',views.ApartmentDetail.as_view()),
	path('availability/',views.AvailabilityList.as_view()),
	path('availability/<int:pk>/',views.AvailabilityDetail.as_view()),
]
