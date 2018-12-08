from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	student,
	quick_appointmnet,
	appointment_book,
	)

urlpatterns = [
    path('', views.student, name='student'),
    path('my_appointment/', views.student, name='student'),
    path('quick_appointmnet/', views.quick_appointmnet, name='quick_appointmnet'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),
      
]
