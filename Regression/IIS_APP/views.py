from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm,CreateTestsuiteForm
from .models import RegisterdUser,CreateTestsuite
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.generic import ListView
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

def job(request):
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
    return render(request, "about_us.html")


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
        # return render(request, "register.html", user_info)
    registered_models = CreateTestsuite.objects.all()
    return render(request, 'register.html', {'form': form, 'registered_models': registered_models})


def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST.get('username')
        psswrd = request.POST.get('pswd')


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
    global usrnme
    userdetails = {'username':usrnme}
    return render(request,"project.html",userdetails)

def hoursupload(request):
    return render(request,"csv_uploader.html")

def logout(request):
    global usrnme
    del usrnme
    return render(request,"logout.html")


def createtestsuite(request):
    global usrnme
    if request.method == "POST":
        form = CreateTestsuiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"job added")
            registered_models = CreateTestsuite.objects.all()
            user_info = {'form': form, 'registered_models': registered_models}
            return render(request, "createjob.html", user_info)
            # return redirect("userList")
    else:
        form = CreateTestsuiteForm()
        registered_models = CreateTestsuite.objects.all()
        user_info = {'form':form, 'registered_models': registered_models}
        return render(request,"createjob.html",user_info)

class userList(ListView):
    model = CreateTestsuite
    template_name = "user_data.html"
    context_object_name = "alldata"
