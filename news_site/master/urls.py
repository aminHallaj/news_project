from django.urls import path
from . import views

urlpatterns = [
    path('master/signin/', views.master_signin, name='master_signin'),
    path('master/signin/submit/', views.master_signin_submit, name='master_signin_submit'),
    path('master/logout/', views.master_logout, name='master_logout'),
    path('master/dashboard/', views.master_panel, name='master_panel'),
    path('master/dashboard/post/create/', views.master_post_create, name='master_post_create'),
    path('master/dashboard/post/create/submit/', views.master_post_create_submit, name='master_post_create_submit'),
    path('master/dashboard/category/create/', views.master_category_create, name='master_category_create'),
    path('master/dashboard/category/create/submit/', views.master_category_create_submit, name='master_category_create_submit'),
    path('master/dashboard/category/delete/<id>/', views.master_category_delete, name='master_category_delete'),

]