# Generated by Django 3.2.8 on 2022-01-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eycmedia', '0003_auto_20220113_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotosCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/photoscenter')),
            ],
        ),
    ]
