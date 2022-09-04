# Generated by Django 4.1 on 2022-09-04 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_userorder_alter_account_date_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_post',
            field=models.DateField(default=datetime.datetime(2022, 9, 4, 16, 27, 50, 556019)),
        ),
        migrations.AlterField(
            model_name='account',
            name='image_1',
            field=models.ImageField(upload_to='shop/account_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='account',
            name='image_2',
            field=models.ImageField(upload_to='shop/account_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='account',
            name='title_image',
            field=models.ImageField(upload_to='shop/account_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='account_id',
            field=models.TextField(max_length=250, verbose_name='Account ID'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Your email'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Your name'),
        ),
    ]
