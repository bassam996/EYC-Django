from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError



# Create your models here.

class Board(models.Model):
    name          = models.CharField(max_length=50)
    name_en       = models.CharField(max_length=50 , null= True , blank= True)
    job_title     = models.CharField(max_length=50)
    job_title_en  = models.CharField(max_length=50 , null= True , blank= True)
    image         = models.ImageField(null=True , blank=True , upload_to='static/img/board')
    
    def __str__(self):
        return str(self.name)




class Branches(models.Model):
    branch_name       = models.CharField(max_length=50)
    branch_name_en    = models.CharField(max_length=50 , null= True , blank= True)
    branch_address    = models.CharField(max_length=500)
    branch_address_en = models.CharField(max_length=500 , null= True , blank= True)
    branch_on_map     = models.URLField()
    branch_image      = models.ImageField(null=True , blank=True , upload_to='static/img/')

    def __str__(self):
        return str(self.branch_name)


class Switch_V_Form(models.Model):
    active  = models.BooleanField(default=True)


# Volunteering def class

def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('ID must contain Numbers Only | الرقم القومي يجب أن يحتوي على أرقام فقط')

class Volunteering(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    national_id = models.CharField(max_length = 14 , validators=[only_int])
    address = models.CharField(max_length=200)


    def __str__(self):
        return str(self.national_id)

# End Volunteering Class


class Contact(models.Model):
    name     = models.CharField(max_length=70)
    phone    = models.IntegerField()
    email    = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.phone)



class Partnerships(models.Model):
    partner_name             = models.CharField(max_length=200)
    partner_name_en          = models.CharField(max_length=200)
    partner_bio              = RichTextField()
    partner_bio_en           = RichTextField()
    communication_officer    = models.CharField(max_length=50)
    communication_officer_en = models.CharField(max_length=50)
    partner_image = models.ImageField(null=True , blank=True , upload_to='static/img/partner')
    url = models.URLField()

 
