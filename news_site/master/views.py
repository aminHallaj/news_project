from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import login , authenticate , logout 
from django.contrib.auth.models import  User , Permission
from django.contrib import messages
from django.urls import reverse
from settings_site.models import *
from news.models import *
from customer.models import *
from django.http import Http404, HttpResponseRedirect, JsonResponse
import time
from datetime import date, datetime
import jdatetime
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.db.models import Q, Value as V
import re
from django.db.models.functions import Concat
from django.template.loader import render_to_string
from django.utils.text import slugify



def master_panel(request):

    if not request.user.is_authenticated:
        return redirect('master_signin')

    settings = Settings.objects.get(id=1)

    show_news_list = News.objects.all().order_by('-id')[:3]

    # تعداد خبرها
    news_count = News.objects.count()

    # تعداد نظرها
    comment_count = PointOfView.objects.count()

    # تعداد کاربران
    user_count = User.objects.count()

    show_reviews_list = PointOfView.objects.all().order_by('-id')[:4]

    news_list_show = News.objects.all().order_by('-id')

    search_query = request.GET.get('search')

    if search_query:
        news_list_show = news_list_show.annotate(
        full_name=Concat('author__first_name', V(' '), 'author__last_name')
        ).filter(
            Q(title__icontains=search_query) |
            Q(full_name__icontains=search_query) |
            Q(sub_category__title__icontains=search_query) |
            Q(sub_category__category__title__icontains=search_query)
        )

    paginator = Paginator(news_list_show, 8)
    page = request.GET.get('page', 1)
    news_list_show = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            template_name="master/includes/news_list_table.html",
            context={"news_list_show": news_list_show}
        )
        pagination_html = render_to_string(
            template_name="master/includes/pagination.html",
            context={"news_list_show": news_list_show}
        )
        data_dict = {
            "html_from_view": html,
            "pagination_html": pagination_html,
            "start_index": news_list_show.start_index(),
            "end_index": news_list_show.end_index(),
            "total_count": paginator.count,
        }
        return JsonResponse(data=data_dict, safe=False)

    list_dashboard = {
        "settings":settings,"show_news_list":show_news_list,
        "news_count":news_count,"comment_count":comment_count,
        "user_count":user_count,"news_list_show":news_list_show,
        "show_reviews_list":show_reviews_list,
    }

    return render(request, 'master/dashboard.html', list_dashboard)


def master_signin(request):

    settings = Settings.objects.get(id=1)

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('master_panel'))
    
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


def master_post_list(request):
    if not request.user.is_authenticated:
        return redirect('master_signin')
    settings = Settings.objects.get(id=1)
    news_list_show = News.objects.all().order_by('-id')

    search_query = request.GET.get('search')

    if search_query:
        news_list_show = news_list_show.annotate(
        full_name=Concat('author__first_name', V(' '), 'author__last_name')
        ).filter(
            Q(title__icontains=search_query) |
            Q(full_name__icontains=search_query) |
            Q(sub_category__title__icontains=search_query) |
            Q(sub_category__category__title__icontains=search_query)
        )

    paginator = Paginator(news_list_show, 8)
    page = request.GET.get('page', 1)
    news_list_show = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            template_name="master/includes/news_list_table.html",
            context={"news_list_show": news_list_show}
        )
        pagination_html = render_to_string(
            template_name="master/includes/pagination.html",
            context={"news_list_show": news_list_show}
        )
        data_dict = {
            "html_from_view": html,
            "pagination_html": pagination_html,
            "start_index": news_list_show.start_index(),
            "end_index": news_list_show.end_index(),
            "total_count": paginator.count,
        }
        return JsonResponse(data=data_dict, safe=False)

    list_news = {
        "settings": settings,
        "news_list_show": news_list_show,
        "paginator": paginator
    }

    return render(request, 'master/dashboard-post-list.html', list_news)



