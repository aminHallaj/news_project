# Generated by Django 5.0.6 on 2024-07-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_pointofview_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofview',
            name='date',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
