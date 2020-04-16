# Django-appointment-and-booking-system
A  python prototype Django project for booking and appoientment for teacher and student

#This  web application has several important features :
(i) Easy appointment creation  for teacher 
(ii) Easy date picker, time picker and auto time suggestion while creating new appointment
(ii) Appointment edit and deletion  option 
(iv) Success notification
(v) Search  option with numeric and string
(vi) Calendar Integration
(vii) Central administrator
(viii) Different type of profile group like Teacher and Student 
(ix) Modular Login system


#References
To understand this project in code level we highly recommend  to have a good knowledge in python 3 (we have used 3.70), python web framework django (2.1.3). We also recommend to know little about javascript and its framework vue.js. We have used calendar integration and date picker with pure javascript, jQuery and vue.js. In calendar integration we have used Jason formatted data, so it's good have idea  about Jason. Finally, we recommend to have knowledge about html css, we have used bootstrap  framework for html and css. We also recommend to have very clear knowledge about foreign key relationship and sqlite3 database. 
https://www.djangoproject.com/ (***)
https://www.python.org/ (***)
https://getbootstrap.com/ (**)
https://developer.mozilla.org/bm/docs/Web/JavaScript (*)
https://vuejs.org/ (*)
https://fullcalendar.io/ (*)
http://jonthornton.github.io/jquery-timepicker/ (*)
https://www.w3schools.com/js/js_json_datatypes.asp (*)
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/(**)
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/(**)
https://medium.com/@_christopher/deploying-my-django-app-to-a-real-server-part-ii-f0c277c338f4(*)
https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/ (***)


Deployment in localhost windows pc:
####################################
To run this project in localhost , we have to setup python, pip, virtualenv and django.
Frist,  we have to make sure that we  have installed pip and python in our pc. Then,

1. Run Windows Powershell as Administrator

We have to create a new directory to install virtualenv . Browse that directory via command and run. separate virtual server for each project is best, it will not affect other project library.

2. pip install virtualenv
3. virtualenv .
4. Scripts\activate or scripts\activate

Now we have to create another directory inside virtualenv, then we have to install django inside it. Browse that new directory via command line and install django inside it.

5. pipenv install django /pip install django

Copy this  whole oproject inside django directory, browse the app and run 
python .\manage.py runserver

After successfully deployment we will  require this User access for the project: 
Supersuer: admin (url: http://127.0.0.1:8000/admin)
Other User: Teacher1, Teacher2, Student1, Student2 (url: http://127.0.0.1:8000/)
password for all admin and user: Saroar123

*Inside project some url is not dynamically set, I forget to do that

**See the screens.pdf for scrrenshot of the project
