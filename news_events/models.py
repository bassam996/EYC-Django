from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.



class News(models.Model):
    title      = models.CharField(max_length=50)
    title_en   = models.CharField(max_length=50)
    desc       = RichTextField()
    desc_en    = RichTextField()
    date       = models.DateTimeField(null=True , blank=True)
    image      = models.ImageField(null=True , blank=True , upload_to='static/img/news') 

    def __str__(self):
        return str(self.title)
