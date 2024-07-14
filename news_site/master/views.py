from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import login , authenticate , logout 
from django.contrib.auth.models import  User , Permission
from django.contrib import messages
from settings_site.models import *
from news.models import *
from django.http import Http404, JsonResponse
import time
from datetime import date, datetime
import jdatetime



def master_panel(request):

    settings = Settings.objects.get(id=1)

    show_news_list = News.objects.all().order_by('-id')[:3]


    list_dashboard = {
        "settings":settings,"show_news_list":show_news_list,
    }

    return render(request, 'master/dashboard.html', list_dashboard)


def master_signin(request):

    settings = Settings.objects.get(id=1)
            

    list_signin = {
        "settings":settings,
    }

    return render(request, 'master/signin.html', list_signin)


def master_signin_submit(request):
    
    if request.method == "POST":

        usernams = request.POST.get('username')
        passwords = request.POST.get('password')
        user = authenticate(username = usernams , password = passwords)

        if user is not None:

            login(request,user)
            messages.success(request, f"  {request.user.get_full_name()} خوش اومدین.")
            return redirect("master_panel")
            
        else:
            messages.error(request,"نام کاربری یا رمز عبور نامعتبر است.")
            return redirect("master_signin")
            
    return redirect("master_signin")


def master_logout(request):

    logout(request)
    return redirect("master_signin")



def master_post_create(request):

    settings = Settings.objects.get(id=1)

    show_subcategory = SubCategory.objects.all()

    list_post_create = {
        "settings":settings,"show_subcategory":show_subcategory,
    }

    return render(request, 'master/dashboard-post-create.html', list_post_create)



def master_post_create_submit(request):

    if request.method == 'POST':
        title_news = request.POST.get('title_news')
        text_news = request.POST.get('text_news')
        sub_cat_news = request.POST.get('sub_cat_news')
        img_news = request.FILES.get('img_news')

        if not all([title_news, text_news, sub_cat_news]):
            return JsonResponse({"success": False, "message": "اطلاعات را کامل کنید", "data": {}}, status=200)

        try:
            sub_category = SubCategory.objects.get(id=sub_cat_news)
            create_news = News.objects.create(
                user=request.user,
                author=request.user,
                sub_category=sub_category,
                title=title_news,
                text=text_news,
                img=img_news,
                date=time.time(),
            )

            return JsonResponse({
                "success": True, 
                "message": 'خبر با موفقیت ایجاد شد.',
                "data": {'title_news': create_news.title}
            }, status=200)

        except SubCategory.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی نامعتبر است', "data": {}}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ایجاد خبر: {str(e)}', "data": {}}, status=200)

    return redirect('master_post_create')