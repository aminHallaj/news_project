# Generated by Django 5.0.6 on 2024-07-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_newsletters_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='coler_text',
            field=models.CharField(default='#1', max_length=500),
            preserve_default=False,
        ),
    ]
