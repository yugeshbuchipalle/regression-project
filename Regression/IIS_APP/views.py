from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm,CreateTestsuiteForm
from .models import RegisterdUser,CreateTestsuite
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.generic import ListView
import csv
from .forms import CSVUploadForm
import jenkins
import io
# def app_homepage(request):
#     return render(request, 'project.html')
JENKINS_URL = "http://localhost:8080/"
JENKINS_USERNAME = "yugeshbuchipalle"
JENKINS_PASSWORD = "Vijaya@238a"
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

usrnme =""
def signin(request):
    # global usrnme
    print(request.POST)
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
        print("form")
        print(type(form))
        jobname = form.data['jobname']
        Testsuite = form.data['Testsuite']
        environment = form.data['envirionment']
        email = form.data['emailid']
        existing_jobs= [i.jobname for i in CreateTestsuite.objects.all()]
        print(existing_jobs)
        if form.is_valid() and form.data['jobname'] not in existing_jobs:
            form.save()
            messages.success(request,"job added")
            f = open("C:\\Users\\yuges\\PycharmProjects\\pythonProject4\\Regression\\IIS_APP\\jenkinsfile.txt", "r")
            job_config = f.read().format(Testsuite, environment,email)

            server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
            server.create_job(jobname, job_config)
        else:
            messages.info(request,"job name already exists")
        registered_models = CreateTestsuite.objects.all()
        user_info = {'form': form, 'registered_models': registered_models}
        return render(request, "createjob.html", user_info)
    else:
        form = CreateTestsuiteForm()
        registered_models = CreateTestsuite.objects.all()
        user_info = {'form':form, 'registered_models': registered_models}
        return render(request,"createjob.html",user_info)

class userList(ListView):
    model = CreateTestsuite
    template_name = "user_data.html"
    context_object_name = "alldata"



import pandas as pd
import calendar
from datetime import datetime
def upload_csv(request):
    datem = datetime.today().strftime("%Y-%m")
    yearmonth = datem.split('-')
    month_count = calendar.monthrange(int(yearmonth[0]), int(yearmonth[1]))[1]
    count = 0
    for day in range(1, month_count + 1):
        presentday = datetime(int(yearmonth[0]), int(yearmonth[1]), day)
        if presentday.strftime('%A') not in ["Saturday", "Sunday"]:
            count = count + 1

    completed_in_a_month = count * 9
    print("Hours completed in a month " + str(completed_in_a_month))
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            df1=pd.read_csv(csv_file)
            df2 = df1.fillna(0)
            print(df2)
            d = {}
            for i, j in zip(list(df2['Assigned To']), list(df2['Completed Work'])):
                if i in d:
                    d[i] = d[i] + j
                else:
                    d[i] = j
            for i in d:
                l = []
                d[i] = [completed_in_a_month, d[i], completed_in_a_month - d[i]]
            userdetails = d
            return render(request, "hours.html", {'userdetails': userdetails})
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def trigger(request):
        if request.method == 'POST':
            # Retrieve form data
            print(request.POST)
            jobname = request.POST.get('jobname')
            print("jobname")
            print(jobname)
            server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
            PARAMETERS = {}
            TOKEN_NAME = "1234"
            server.build_job(jobname, PARAMETERS, TOKEN_NAME)
        return redirect("loggedin")


