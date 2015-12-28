from __future__ import unicode_literals

from django.db import models

class Teacher(models.Model):
	firstName = models.CharField(max_length=30, blank = True)
	lastName = models.CharField(max_length=30, blank = True)
	office_details = models.CharField(max_length=200, blank = True)
	phone_number = models.CharField(max_length=11)
	email = models.EmailField(max_length=70,blank=True)

class Student(models.Model):
	firstName = models.CharField(max_length=30, blank = True)
	lastName = models.CharField(max_length=30, blank = True)
	email = models.EmailField(max_length=70,blank=True)

	
class Course(models.Model):
	name = models.CharField(max_length=70, blank = True)
	code = models.CharField(max_length=20, blank = True)
	classroom = models.CharField(max_length=20, blank = True)
	times = models.CharField(max_length=70, blank = True)
	teacher = models.ForeignKey(Teacher, null=True)
	students = models.ManyToManyField(Student, null=True)
