# Generated by Django 3.2.8 on 2022-01-23 09:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_media_welcomescreen'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomescreen',
            name='desc',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadres',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='cadres',
            name='bio_en',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
