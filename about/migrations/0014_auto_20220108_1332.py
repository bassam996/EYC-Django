# Generated by Django 3.2.8 on 2022-01-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_partnerships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='board',
            name='title',
        ),
        migrations.RemoveField(
            model_name='board',
            name='title_en',
        ),
        migrations.AddField(
            model_name='board',
            name='desc_job',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(default=1, upload_to='static/img/board'),
            preserve_default=False,
        ),
    ]
