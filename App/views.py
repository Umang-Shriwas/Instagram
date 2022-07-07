from cProfile import Profile
from email import message
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('pr')
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
    profile=Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile,'profile_user':True})

def Logout(request):
    logout(request)
    return redirect("Login")

def search(request):
    search=request.GET['username']
    profiles=Profile.objects.filter(user__username__icontains=search)
    context={'profiles':profiles}
    return render(request,'search.html',context)