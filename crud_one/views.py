from django.shortcuts import render, redirect    #
from django.http import HttpResponse
from crud_one.models import City       #

def main(request):
	return HttpResponse('Crud_one')

def login(request):
	return render(request, 'crud_one/login.html')

def login_process(request):
	return HttpResponse('login_process')
	
def register(request):
	return render(request, 'crud_one/register.html')
	
def register_process(request):
	return HttpResponse('register_process')
	
def logout(request):
	return HttpResponse('logout_process')
	
def page(request):
	allModels = City.objects.all()
	return render(request, 'crud_one/page.html', {'data': allModels})

def page_create(request):
	if request.POST:
		city = request.POST.get('city')
		country = request.POST['country']
		population = request.POST['population']
		model = City(city=city, country=country, population=population, owner=0)	
		model.save()
	return redirect('page')
	
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
	
def page_delete(request):
	if request.POST:
		id = request.POST.get('id')
		model = City.objects.filter(id=id)	
		model.delete()
	return redirect('page')
	
def admin(request):
	return render(request, 'crud_one/admin.html')

def admin_process(request):
	return HttpResponse('admin_process')
