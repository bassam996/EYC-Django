# Generated by Django 3.2.8 on 2021-11-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('branch_address', models.CharField(max_length=500)),
                ('branch_on_map', models.URLField()),
            ],
        ),
    ]
