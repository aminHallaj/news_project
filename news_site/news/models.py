from __future__ import unicode_literals
from email.policy import default
from django.contrib.auth.models import  User , Permission
from django.db import models
import jdatetime




class Category(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="category")
    title=models.CharField(max_length=500)
    img=models.FileField(upload_to='img_category',blank=True)
    coler=models.CharField(max_length=500)

    def __str__(self):
            return f"{self.title}"


class SubCategory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcategory")
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    title=models.CharField(max_length=500)

    def __str__(self):
            return f"{self.title} | {self.category}"



class News(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_author")
    sub_category=models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="news")
    title=models.CharField(max_length=500)
    img=models.FileField(upload_to='img_news',blank=True)
    date = models.FloatField(null=True , blank=True)
    text=models.TextField(null=True , blank=True)

    def __str__(self):
            return f"{self.title} | {self.author} | {self.sub_category}"
    

    @property
    def jdate(self):
        try:
            return  jdatetime.datetime.fromtimestamp(self.date).strftime("%Y/%m/%d")
        except:
            return '-'


class NewsLetters(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="newsletters")
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

    def __str__(self):
            return f"{self.first_name_and_last_name} | {self.email} | {self.text}"
    

    @property
    def jdate(self):
        try:
            return  jdatetime.datetime.fromtimestamp(self.date).strftime("%Y/%m/%d")
        except:
            return '-'

