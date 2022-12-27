from django.shortcuts import render
from .forms import EmailForm
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    comments=ClientComment.objects.all()
    comm=ClientComment.objects.all().first()
    if request.method=="POST":
        review=request.POST.get('review')
        rate=request.POST.get('rating')
        ClientComment.objects.create(content=review,client = request.user,rating=rate)
    return render(request, 'base.html',{"comments": comments,"comm":comm})

def logoutUser(request):
    logout(request)
    return redirect('pressing:home')


def contact(request):
    ch=0
    if request.method=="POST":
        form=EmailForm(request.POST)
        if form.is_valid():
            ch=1    
            send_mail(form['subject'].value()+" from : "+form['your_email'].value(),
            form['content'].value(),
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER,],
            ) 
    form=EmailForm()
    return render(request,'contact.html',{"form":form,"ch":ch})


def clothes(request,ch):
    clothe=Lenge.objects.filter(caseoflenge=ch,author=request.user)
    size=1
    if len(clothe)==0 :
        size=0
    return render(request,'clothes.html',{"clothe":clothe,'ch':ch,'size':size})


def notif(request):
    notifs=NotifierClient.objects.filter(client=request.user)
    size=1
    if len(notifs)==0 :
        size=0
    return render(request,'notif.html',{"notifs":notifs,'size':size})
