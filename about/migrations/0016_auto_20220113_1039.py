# Generated by Django 3.2.8 on 2022-01-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_auto_20220108_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerships',
            name='communication_officer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerships',
            name='communication_officer_en',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerships',
            name='partner_bio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerships',
            name='partner_bio_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerships',
            name='partner_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/partner'),
        ),
    ]
