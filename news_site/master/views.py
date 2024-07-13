from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import login , authenticate , logout 
from django.contrib.auth.models import  User , Permission
from django.contrib import messages
from settings_site.models import *
from news.models import *



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

    list_post_create = {
        "settings":settings,
    }

    return render(request, 'master/dashboard-post-create.html', list_post_create)



def master_post_create_submit(request):
    pass