def master_post_create(request):
    if not request.user.is_authenticated:
        return redirect('master_signin')

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

        if not all([title_news, text_news, sub_cat_news, img_news]):
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
            return JsonResponse({"success": False, "message": f'خطا در ایجاد خبر: دسته بندی خود را انتخاب نکرده اید', "data": {}}, status=200)

    return redirect('master_post_create')



def master_post_edit(request, id):
    
    if not request.user.is_authenticated:
        return redirect('master_signin')

    settings = Settings.objects.get(id=1)

    edit_news = News.objects.get(id=id)

    show_subcategory = SubCategory.objects.all()

    list_post_create = {
        "settings":settings,"edit_news":edit_news,"show_subcategory":show_subcategory,
    }

    return render(request, 'master/dashboard-post-edit.html', list_post_create)



def master_post_edit_submit(request ,id):

    if request.method == 'POST':
        edit_news = get_object_or_404(News, id=id)
        
        title_news_edit = request.POST.get('title_news_edit')
        text_news_edit = request.POST.get('text_news_edit')
        sub_cat_news_edit = request.POST.get('sub_cat_news_edit') or edit_news.sub_category.id
        img_news_edit = request.FILES.get('img_news_edit')

        if not all([title_news_edit, text_news_edit]):
            return JsonResponse({"success": False, "message": "لطفا تمام فیلدهای ضروری را پر کنید"}, status=400)

        try:
            sub_category = SubCategory.objects.get(id=sub_cat_news_edit)
            
            edit_news.title = title_news_edit
            edit_news.text = text_news_edit
            edit_news.sub_category = sub_category
            edit_news.date = time.time()
            
            if img_news_edit:
                edit_news.img = img_news_edit
            
            edit_news.save()
            messages.success(request, 'خبر با موفقیت بروز شد')

            return JsonResponse({
                "success": True,
                "message": 'خبر با موفقیت ویرایش شد.',
                "redirect_url": reverse('master_post_list')
            })

        except SubCategory.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی نامعتبر است'}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ویرایش خبر: {str(e)}'}, status=500)

    return redirect('master_post_list')



def master_change_news_status(request, id):
    news = get_object_or_404(News, id=id)
    status = request.POST.get('status')
    reason = request.POST.get('reason', '')

    if status in ['0', '1', '2']:
        news.status_news = int(status)
        if status == '2':
            news.reject_reason = reason
        news.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def master_resubmit_news(request, id):
    news = get_object_or_404(News, id=id)
    if news.status_news == 2:  # اگر رد شده است
        news.status_news = 0  # به حالت در حال انتظار تغییر می‌دهد
        news.save()
    return redirect('master_post_edit', id=news.id)



