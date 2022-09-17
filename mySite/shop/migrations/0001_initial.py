# Generated by Django 4.1 on 2022-09-08 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Your name')),
                ('email', models.CharField(max_length=100, verbose_name='Your email')),
                ('account_id', models.TextField(max_length=250, verbose_name='Account ID')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.ImageField(upload_to='shop/account_images/%Y/%m/%d')),
                ('image_1', models.ImageField(upload_to='shop/account_images/%Y/%m/%d')),
                ('image_2', models.ImageField(upload_to='shop/account_images/%Y/%m/%d')),
                ('image_3', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Short description')),
                ('level', models.IntegerField()),
                ('full_acces', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=250)),
                ('vbucks', models.IntegerField()),
                ('bling_amount', models.IntegerField()),
                ('gliders_amount', models.IntegerField()),
                ('save_world', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=250)),
                ('hot_og', models.CharField(max_length=250)),
                ('mail', models.CharField(choices=[('Connected', 'Email in pack'), ('No email', 'No email'), ('Others', 'Other')], max_length=250, verbose_name='Type of email on account')),
                ('outfits', models.IntegerField()),
                ('emotions', models.IntegerField()),
                ('description', models.TextField(verbose_name='Full account description')),
                ('acc_raiting', models.CharField(default='5*', max_length=20)),
                ('acc_price', models.IntegerField(default=10)),
                ('date_post', models.DateTimeField(default=datetime.datetime(2022, 9, 8, 16, 20, 12, 729189))),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.accountplatform')),
            ],
            options={
                'ordering': ('-outfits',),
            },
        ),
    ]
