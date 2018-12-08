from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	teacher,
	teacher_appointment_list,
	appointment_delete,
	teacher_appointment_update,
	)





urlpatterns = [
    path('', views.teacher, name='teacher_home'),
    path('my_appointment/', views.teacher, name='teacher_appointment'),
    path('create_appointment/', views.teacher_appointment_list, name='teacher_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', teacher_appointment_update,name='teacher_appointment_update'),      
      
]