def master_category_create(request):
    if not request.user.is_authenticated:
        return redirect('master_signin')

    settings = Settings.objects.get(id=1)
    show_add_category = Category.objects.all().order_by('-id')

    # Category logic
    show_list_category = Category.objects.all().order_by('-id')
    category_search_query = request.GET.get('category_search')
    if category_search_query:
        show_list_category = show_list_category.filter(Q(title__icontains=category_search_query))

    category_paginator = Paginator(show_list_category, 8)
    category_page = request.GET.get('category_page', 1)
    show_list_category = category_paginator.get_page(category_page)

    # Subcategory logic
    show_list_sub_category = SubCategory.objects.all().order_by('-id')
    subcategory_search_query = request.GET.get('subcategory_search')
    if subcategory_search_query:
        show_list_sub_category = show_list_sub_category.filter(Q(title__icontains=subcategory_search_query) |
        Q(category__title__icontains=subcategory_search_query))

    subcategory_paginator = Paginator(show_list_sub_category, 8)
    subcategory_page = request.GET.get('subcategory_page', 1)
    show_list_sub_category = subcategory_paginator.get_page(subcategory_page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.GET.get('table') == 'category':
            html = render_to_string(
                template_name="master/includes/category_list_table.html",
                context={"show_list_category": show_list_category}
            )
            pagination_html = render_to_string(
                template_name="master/includes/category_pagination.html",
                context={"show_list_category": show_list_category}
            )
            data_dict = {
                "html_from_view": html,
                "pagination_html": pagination_html,
                "start_index": show_list_category.start_index(),
                "end_index": show_list_category.end_index(),
                "total_count": category_paginator.count,
            }
        elif request.GET.get('table') == 'subcategory':
            html = render_to_string(
                template_name="master/includes/sub_category_list_table.html",
                context={"show_list_sub_category": show_list_sub_category}
            )
            pagination_html = render_to_string(
                template_name="master/includes/sub_category_pagination.html",
                context={"show_list_sub_category": show_list_sub_category}
            )
            data_dict = {
                "html_from_view": html,
                "pagination_html": pagination_html,
                "start_index": show_list_sub_category.start_index(),
                "end_index": show_list_sub_category.end_index(),
                "total_count": subcategory_paginator.count,
            }
        return JsonResponse(data=data_dict, safe=False)

    list_cat_and_sub_cat_create = {
        "settings": settings,
        "show_add_category": show_add_category,
        "show_list_category": show_list_category,
        "show_list_sub_category": show_list_sub_category,
    }

    return render(request, 'master/dashboard-post-categories.html', list_cat_and_sub_cat_create)

def is_valid_hex_color(color):
    return re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color) is not None


def master_category_create_submit(request):

    if request.method == 'POST':
        title_category = request.POST.get('title_category')
        color_bg_category = request.POST.get('color_bg_category')
        color_text_category = request.POST.get('color_text_category')
        img_category = request.FILES.get('img_category')

        if not all([title_category]):
            return JsonResponse({"success": False, "message": "اطلاعات را کامل کنید", "data": {}}, status=200)

        if Category.objects.filter(title=title_category).exists():
            return JsonResponse({"success": False, "message": 'دسته بندی وارد شده تکراری میباشد'}, status=200)

        if not is_valid_hex_color(color_bg_category) or not is_valid_hex_color(color_text_category):
            return JsonResponse({"success": False, "message": "کد رنگ نامعتبر است"}, status=200)
        
        try:
            create_category = Category.objects.create(
                user=request.user,
                title=title_category,
                color=color_bg_category,
                color_text=color_text_category,
                img=img_category,
            )

            return JsonResponse({
                "success": True, 
                "message": 'دسته بندی با موفقیت ایجاد شد.',
                "data": {'title_category': create_category.title,'color_bg_category': create_category.color,
                'color_text_category': create_category.color_text,
                'img_category': create_category.img.url if create_category.img else None,}
            }, status=200)

        except SubCategory.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی نامعتبر است', "data": {}}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ایجاد دسته بندی: {str(e)}', "data": {}}, status=200)

    return redirect('master_category_create')


def master_category_delete(request, id):

    try:
        category_delete = Category.objects.get(id=id)
        try:
            fs = FileSystemStorage()
            fs.delete(category_delete.img)
        except:
            pass

        category_delete.delete()

        return JsonResponse({"success":True, "message":"حذف با موفقیت انجام شد ", "data":{}},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"success":False, "message":"حذف انجام نشد ", "data":{}},status=200)
    

def master_category_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('master_signin')

    try:
        category = Category.objects.get(id=id)
        return JsonResponse({
            'title': category.title,
            'color': category.color,
            'color_text': category.color_text,
        })
    except Category.DoesNotExist:
        return JsonResponse({'error': 'دسته‌بندی یافت نشد'}, status=404)


