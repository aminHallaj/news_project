from __future__ import unicode_literals
from email.policy import default
from django.contrib.auth.models import  User , Permission
from django.db import models
import jdatetime
from django.core.validators import RegexValidator
from django.utils.text import slugify


GENDER=[
    (0,"جنسیت"),
    (1,"مرد"),
    (2,"زن"),
    (3,"سایر"),
]

mobile_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره موبایل باید در فرمت صحیح وارد شود.")
national_id_validator = RegexValidator(regex=r'^\d{10}$', message="کد ملی باید 10 رقم باشد.")

class Author(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(null=True, blank=True)
    profile_image= models.ImageField(upload_to='author_profiles/', blank=True, null=True)
    username= models.CharField(max_length=150, unique=True)
    national_id= models.CharField(max_length=10, unique=True, validators=[national_id_validator])
    date_birth= models.DateField(null=True, blank=True)
    mobile= models.CharField(max_length=15, blank=True, null=True, validators=[mobile_validator])
    gender= models.SmallIntegerField(default=0 , choices=GENDER)
    is_active= models.BooleanField(default=False)
    address= models.TextField(null=True , blank=True)
    bio= models.TextField(null=True, blank=True)
    slug= models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args, **kwargs)
        # Update corresponding User fields
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.email = self.email
        self.user.profile_image = self.profile_image
        self.user.username = self.username
        self.user.save()

    @property
    def jdate_birth(self):
        try:
            return  jdatetime.datetime.fromtimestamp(self.date_birth).strftime("%Y/%m/%d")
        except:
            return '-'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
            return f"{self.get_full_name()} | {self.username} | {self.national_id}"
