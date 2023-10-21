from django import forms 								#

class UserForm(forms.Form):
	login = forms.CharField(min_length = 3)
	password = forms.CharField(widget = forms.PasswordInput(), min_length = 3)
class CityCreateForm(forms.Form):
	city = forms.CharField(required=True)
	country = forms.CharField(required=True)
	population = forms.IntegerField(required=True)
class CityUpdateForm(forms.Form):
	id = forms.IntegerField(required=True)
	city = forms.CharField(required=True)
	country = forms.CharField(required=True)
	population = forms.IntegerField(required=True)
class CityDeleteForm(forms.Form):
	id = forms.IntegerField(required=True)


