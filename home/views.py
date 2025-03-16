import os
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from .models import Meme
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def LandingPage(request):
    return render(request,'landingpage.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)

        if user is None:
            return render(request,'login.html',{'error':'Invalid Credentitals !'}) 
        else :
            login(request,user)
            return redirect('home')

    return render(request,'login.html')

def Signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstName')
        last_name=request.POST.get('lastName')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')

        if pass1!=pass2:
            return render(request,'signup.html',{'error':'passwords do not match !'})
        
        if User.objects.filter(email=email).exists():
            return render(request,'signup.html',{'error':'Email already Exits !'})
        
        if User.objects.filter(username=username).exists():
            return render(request,'signup.html',{'error':'Username alreadt Exists !'})

        try :
            user=User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
            user.set_password(pass1)
            user.save()
            return redirect('login')
        
        except IntegrityError:
            return render(request,'signup.html',{'error':'Something went wrong ! Please try again later...'})

    return render(request,'signup.html')

@login_required(login_url='login')
def home(request):
    memes = Meme.objects.all().order_by('-id')  
    return render(request, 'home.html', {'memes': memes,'Title':'Meme by Bhavesh Kale'})
    
@login_required(login_url='login')
def delete_meme(request,memeid):
    meme=Meme.objects.get(id=memeid)
    meme.delete()
    return redirect ('home')

@login_required(login_url='login')
def add_meme(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        Meme.objects.create(title=title, image=image)

        return redirect('home')   
    return redirect('home.html')

@login_required(login_url='login')
def update_meme(request,memeid):
    meme=get_object_or_404(Meme,id=memeid)

    if request.method=='POST':

        new_title=request.POST.get('title')
        new_image=request.FILES.get('image')
        
        if new_image:
            old_image_path = os.path.join(settings.MEDIA_ROOT, str(meme.image))

            if os.path.exists(old_image_path):
                os.remove(old_image_path)
            
            meme.image=new_image
        
        meme.title=new_title
        meme.save()
        return redirect('home')
    
    return render(request,'update_meme.html',{'meme':meme})

@login_required(login_url='login')
def Logout_view(request):
    logout(request)
    return redirect('login')






