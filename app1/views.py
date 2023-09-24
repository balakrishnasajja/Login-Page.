from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        # fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        # organization = request.POST.get('organization')

        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.info(request,"Your password and confrom password are not Same!")
            # return HttpResponse("Your password and confrom password are not Same!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            # my_user.first_name = fname
            # my_user.last_name = lname
            my_user.save()
            messages.info(request,'Account created successfully')
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, "You are successfully logged in.")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    messages.info(request,'You Logged out Successfuly')
    return redirect('signup')