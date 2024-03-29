# Generated by Django 3.2.8 on 2022-01-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/mediamodel'),
        ),
        migrations.AddField(
            model_name='research',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/research'),
        ),
        migrations.AddField(
            model_name='technology',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/technology'),
        ),
        migrations.AddField(
            model_name='youth',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/youth'),
        ),
    ]
