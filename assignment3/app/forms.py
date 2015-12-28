from django import forms
from .models import *

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 30)
	email = forms.EmailField()
	message = forms.CharField(max_length =200)

	def clean_message(self):
		message = self.cleaned_data['message']


class teacherForm(forms.Form):
	firstName = forms.CharField(max_length=30)
	lastName = forms.CharField(max_length=30)
	office_details = forms.CharField(max_length=200)
	phone_number = forms.CharField(max_length=11)
	email = forms.EmailField(max_length=70)

class studentForm(forms.Form):
	firstName = forms.CharField(max_length=30)
	lastName = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=70)

class courseForm(forms.Form):
	name = forms.CharField(max_length=70)
	code = forms.CharField(max_length=20)
	classroom = forms.CharField(max_length=20)
	times = forms.CharField(max_length=70)


studentss = [(std.firstName,std.firstName) for std in Student.objects.all()]
coursess = [(c.name,c.name) for c in Course.objects.all()]

class EnrollStudents(forms.Form):
	student = forms.ChoiceField(studentss, widget = forms.Select())
	course = forms.ChoiceField(coursess, widget = forms.Select())


