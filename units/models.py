from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Research(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/research')
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)



class Media(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/mediamodel') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)



class Youth(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/youth') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)



class Technology(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/technology')
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)

