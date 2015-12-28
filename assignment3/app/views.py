from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from .models import *
from .forms import *


def teacher_form(request):
	if request.method == 'POST':
		form = teacherForm(request.POST)
		if form.is_valid():
			firstName = form.cleaned_data["firstName"]
			lastName = form.cleaned_data["lastName"]
			office_details = form.cleaned_data["office_details"]
			phone_number = form.cleaned_data["phone_number"]
			email = form.cleaned_data["email"]
			a = Teacher(firstName = firstName, lastName = lastName, office_details=office_details, phone_number=phone_number, email=email)
			a.save()
			return HttpResponseRedirect("/allTeachers/")
	else:
		form = teacherForm()
	return render_to_response('Form.html', {'form':form}, RequestContext(request) )

def student_form(request):
	if request.method == 'POST':
		form = studentForm(request.POST)
		if form.is_valid():
			firstName = form.cleaned_data["firstName"]
			lastName = form.cleaned_data["lastName"]
			email = form.cleaned_data["email"]
			a = Student(firstName = firstName, lastName = lastName, email=email)
			a.save()
			return HttpResponseRedirect("/allStudents/")
	else:
		form = studentForm()
	return render_to_response('Form.html',{"form":form}, RequestContext(request))

def course_form(request):
	if request.method == 'POST':
		form = courseForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			code = form.cleaned_data["code"]
			classroom = form.cleaned_data["classroom"]
			times = form.cleaned_data["times"]
			a = Course(name=name, code=code, classroom = classroom, times=times)
			a.save()
			return HttpResponseRedirect("/allCourses/")
	else:
		form = courseForm()
	return render_to_response('Form.html',{"form":form}, RequestContext(request))

def allTeachers(request):
	a = Teacher.objects.all()
	return render_to_response('successT.html', {'list': a}, RequestContext(request))

def allStudents(request):
	a = Student.objects.all()
	return render_to_response('successS.html', {'list': a}, RequestContext(request))

def allCourses(request):
	a = Course.objects.all()
	return render_to_response('successC.html', {'list': a}, RequestContext(request))

def enroll_students(request):
	if request.method == 'POST':
		form = EnrollStudents(request.POST)
		if form.is_valid():
			student = form.cleaned_data['student']			
			course = form.cleaned_data['course']
			std = Student.objects.get(firstName = student)
			c = Course.objects.get(name = course)
			c.students.add(std)

			return HttpResponseRedirect("/course/"+course)
	else:
		form = EnrollStudents()
	return render_to_response('Form.html',{"form":form}, RequestContext(request))

def enrolled_students(request,course):
	stds = Course.objects.get(name=course).students.all()
	return render_to_response('courses.html', {'list': stds, 'name': course}, RequestContext(request))






