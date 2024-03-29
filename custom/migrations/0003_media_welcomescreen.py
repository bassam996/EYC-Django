# Generated by Django 3.2.8 on 2022-01-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_cadres_radio_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrImage', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('ScImage', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
                ('ScImage2', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
                ('ScImage3', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
                ('ScImage4', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
                ('ScImage5', models.ImageField(blank=True, null=True, upload_to='static/img/md')),
            ],
        ),
        migrations.CreateModel(
            name='WelcomeScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/welcome')),
            ],
        ),
    ]
