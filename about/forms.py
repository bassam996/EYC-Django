from django import forms
from .models import Volunteering , Contact

class VolunteeringForm(forms.ModelForm):
    class Meta :
        model  = Volunteering
        fields = ['name' , 'phone' , 'email' , 'national_id' , 'address']
        labels = {
            'name'  : ('Name | الأسم'),
            'phone' : ('Phone | الهاتف'),
            'email' : ('Email | البريد الإلكتروني'),
            'national_id' : ('National ID | الرقم القومي'),
            'address' : ('Address | العنوان'),
        }

class ContactForm(forms.ModelForm):
    class Meta :
        model  = Contact
        fields = ['name' , 'phone' , 'email' , 'message']
        labels = {
            'name' : ('Full Name | اسمك كامل'),
            'phone' : ('Your Phone | رقم هاتفك'),
            'email' : ('Your Email | بريدك الإلكتروني'),
            'message' : ('Your Message | رسالتك')
        }
    