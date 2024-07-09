from django.urls import path
from . import views

urlpatterns = [
    path('master/dashboard/', views.master_panel, name='master_panel'),
    path('master/signin/', views.master_signin, name='master_signin'),
    path('master/signin/submit/', views.master_signin_submit, name='master_signin_submit'),
    path('master/logout/', views.master_logout, name='master_logout'),

]