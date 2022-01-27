from django.shortcuts import redirect, render
from .models import Board , Branches , Switch_V_Form , Partnerships
from .forms import VolunteeringForm , ContactForm
from django.contrib import messages

# def volunteering

def volunteering(request):
    if request.method == "POST":
      v_form = VolunteeringForm(request.POST)
      if v_form.is_valid():
          v_form.save()
          messages.add_message(request, messages.INFO, "تم إستقبال البيانات بنجاح | The data has been received successfully")
          return redirect('/volunteering/')

    else :
        v_form = VolunteeringForm()
    
    context = {'volunteering' : v_form }
    return render(request , 'volunteering.html' , context )

# def contact 

def contact(request):
    if request.method =="POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.add_message(request, messages.INFO, "تم إستقبال رسالتك بنجاح | Your Message has been received successfully")
            return redirect('/contact-us/')
        else :
            contactform = ContactForm()
            
    context = {'contact' : ContactForm }
    return render(request , 'contact.html' , context )

# partner def

def ourParteners(request):
    partnership = Partnerships.objects.all()
    context     = {'partner' : partnership}
    return render(request , 'ourParteners.html' , context)

# board def

def board(request):
    board   = Board.objects.all()
    context = {'board' : board }
    return render(request , 'board.html' , context )

# branches def

def branches(request):
    branches = Branches.objects.all()
    context  = {'branches' : branches }
    return render(request , 'branches.html' , context )