# Generated by Django 3.2.8 on 2021-12-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Youth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
    ]