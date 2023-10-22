from django.urls import path
from . import views

urlpatterns = [
	path('', views.main),
	path('login', views.login_c, name='login'),
	path('login/process', views.login_process),
	path('register', views.register),
	path('register/process', views.register_process),
	path('logout', views.logout_c),
	path('page', views.page, name='page'),
	path('page/create', views.page_create),
	path('page/update', views.page_update),
	path('page/delete', views.page_delete),
	path('admin', views.admin),
	path('admin/process', views.admin_process),
	path('cookie', views.cook),
]
