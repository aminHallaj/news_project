from django.shortcuts import render , get_object_or_404 , redirect , resolve_url
from settings_site.models import *
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import  User , Permission
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.http import Http404, JsonResponse
import time
from datetime import date, datetime
import jdatetime


def front_index(request):

    settings = Settings.objects.get(id=1)

    category_menu = Category.objects.all()

    category_menu2 = Category.objects.all()[:12]
    
    popular = News.objects.all().order_by('-id')[:4]

    news_slider = News.objects.all().order_by('-id')[:10]

    news_slider2 = News.objects.all().order_by('-id')[:4]

    news_list = News.objects.all().order_by('-id')

    menu_news_list = News.objects.all().order_by('-id')[:4]

    footer_news_list = News.objects.all().order_by('-id')[:2]

    list_index = {
        "category_menu2":category_menu2, "menu_news_list":menu_news_list,
        "news_slider2":news_slider2,"news_slider":news_slider,
        'popular':popular,'settings':settings,
        'news_list':news_list,"category_menu":category_menu,
        'footer_news_list':footer_news_list,
    }

    return render(request, 'front/index.html', list_index)


def front_about_us(request):

    settings=Settings.objects.get(id=1)
    
    category_menu=Category.objects.all()

    category_menu2 = Category.objects.all()[:12]

    menu_news_list = News.objects.all().order_by('-id')[:4]

    footer_news_list = News.objects.all().order_by('-id')[:2]


    list_about_us = {
        'settings':settings,"category_menu":category_menu,
        "menu_news_list":menu_news_list, "category_menu2":category_menu2,
        'footer_news_list':footer_news_list,
    }

    return render(request, 'front/about-us.html', list_about_us)


def front_contact_us(request):

    settings=Settings.objects.get(id=1)

    category_menu=Category.objects.all()

    category_menu2 = Category.objects.all()[:12]

    menu_news_list = News.objects.all().order_by('-id')[:4]

    contact_us=ContactUsSettings.objects.get(id=1)

    footer_news_list = News.objects.all().order_by('-id')[:2]

    list_contact_us = {
        'settings':settings,"category_menu":category_menu,
        "contact_us":contact_us, "menu_news_list":menu_news_list,
        "category_menu2":category_menu2, 'footer_news_list':footer_news_list,
    }

    return render(request, 'front/contact-us.html', list_contact_us)



def front_contact_us_submit(request):

    if request.method == 'POST':

        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        text = request.POST.get('text')

        if not all([last_name, email, text, title ]):
            return JsonResponse({"sucess":False, "message":"اطلاعات را کامل کنید", "data":{}},status=200)

        else:
        
            try:
                send_masseges_contact_us = ContactUs.objects.create(
                    user = request.user,
                    first_name_and_last_name = last_name,
                    email = email,
                    title = title,
                    text = text,
                )

                return JsonResponse({"success":True, "message":'پیام شما با موفقیت ارسال شد' , "data":{
            'last_name':send_masseges_contact_us.first_name_and_last_name ,
            'email':send_masseges_contact_us.email ,'text':send_masseges_contact_us.text,
            'title':send_masseges_contact_us.title }},status=200)

            except:
                return JsonResponse({"success":False, "message":'لطفا تمامی فیلد ها را پر کنید', "data":{}},status=200)

    return redirect('front_contact_us')



def front_post_single(request,id):

    settings = Settings.objects.get(id=1)

    category_menu = Category.objects.all()

    category_menu2 = Category.objects.all()[:12]

    category_show_list = Category.objects.all()[:12]

    menu_news_list = News.objects.all().order_by('-id')[:4]

    news_show = News.objects.get(id=id)

    comment_show = PointOfView.objects.filter(news_id=id).order_by('-id')

    footer_news_list = News.objects.all().order_by('-id')[:2]

    # category_post_counts = {category.id: category.news_set.count() for category in category_show_list}

    list_post_single = {
        "id":id,'settings':settings,'news_show':news_show, "category_menu2":category_menu2,
        "category_menu":category_menu, "menu_news_list":menu_news_list,
        'footer_news_list':footer_news_list, 'category_show_list':category_show_list,
        'comment_show':comment_show,
    }

    return render(request, 'front/post-single.html', list_post_single)


def front_post_single_comment_submit(request, id):

    if request.method == 'POST':

        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        if not all([last_name, email, comment]):
            return JsonResponse({"sucess":False, "message":"اطلاعات را کامل کنید", "data":{}},status=200)

        else:
        
            try:
                comment_add = PointOfView.objects.create(
                    user = request.user,
                    news_id = id,
                    first_name_and_last_name = last_name,
                    email = email,
                    date = time.time(),
                    text = comment,
                )

                return JsonResponse({"success":True, "message":'نظر شما با موفقیت ثبت شد' , "data":{
            'last_name':comment_add.first_name_and_last_name ,
            'email':comment_add.email ,'comment':comment_add.text, 'id':comment_add.id }},status=200)


            except:
                return JsonResponse({"success":False, "message":'لطفا تمامی فیلد ها را پر کنید', "data":{}},status=200)

    return redirect('front_post_single', id=id)



def front_all_post_list(request):

    settings=Settings.objects.get(id=1)

    category_menu=Category.objects.all()

    category_menu2 = Category.objects.all()[:12]

    menu_news_list = News.objects.all().order_by('-id')[:4]

    news_list=News.objects.all().order_by('-id')

    footer_news_list = News.objects.all().order_by('-id')[:2]


    paginator = Paginator (news_list,8)
    page = request.GET.get('page')

    try:
        news_list= paginator.page(page)
        
    except EmptyPage:
        news_list=paginator.page(paginator.num_page)

    except PageNotAnInteger:
        news_list=paginator.page(1)


    list_all_post_list = {
        "news_list":news_list, 'settings':settings,"category_menu":category_menu,
        "menu_news_list":menu_news_list,"category_menu2":category_menu2, 
        'footer_news_list':footer_news_list,
    }


    return render(request, 'front/post-grid.html', list_all_post_list)


def front_post_list(request,id):

    settings=Settings.objects.get(id=1)

    category_menu=Category.objects.all()

    category_menu2 = Category.objects.all()[:12]

    menu_news_list = News.objects.all().order_by('-id')[:4]

    category_list=Category.objects.get(id=id)

    subcategories = category_list.subcategory.all()

    news_list = News.objects.filter(sub_category__in=subcategories).order_by('-id')

    news_list_all=News.objects.all().order_by('-id')

    footer_news_list = News.objects.all().order_by('-id')[:2]


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
        "category_list":category_list, "menu_news_list":menu_news_list,
        "category_menu2":category_menu2, 'footer_news_list':footer_news_list,
    }


    return render(request, 'front/post-grid.html', list_post_list)


def front_news_letters_submit(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        if not all([email]):
            return JsonResponse({"sucess":False, "message":"اطلاعات را کامل کنید", "data":{}},status=200)
        
        if NewsLetters.objects.filter(email= email ).count() != 0 :
            return JsonResponse({"success":False, "message":'ایمیل وارد شده تکراری میباشد', "data":{}},status=200)

        else:
        
            try:
                news_letter_add = NewsLetters.objects.create(
                    email = email,
                )

                return JsonResponse({"success":True, "message":'شما با موفقیت در خبرنامه عضو شدید' , "data":{
                    'email':news_letter_add.email }},status=200)

            except:
                return JsonResponse({"success":False, "message":'خطایی رخ داده است لطفا دوباره تلاش کنید', "data":{}},status=200)

