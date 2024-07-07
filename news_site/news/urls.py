from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_index, name='front_index'),
    path('about/us/', views.front_about_us, name='front_about_us'),
    path('contact/us/', views.front_contact_us, name='front_contact_us'),
    path('contact/us/add/submit/', views.front_contact_us_submit, name='front_contact_us_submit'),
    path('post/single/<id>/', views.front_post_single, name='front_post_single'),
    path('post/single/comment/<id>/submit/', views.front_post_single_comment_submit, name='front_post_single_comment_submit'),
    path('post/list/all/', views.front_all_post_list, name='front_all_post_list'),
    path('post/list/<id>/', views.front_post_list, name='front_post_list'),
    path('post/news/letters/add/submit/', views.front_news_letters_submit, name='front_news_letters_submit'),
]
