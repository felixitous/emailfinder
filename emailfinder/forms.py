from django import forms

class NameForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=100)
	middle_name = forms.CharField(label='Middle Name', max_length=100, required=False)
	last_name = forms.CharField(label='Last Name', max_length=100)
	domain_name = forms.CharField(label='Domain Name', max_length=100)
