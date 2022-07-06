from cProfile import Profile
from email import message
from django.shortcuts import redirect, render
from .models import Profile
from django.core.checks import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'Login.html')

def create_profile(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        image=request.FILES['image']
        user=User.objects.create_user(username=username,password=password)
        profile= Profile.objects.create(user=user,profile_picture=image)
        if profile:
            messages.success(request, 'Profile Created Please Login')
            return redirect("Login")
    return render(request,'SignUp.html')

def profile(request):
    
    return render(request,'profile.html')

