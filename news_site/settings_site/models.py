from __future__ import unicode_literals
from email.policy import default
from django.contrib.auth.models import  User , Permission
from django.db import models

class Settings(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="settings")
    tab_name=models.CharField(max_length=200)
    name_site=models.CharField(max_length=200)
    telegram_url=models.CharField(max_length=200)
    instagram_url=models.CharField(max_length=200)
    whatsapp_url=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    copy_right=models.CharField(max_length=200)
    number=models.IntegerField()
    logo_favicon=models.FileField(upload_to='logo_favicon',blank=True)
    logo_header=models.FileField(upload_to='logo_header',blank=True)
    logo_header_dark=models.FileField(upload_to='logo_header_dark',blank=True)
    logo_header_menu=models.FileField(upload_to='logo_header_menu',blank=True)
    logo_header_menu_dark=models.FileField(upload_to='logo_header_menu_dark',blank=True)
    logo_footer=models.FileField(upload_to='logo_footer',blank=True)
    site_title=models.TextField(null=True , blank=True)
    footer_title=models.TextField(null=True , blank=True)
    about_us=models.TextField(null=True , blank=True)
    address=models.TextField(null=True , blank=True)

    def __str__(self):
            return f"{self.name_site} | {self.pk}"
    


class ContactUsSettings(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="contactussettings")
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    number=models.IntegerField()
    hours_of_work=models.TextField(null=True , blank=True)    

    def __str__(self):
            return f"{self.title}"
    

class ContactUs(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="contactus")
    first_name_and_last_name=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    text=models.TextField(null=True , blank=True)    

    def __str__(self):
            return f"{self.title}"