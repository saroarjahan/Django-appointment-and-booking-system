from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import Group


def teacher(request):#this section for my appointment
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Teacher" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(appointment_with__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name
		}
		return render(request, 'teacher.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/') 

def teacher_appointment_list(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Teacher" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)
		else:
			appointment_list = appointment_list #search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		    "form":AppointmentForm(),
		}
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			    saving=form.save(commit=False)
			    saving.user=request.user
			    saving.save()
			    messages.success(request, 'Post Created Sucessfully')
		return render(request, 'teacher_create_appointment.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')

  
def appointment_delete(request, id):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Teacher" == group_name:
		single_appointment= Appointment.objects.get(id=id)
		single_appointment.delete()
		messages.success(request, 'Your profile was updated.')
		return redirect('http://127.0.0.1:8000/teacher/create_appointment/')
	else:
		return redirect('http://127.0.0.1:8000/')

def teacher_appointment_update(request,id):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Teacher" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)
		else:
			appointment_list = appointment_list #search end

		single_appointment=ingle_appointment= Appointment.objects.get(id=id)
		form = AppointmentForm(request.POST or None, instance=single_appointment)
		if form.is_valid():
			    saving=form.save(commit=False)
			    saving.user=request.user
			    saving.save()
			    messages.success(request, 'Post Created Sucessfully')
			    return redirect('http://127.0.0.1:8000/teacher/create_appointment/')
			    

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		    "form":form,
		}

		return render(request, 'teacher_appointment_update.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')