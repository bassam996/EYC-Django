# Generated by Django 3.2.8 on 2021-11-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.CharField(max_length=10)),
                ('courses', models.CharField(max_length=10)),
                ('Followers', models.CharField(max_length=10)),
                ('events', models.CharField(max_length=10)),
            ],
        ),
    ]
