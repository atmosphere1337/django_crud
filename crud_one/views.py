from django.shortcuts import render, redirect #
from django.http import HttpResponse
from crud_one.models import City        	  #
from .forms import *              			  #
from django.contrib.auth.models import User   #
from django.contrib.auth import login, authenticate, logout   #
from django.contrib import messages                  #
from django.contrib.auth.decorators import login_required, permission_required   #

def main(request):
	return HttpResponse('Crud_one')

def login_c(request):
	return render(request, 'crud_one/login.html', {'form': UserForm})

def login_process(request):
	if request.POST:
		login_str = request.POST.get('login')
		password = request.POST['password']
		model = authenticate(username=login_str, password=password)
		if model is not None:
			login(request, model)
			messages.info(request, f"Welcome, {login_str}")
			return redirect('page')
		else:
			messages.error(request, "Wrong login or password")
			return redirect('login')
	return redirect('login')
	
def register(request):
	return render(request, 'crud_one/register.html', {'form': UserForm})

def register_process(request):
	if request.POST:
		login = request.POST.get('login')
		password = request.POST['password']
		User.objects.create_user(username=login, password=password)
	return redirect('login')	


@login_required
def logout_c(request):
	logout(request)
	return redirect('login')
	
@login_required
def page(request):
	allModels = City.objects.all()
	output = {}
	output['data'] = allModels 
	output['form_create'] = CityCreateForm 
	output['form_update'] = CityUpdateForm
	output['form_delete'] = CityDeleteForm
	output['id'] = request.user.id
	return render(request, 'crud_one/page.html', output)

@login_required
def page_create(request):
	if request.POST:
		city = request.POST.get('city')
		country = request.POST['country']
		population = request.POST['population']
		model = City(city=city, country=country, population=population, owner=0)	
		model.save()
	return redirect('page')
	
@login_required
def page_update(request):
	if request.POST:
		id = request.POST.get('id')
		city = request.POST.get('city')
		country = request.POST['country']
		population = request.POST['population']
		model = City.objects.get(id=id)	
		model.city = city
		model.country = country
		model.population = population
		model.save()
	return redirect('page')
	
@login_required
def page_delete(request):
	if request.POST:
		id = request.POST.get('id')
		model = City.objects.filter(id=id)	
		model.delete()
	return redirect('page')
	
@login_required
def admin(request):
	if request.user.is_superuser: 
		return render(request, 'crud_one/admin.html')
	else:
		messages.error(request, 'you are not admin')
		return redirect('page')

@login_required
def admin_process(request):
	return HttpResponse('admin_process')

@login_required
def cook(request):
	if request.COOKIES.get('cook'):
		return HttpResponse('The cookie is still acitve for 5s')
	else:
		response = HttpResponse()
		response.write('Cookie was unset but now it is. Reload the page')
		response.set_cookie(key='cook', value = 1, max_age=5)
		return response