def master_category_edit_submit(request, id):

    if request.method == 'POST':
        title_category_edit = request.POST.get('title_category_edit')
        color_bg_category_edit = request.POST.get('color_bg_category_edit')
        color_text_category_edit = request.POST.get('color_text_category_edit')
        img_category_edit = request.FILES.get('img_category_edit')

        if not title_category_edit:
            return JsonResponse({"success": False, "message": "اطلاعات را کامل کنید"}, status=200)
        
        if not is_valid_hex_color(color_bg_category_edit) or not is_valid_hex_color(color_text_category_edit):
            return JsonResponse({"success": False, "message": "کد رنگ نامعتبر است"}, status=200)


        try:
            edit_category = Category.objects.get(id=id)
            edit_category.title = title_category_edit
            edit_category.color = color_bg_category_edit
            edit_category.color_text = color_text_category_edit
            
            if img_category_edit:
                edit_category.img = img_category_edit
            
            edit_category.save()

            return JsonResponse({
                "success": True,
                "message": 'دسته بندی با موفقیت ویرایش شد',
                "data": {
                    'title_category_edit': edit_category.title,
                    'color_bg_category_edit': edit_category.color,
                    'color_text_category_edit': edit_category.color_text,
                    'img_category_edit': edit_category.img.url if edit_category.img else None,
                    'id': edit_category.id
                }
            }, status=200)

        except Category.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی نامعتبر است'}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ویرایش دسته بندی: {str(e)}'}, status=200)

    return redirect('master_category_create')



def master_sub_category_create_submit(request):

    if request.method == 'POST':
        title_subcategory_add = request.POST.get('title_subcategory_add')
        category_add_show = request.POST.get('category_add_show')

        if not all([title_subcategory_add, category_add_show]):
            return JsonResponse({"success": False, "message": "اطلاعات را کامل کنید", "data": {}}, status=200)

        if SubCategory.objects.filter(title=title_subcategory_add).exists():
            return JsonResponse({"success": False, "message": 'دسته بندی وارد شده تکراری میباشد'}, status=200)

        try:
            category = Category.objects.get(id=category_add_show)
            create_sub_category = SubCategory.objects.create(
                user=request.user,
                category=category,
                title=title_subcategory_add,
            )

            return JsonResponse({
                "success": True, 
                "message": 'زیر دسته بندی با موفقیت ایجاد شد.',
                "data": {
                    'title_subcategory_add': create_sub_category.title,
                    'category_title': create_sub_category.category.title
                }
            }, status=200)

        except Category.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی اصلی یافت نشد', "data": {}}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ایجاد زیر دسته بندی: {str(e)}', "data": {}}, status=200)

    return redirect('master_category_create')


def master_sub_category_delete(request, id):

    try:
        sub_category_delete = SubCategory.objects.get(id=id)

        sub_category_delete.delete()

        return JsonResponse({"success":True, "message":"حذف با موفقیت انجام شد ", "data":{}},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"success":False, "message":"حذف انجام نشد ", "data":{}},status=200)
    

def master_sub_category_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('master_signin')

    try:
        category = Category.objects.get(id=id)
        return JsonResponse({
            'title': category.title,
            'color': category.color,
            'color_text': category.color_text,
        })
    except Category.DoesNotExist:
        return JsonResponse({'error': 'دسته‌بندی یافت نشد'}, status=404)


