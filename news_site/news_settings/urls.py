from django.contrib import admin
from django.urls import path , include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('',include('master.urls')),
    path('',include('customer.urls')),
    path('',include('settings_site.urls')),
]

urlpatterns+=[
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]
