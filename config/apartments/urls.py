# apartments/urls.py
from django.urls import path
from . import views

from .views import ApartmentList,ApartmentDetail

urlpatterns = [
	path('apartments/',views.ApartmentList.as_view()),
	path('apartments/<int:pk>/',views.ApartmentDetail.as_view()),
]
