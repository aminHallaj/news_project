from django.shortcuts import render , get_object_or_404 , redirect
from settings_site.models import *
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import  User , Permission
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger


def front_index(request):

    settings = Settings.objects.get(id=1)

    category_menu = Category.objects.all()

    category_menu2 = Category.objects.all()[:12]
    
    popular = News.objects.all().order_by('-id')[:4]

    news_slider = News.objects.all().order_by('-id')[:10]

    news_slider2 = News.objects.all().order_by('-id')[:4]

    news_list = News.objects.all()

    menu_news_list = News.objects.all().order_by('-id')[:4]

    list_index = {
        "category_menu2":category_menu2, "menu_news_list":menu_news_list,
        "news_slider2":news_slider2,"news_slider":news_slider,
        'popular':popular,'settings':settings,
        'news_list':news_list,"category_menu":category_menu
    }

    return render(request, 'front/index.html', list_index)


def front_about_us(request):

    settings=Settings.objects.get(id=1)
    category_menu=Category.objects.all()


    list_about_us = {
        'settings':settings,"category_menu":category_menu
    }

    return render(request, 'front/about-us.html', list_about_us)


def front_contact_us(request):

    settings=Settings.objects.get(id=1)
    category_menu=Category.objects.all()

    contact_us=ContactUsSettings.objects.get(id=1)


    list_contact_us = {
        'settings':settings,"category_menu":category_menu,"contact_us":contact_us
    }

    return render(request, 'front/contact-us.html', list_contact_us)


def front_post_single(request,id):

    settings=Settings.objects.get(id=1)
    category_menu=Category.objects.all()

    news_show=News.objects.get(id=id)


    list_post_single = {
        "id":id,'settings':settings,'news_show':news_show,"category_menu":category_menu
    }

    return render(request, 'front/post-single.html', list_post_single)


def front_post_list(request,id):

    settings=Settings.objects.get(id=1)
    category_menu=Category.objects.all()

    category_list=Category.objects.get(id=id)

    subcategories = category_list.subcategory.all()

    news_list = News.objects.filter(sub_category__in=subcategories)

    news_list_all=News.objects.all()


    paginator = Paginator (news_list,8)
    page = request.GET.get('page')

    try:
        news_list= paginator.page(page)
        
    except EmptyPage:
        news_list=paginator.page(paginator.num_page)

    except PageNotAnInteger:
        news_list=paginator.page(1)


    list_post_list = {
        "news_list_all":news_list_all,"news_list":news_list,'id':id,
        'settings':settings,"category_menu":category_menu,
        "category_list":category_list
    }


    return render(request, 'front/post-grid.html', list_post_list)