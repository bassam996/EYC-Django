# Generated by Django 3.2.8 on 2021-12-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_branches_branch_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.CharField(max_length=50)),
                ('v_phone', models.IntegerField()),
                ('v_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
