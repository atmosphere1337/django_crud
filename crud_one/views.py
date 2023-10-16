from django.shortcuts import render
from django.http import HttpResponse

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
	return render(request, 'curd_one/page.html')

def page_create(request):
	return HttpResponse('page_create_process')
	
def page_update(request):
	return HttpResponse('page_update_process')
	
def page_delete(request):
	return HttpResponse('page_delete_process')
	
def admin(request):
	return render(request, 'curd_one/admin.html')

def admin_process(request):
	return HttpResponse('admin_process')
