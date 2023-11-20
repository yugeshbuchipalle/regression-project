import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm,CreateTestsuiteForm
from .models import RegisterdUser,CreateTestsuite,Result
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.generic import ListView
import csv
from .forms import CSVUploadForm
import jenkins
import io
import random
import serializers
import ast
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
    registered_models = Result.objects.all()
    userdetails = {'username':usrnme,'registered_models': registered_models}
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
            # f = open("C:\\Users\\yuges\\PycharmProjects\\pythonProject4\\Regression\\IIS_APP\\jenkinsfile.txt", "r")
            # job_config = f.read().format(Testsuite, environment, email)
            f= open("C:\\Users\\yuges\\PycharmProjects\\regressiopn-project\\Regression\\IIS_APP\\pyjen.txt","r")
            job_config = f.read().format(jobname)


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
            results(jobname)
        return redirect("loggedin")

def results(jobname):
    server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
    time.sleep(5)
    latest_build_info = server.get_job_info(jobname)['lastBuild']['number']
    progress = server.get_build_info(jobname, latest_build_info)["inProgress"]
    print(progress)
    while (progress == True):
        progress = server.get_build_info(jobname, latest_build_info)["inProgress"]
        print(progress)
        print(server.get_build_info(jobname, latest_build_info)["id"])
    latest_build_number = server.get_job_info(jobname)['lastBuild']['number']
    result = server.get_build_test_report(jobname, latest_build_number)
    percentage = (result['passCount'] / (result['passCount'] + result['failCount'])) * 100
    print(percentage)
    l = []
    for i in result['suites'][0]['cases']:
        l.append([i['name'], i['status']])
    print(l)
    model_result = Result(jobname=jobname,passed=result['passCount'], failed=result['failCount'],percentage=percentage,result_list=str(l))
    model_result.save()
    result_info = {'model_result': model_result}
    # return render(request,"loggedin.html",user_info)

def resultpage(request):
    if request.method == 'POST':
        # Retrieve form data
        print(request.POST)
        jobname = request.POST.get('jobname')
        id = request.POST.get('id')
        print("jobname")
        print(jobname)
        print(id)
        resultdata = Result.objects.filter(id=id)
        print(ast.literal_eval(list(resultdata.values())[0]['result_list']))
        resultdata = ast.literal_eval(list(resultdata.values())[0]['result_list'])
    return render(request, "result.html",{'resultdata':resultdata})

def testresult(request):
    l=[]
    d = {}
    for i in Result.objects.all():
        l.extend(ast.literal_eval(i.result_list))
    for i in l:
        d1 = {'pass': 0, 'fail': 0, 'total': 0,'percentage':0}
        # print(d.items())
        if i[0] in d:
            if i[1] == "PASSED":
                # print("second time : "+ str(i[0]))
                d[i[0]]['pass'] = d[i[0]]['pass'] + 1
            elif i[1] == "FAILED":
                d[i[0]]['fail'] = d[i[0]]['pass'] + 1
        else:
            d[i[0]] = d1
            # print(d)
            if i[1] == "PASSED":
                d[i[0]]['pass'] = 1

            elif i[1] == "FAILED":
                d[i[0]]['fail'] = 1

            # elif i[1] == "FAILED":
            #     d1[i[0]]['fail'] = fail1 + 1
        d[i[0]]['total'] = d[i[0]]['total'] + 1
        d[i[0]]['percentage'] = (d[i[0]]['pass'] / d[i[0]]['total']) * 100
    return render(request, "testcases.html", {'resultdata': d})