def master_sub_category_edit_submit(request, id):

    if request.method == 'POST':
        title_category_edit = request.POST.get('title_category_edit')
        color_bg_category_edit = request.POST.get('color_bg_category_edit')
        color_text_category_edit = request.POST.get('color_text_category_edit')
        img_category_edit = request.FILES.get('img_category_edit')

        if not title_category_edit:
            return JsonResponse({"success": False, "message": "اطلاعات را کامل کنید"}, status=200)
        
        if not is_valid_hex_color(color_bg_category_edit) or not is_valid_hex_color(color_text_category_edit):
            return JsonResponse({"success": False, "message": "کد رنگ نامعتبر است"}, status=200)


        try:
            edit_category = Category.objects.get(id=id)
            edit_category.title = title_category_edit
            edit_category.color = color_bg_category_edit
            edit_category.color_text = color_text_category_edit
            
            if img_category_edit:
                edit_category.img = img_category_edit
            
            edit_category.save()

            return JsonResponse({
                "success": True,
                "message": 'دسته بندی با موفقیت ویرایش شد',
                "data": {
                    'title_category_edit': edit_category.title,
                    'color_bg_category_edit': edit_category.color,
                    'color_text_category_edit': edit_category.color_text,
                    'img_category_edit': edit_category.img.url if edit_category.img else None,
                    'id': edit_category.id
                }
            }, status=200)

        except Category.DoesNotExist:
            return JsonResponse({"success": False, "message": 'دسته بندی نامعتبر است'}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ویرایش دسته بندی: {str(e)}'}, status=200)

    return redirect('master_category_create')


def master_post_delete(request, id):

    try:
        news_delete = News.objects.get(id=id)
        try:
            fs = FileSystemStorage()
            fs.delete(news_delete.img)
        except:
            pass

        news_delete.delete()

        return JsonResponse({"success":True, "message":"حذف با موفقیت انجام شد ", "data":{}},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"success":False, "message":"حذف انجام نشد ", "data":{}},status=200)


def master_reviews(request):

    if not request.user.is_authenticated:
        return redirect('master_signin')

    settings = Settings.objects.get(id=1)

    show_reviews_list = PointOfView.objects.all().order_by('-id')


    paginator = Paginator(show_reviews_list, 8)
    page = request.GET.get('page', 1)
    show_reviews_list = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            template_name="master/includes/reviews_list_table.html",
            context={"show_reviews_list": show_reviews_list}
        )
        pagination_html = render_to_string(
            template_name="master/includes/reviews_pagination.html",
            context={"show_reviews_list": show_reviews_list}
        )
        data_dict = {
            "html_from_view": html,
            "pagination_html": pagination_html,
            "start_index": show_reviews_list.start_index(),
            "end_index": show_reviews_list.end_index(),
            "total_count": paginator.count,
        }
        return JsonResponse(data=data_dict, safe=False)


    list_reviews = {
    "settings":settings,"show_reviews_list":show_reviews_list,
    "paginator":paginator,
    }
    return render(request, 'master/dashboard-reviews.html', list_reviews)


def master_toggle_review_active(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        is_active = request.POST.get('is_active') == 'true'
        
        try:
            review = PointOfView.objects.get(id=review_id)
            review.active = is_active
            review.save()
            return JsonResponse({'status': 'success'})
        except PointOfView.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Review not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def master_reviews_delete(request, id):

    try:
        reviews_delete = PointOfView.objects.get(id=id)
        reviews_delete.delete()

        return JsonResponse({"success":True, "message":"حذف با موفقیت انجام شد ", "data":{}},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"success":False, "message":"حذف انجام نشد ", "data":{}},status=200)
    

def master_reviews_edit_submit(request, id):
    if request.method == 'POST':
        edit_reviews = get_object_or_404(PointOfView, id=id)
        text_reviews_edit = request.POST.get('text_reviews_edit')

        if not text_reviews_edit:
            return JsonResponse({"success": False, "message": "لطفا متن نظر را وارد کنید"}, status=200)

        try:
            edit_reviews.text = text_reviews_edit
            edit_reviews.save()
            return JsonResponse({
                "success": True,
                "message": 'نظر کاربر با موفقیت ویرایش شد.',
                "data": {
                    'text_reviews_edit': edit_reviews.text,
                    'id': edit_reviews.id
                }
            })
        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ویرایش نظر کاربر: {str(e)}'}, status=200)

    return JsonResponse({"success": False, "message": "درخواست نامعتبر"}, status=200)


