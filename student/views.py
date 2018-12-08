from django.views.generic import TemplateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from teacher.models import Appointment
from teacher.forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def quick_appointmnet(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Student" == group_name:
		user_name=request.user.get_username()
		appointment_list = Appointment.objects.all().order_by("-user")
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name
		}
		return render(request, 'student_quick_appointmnet.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')


def student(request):#this section for my appointment
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Student" == group_name:
		user_name=request.user.get_username()#Getting Username
		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with=user_name)
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,    
		}
		return render(request, 'student.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')

def appointment_book(request, id):#activate after clicking book now button
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Student" == group_name:
		user_name=request.user.get_username()
		single_appointment= Appointment.objects.get(id=id)
		form = single_appointment
		form.appointment_with=user_name
		form.save()
		#return HttpResponseRedirect (instance.get_absolute_url())
		#messages.success(request, 'Your profile was updated.')
		return redirect('http://127.0.0.1:8000/student/')
	else:
		return redirect('http://127.0.0.1:8000/')




