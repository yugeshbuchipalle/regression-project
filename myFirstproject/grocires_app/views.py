from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import RegisterdUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# def app_homepage(request):
#     return render(request, 'project.html')
def app_homepage(request):
     return render(request, 'homepage.html')


def app_homepage1(request):
    return render(request, 'job.html')

def app_homepage2(request):
    return render(request, 'testsuite.html')
def app_homepage3(request):
    return render(request, 'base.html')

def ft1_testcases(request):
    return render(request, 'FT1 testcases.html')


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successful")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form':form}
        return render(request,"register.html",user_info)
def about_us(request):
    return render(request, "aboutUs.html")


def services(request):
    return render(request, "services.html")


def contact_us(request):
    return render(request, "contactUs.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)



def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']

        try:
            user = RegisterdUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            else:
                messages.info(request, "Incorrect password")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "The user does not exist")
            return redirect("signin")

    else:
        return render(request, "signin.html")

def loggedin(request):
    userdetails = {'username':usrnme}
    return render(request,"project.html",userdetails)



def logout(request):
    global usrnme
    del usrnme
    return render(request,"logout.html")