def master_author_list(request):
    if not request.user.is_authenticated:
        return redirect('master_signin')

    settings = Settings.objects.get(id=1)
    author = Author.objects.filter(status_author=1).order_by('-id')
    author_status = Author.objects.all().order_by('-id')

    paginator = Paginator(author, 8)
    page = request.GET.get('page', 1)
    author = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            template_name="master/includes/author_list_table.html",
            context={"author": author}
        )
        pagination_html = render_to_string(
            template_name="master/includes/author_pagination.html",
            context={"author": author}
        )
        data_dict = {
            "html_from_view": html,
            "pagination_html": pagination_html,
            "start_index": author.start_index(),
            "end_index": author.end_index(),
            "total_count": paginator.count,
        }
        return JsonResponse(data=data_dict, safe=False)

    list_author_show = {
        "settings": settings, "author": author, "author_status": author_status,
    }

    return render(request, 'master/dashboard-author-list.html', list_author_show)

def master_change_author_status(request, id):
    author = get_object_or_404(Author, id=id)
    status = request.POST.get('status')

    if status in ['0', '1', '2']:
        author.status_author = int(status)
        author.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def master_resubmit_author(request, id):
    author = get_object_or_404(Author, id=id)
    if author.status_author == 2:  # اگر رد شده است
        author.status_author = 0  # به حالت در حال انتظار تغییر می‌دهد
        author.save()
    return redirect('master_post_edit', id=author.id)


def master_toggle_author_active(request):
    if request.method == 'POST':
        print("Received POST request:", request.POST)
        author_id  = request.POST.get('author_id')
        is_active = request.POST.get('is_active') == 'true'
        
        try:
            author = Author.objects.get(id=author_id)
            author.is_active = is_active
            author.save()
            return JsonResponse({'success': True})
        except Author.DoesNotExist:
            return JsonResponse({'success': False}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'روش درخواست نامعتبر است'}, status=400)



def master_author_create_submit(request):
    if request.method == 'POST':
        # دریافت داده‌های فرم
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        national_code = request.POST.get('nationalCode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        biography = request.POST.get('biography')
        slug = request.POST.get('slug')
        profile_image = request.FILES.get('profile')

        # بررسی اطلاعات ضروری
        if not all([first_name, last_name, national_code, phone, email, username, birthdate, gender]):
            return JsonResponse({"success": False, "message": "لطفاً تمام فیلدهای ضروری را پر کنید.", "data": {}}, status=400)

        # بررسی وجود یوزرنیم
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success": False,
                "message": "این نام کاربری قبلاً استفاده شده است.",
                "field": "username"
            }, status=400)

        # بررسی وجود ایمیل
        if User.objects.filter(email=email).exists():
            return JsonResponse({
                "success": False,
                "message": "این ایمیل قبلاً استفاده شده است.",
                "field": "email"
            }, status=400)

        # بررسی وجود کد ملی
        if Author.objects.filter(national_id=national_code).exists():
            return JsonResponse({
                "success": False,
                "message": "این کد ملی قبلاً ثبت شده است.",
                "field": "nationalCode"
            }, status=400)

        # بررسی وجود شماره تلفن
        if Author.objects.filter(mobile=phone).exists():
            return JsonResponse({
                "success": False,
                "message": "این شماره تلفن قبلاً ثبت شده است.",
                "field": "phone"
            }, status=400)

        try:
            # ایجاد کاربر جدید
            user = User.objects.create_user(username=username, email=email, password=national_code)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # تبدیل جنسیت به عدد مناسب
            gender_map = {'male': 1, 'female': 2}
            gender_num = gender_map.get(gender, 3)

            # ایجاد نویسنده جدید
            author = Author.objects.create(
                user_made=request.user,
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_image=profile_image,
                username=username,
                national_id=national_code,
                date_birth=birthdate,
                mobile=phone,
                gender=gender_num,
                address=address,
                bio=biography,
                slug=slug or slugify(f"{first_name}-{last_name}")
            )

            return JsonResponse({
                "success": True,
                "message": 'نویسنده با موفقیت ثبت شد.',
                "data": {}
            }, status=200)

        except Exception as e:
            return JsonResponse({"success": False, "message": f'خطا در ثبت نام نویسنده: {str(e)}', "data": {}}, status=500)

    return redirect('master_author_list')