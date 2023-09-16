from django.urls import path
from . import views

app_name = 'bank_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('api/branches/<int:district_id>/', views.get_branches_by_district, name='get_branches_by_district'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout, name='logout'),
]