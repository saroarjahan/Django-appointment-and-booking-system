from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout


def group_check(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string

	if "Student" == group_name:
		return redirect('http://127.0.0.1:8000/student/')
	elif "Teacher" == group_name:
		return redirect('http://127.0.0.1:8000/teacher/')

def logout_view(request):
	logout(request)
	return redirect('http://127.0.0.1:8000/')


class register_teacher(TemplateView):
  template_name = "register_teacher.html"

class register_student(TemplateView):
  template_name = "register_student.html"

