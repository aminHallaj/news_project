# Generated by Django 5.0.6 on 2024-07-07 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_pointofview_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletters',
            name='user',
        ),
    ]
