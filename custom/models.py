from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


   
class Achievements(models.Model):
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_en)

class Desc_Achievements(models.Model):
    link      = models.ForeignKey(Achievements , on_delete=models.CASCADE)
    title     = models.CharField(max_length=100)
    title_en  = models.CharField(max_length=100)
    desc      = RichTextField()
    desc_en   = RichTextField()

    def __str__(self):
        return str(self.title_en)

# Radio

class Radio(models.Model):
    image = models.ImageField(null=True , blank=True , upload_to='static/img/radio') 
    link  = models.URLField()

# Technology

  
class Technology(models.Model):
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_en)


class Technology_Desc(models.Model):
    link = models.ForeignKey(Technology , on_delete=models.CASCADE)
    image       = models.ImageField(null=True , blank=True , upload_to='static/img/tech')
    name        = models.CharField(max_length=100)
    name_en     = models.CharField(max_length=100)
    url         = models.URLField()
    url_two     = models.URLField()


# Cadres

class Cadres(models.Model):
    image   = models.ImageField(null=True , blank=True , upload_to='static/img/cadres')
    name    = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    job    = models.CharField(max_length=100)
    job_en = models.CharField(max_length=100)
    university    = models.CharField(max_length=100)
    university_en = models.CharField(max_length=100)
    bio     = RichTextField()
    bio_en  = RichTextField()
    link    = models.URLField()


class WelcomeScreen(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    desc = RichTextField()
    image = models.ImageField(null=True , blank=True , upload_to='static/img/welcome') 

class Media(models.Model):
    PrImage = models.ImageField(null=True , blank=True , upload_to='static/img/md')
    title   = models.CharField(max_length=200)
    title_en   = models.CharField(max_length=200)
    desc    = RichTextField()
    desc_en   = RichTextField()
    ScImage = models.ImageField(null=True , blank=True , upload_to='static/img/md')
    ScImage2 = models.ImageField(null=True , blank=True , upload_to='static/img/md')
    ScImage3 = models.ImageField(null=True , blank=True , upload_to='static/img/md')
    ScImage4 = models.ImageField(null=True , blank=True , upload_to='static/img/md')
    ScImage5 = models.ImageField(null=True , blank=True , upload_to='static/img/md')


    