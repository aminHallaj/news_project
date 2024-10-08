from django.urls import path
from . import views

urlpatterns = [
    # Page Sign In
    path('master/signin/', views.master_signin, name='master_signin'),
    path('master/signin/submit/', views.master_signin_submit, name='master_signin_submit'),
    # End Page Sign In

    # Page Log Out
    path('master/logout/', views.master_logout, name='master_logout'),
    # End Page Log Out

    # Page Dashboard
    path('master/dashboard/', views.master_panel, name='master_panel'),
    # End Page Dashboard

    # Page Post List
    path('master/dashboard/post/list/', views.master_post_list, name='master_post_list'),
    path('master/dashboard/post/delete/<id>/', views.master_post_delete, name='master_post_delete'),
    # End Page Post List

    # Page Category Create And Category Edit
    path('master/dashboard/category/create/', views.master_category_create, name='master_category_create'),
    path('master/dashboard/category/create/submit/', views.master_category_create_submit, name='master_category_create_submit'),
    path('master/dashboard/category/edit/<id>/', views.master_category_edit, name='master_category_edit'),
    path('master/dashboard/category/edit/submit/<id>/', views.master_category_edit_submit, name='master_category_edit_submit'),
    path('master/dashboard/category/delete/<id>/', views.master_category_delete, name='master_category_delete'),
    # End Page Category Create And Category Edit

    # Page Sub Category Create And Sub Category Edit
    path('master/dashboard/sub/category/create/submit/', views.master_sub_category_create_submit, name='master_sub_category_create_submit'),
    path('master/dashboard/sub/category/edit/<id>/', views.master_sub_category_edit, name='master_sub_category_edit'),
    path('master/dashboard/sub/category/edit/submit/<id>/', views.master_sub_category_edit_submit, name='master_sub_category_edit_submit'),
    path('master/dashboard/sub/category/delete/<id>/', views.master_sub_category_delete, name='master_sub_category_delete'),
    # End Page Sub Category Create And Sub Category Edit

    # Page Post Create And Post Edit
    path('master/dashboard/post/create/', views.master_post_create, name='master_post_create'),
    path('master/dashboard/post/create/submit/', views.master_post_create_submit, name='master_post_create_submit'),
    path('master/dashboard/post/edit/<id>/', views.master_post_edit, name='master_post_edit'),
    path('master/dashboard/post/edit/submit/<id>/', views.master_post_edit_submit, name='master_post_edit_submit'),
    path('master/dashboard/post/change-status/<id>/', views.master_change_news_status, name='master_change_news_status'),
    path('master/dashboard/post/resubmit/<id>/', views.master_resubmit_news, name='master_resubmit_news'),
    # End Page Post Create And Post Edit

    # Page reviews Create And reviews Edit
    path('master/dashboard/reviews/', views.master_reviews, name='master_reviews'),
    path('master/dashboard/toggle-review-active/', views.master_toggle_review_active, name='master_toggle_review_active'),
    path('master/dashboard/reviews/edit/submit/<id>/', views.master_reviews_edit_submit, name='master_reviews_edit_submit'),
    path('master/dashboard/reviews/delete/<id>/', views.master_reviews_delete, name='master_reviews_delete'),
    # End Page Post Create And Post Edit

    # Page author Create And author Edit
    path('master/dashboard/author/list/', views.master_author_list, name='master_author_list'),
    path('master/dashboard/author/create/submit/', views.master_author_create_submit, name='master_author_create_submit'),
    path('master/dashboard/author/change-status/<id>/', views.master_change_author_status, name='master_change_author_status'),
    path('master/dashboard/author/change-resubmit/<id>/', views.master_resubmit_author, name='master_resubmit_author'),
    path('master/dashboard/toggle_author_active/', views.master_toggle_author_active, name='master_toggle_author_active'),
    # End Page Post Create And Post Edit

]