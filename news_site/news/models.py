from __future__ import unicode_literals
from email.policy import default
from django.contrib.auth.models import  User , Permission
from django.db import models
import jdatetime




class Category(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="category")
    title=models.CharField(max_length=500)
    img=models.FileField(upload_to='img_category',blank=True)
    color=models.CharField(max_length=500, default='#f5f5f5')
    color_text=models.CharField(max_length=500, default='#000')

    def __str__(self):
            return f"{self.title}"


class SubCategory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcategory")
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    title=models.CharField(max_length=500)

    def __str__(self):
            return f"{self.title} | {self.category}"


SUBMINEWS=[
    (0,"در حال انتظار"),
    (1,"تایید شده"),
    (2,"رد شده"),
]
class News(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_author")
    sub_category=models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="news")
    title=models.CharField(max_length=500)
    img=models.FileField(upload_to='img_news',blank=True)
    date = models.FloatField(null=True , blank=True)
    text=models.TextField(null=True , blank=True)
    status_news = models.IntegerField(default=0, choices=SUBMINEWS)
    reject_reason = models.TextField(blank=True, null=True)

    def __str__(self):
            return f"{self.title} | {self.author} | {self.sub_category}"
    
    def save(self, *args, **kwargs):
        if not self.pk:  # اگر خبر جدید است
            if self.user.is_superuser:  # اگر کاربر ادمین اصلی است
                self.status_news = 1
            else:
                self.status_news = 0
        super().save(*args, **kwargs)
    

    @property
    def jdate(self):
        try:
            return  jdatetime.datetime.fromtimestamp(self.date).strftime("%Y/%m/%d")
        except:
            return '-'


class NewsLetters(models.Model):
    email=models.CharField(max_length=500)

    def __str__(self):
            return f"{self.email}"


class PointOfView(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="pointofview")
    news=models.ForeignKey(News, on_delete=models.CASCADE, related_name="pointofview")
    first_name_and_last_name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    date = models.FloatField(null=True , blank=True)
    text=models.TextField(null=True , blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
            return f"{self.first_name_and_last_name} | {self.email} | {self.text}"
    

    @property
    def jdate(self):
        try:
            return  jdatetime.datetime.fromtimestamp(self.date).strftime("%Y/%m/%d")
        except:
            return '-'

    def save(self, *args, **kwargs):
        if not self.pk: 
            if self.user.is_superuser:  # اگر کاربر ادمین اصلی است
                self.active = True
            else:
                self.active = False
        super().save(*args, **kwargs)
