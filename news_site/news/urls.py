from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_index, name='front_index'),
    path('about/us/', views.front_about_us, name='front_about_us'),
    path('contact/us/', views.front_contact_us, name='front_contact_us'),
    path('post/single/<id>/', views.front_post_single, name='front_post_single'),
    path('post/list/all/', views.front_all_post_list, name='front_all_post_list'),
    path('post/list/<id>/', views.front_post_list, name='front_post_list'),
]
