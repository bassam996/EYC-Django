from django.db import models
from ckeditor.fields import RichTextField



class Peace(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/peace')
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)



class Political_participation(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/political_participation') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)

   


class Women(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/women') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)




class Human_Rights(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/human_rights') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)

    


class Environment(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    desc  = RichTextField()
    desc_en  = RichTextField()
    image = models.ImageField(upload_to='static/img/environment') 
    slug = models.SlugField(max_length=100, unique=True , null=True , blank=True)

    

# End Carriers
