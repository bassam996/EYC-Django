# Generated by Django 3.2.8 on 2021-11-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counters',
            name='name',
            field=models.CharField(default='عدادات الصفحه الرئيسيه', max_length=50),
        ),
    ]
