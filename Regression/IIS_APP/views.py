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
            # decoded_file = csv_file.read().decode('utf-8')
            # io_string = io.StringIO(decoded_file)
            # csv_reader = csv.reader(io_string)
            # csv_reader['Assigned To']
            # for row in csv_reader:
            #     # Process each row
            #     print(row.re)
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
            emailid = request.POST.get('emailid')
            Testsuite = request.POST.get('Testsuite')
            environment = request.POST.get('envirionment')
            job_config = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <authToken>1234</authToken>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <com.katalon.jenkins.plugin.ExecuteKatalonStudioTask plugin="katalon@1.0.34">
      <version>8.6.6</version>
      <location></location>
      <executeArgs>-projectPath=&quot;C:\\Users\\yuges\\Katalon Studio\\FT1\\FT1.prj&quot; -retry=0 -testSuitePath=&quot;Test Suites/{0}&quot; -browserType=&quot;Chrome&quot; -executionProfile=&quot;{1}&quot; -apiKey=&quot;5f791d0c-405a-4379-9031-05160a22f82e&quot; --config -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY -proxy.system.applyToDesiredCapabilities=true</executeArgs>
      <x11Display></x11Display>
      <xvfbConfiguration></xvfbConfiguration>
    </com.katalon.jenkins.plugin.ExecuteKatalonStudioTask>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>""".format(Testsuite, environment)

            JENKINS_URL = "http://localhost:8080/"
            JENKINS_USERNAME = "yugeshbuchipalle"
            JENKINS_PASSWORD = "Vijaya@238a"
            server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
            server.create_job(jobname, job_config)
            PARAMETERS = {}
            TOKEN_NAME = "1234"
            server.build_job(jobname, PARAMETERS, TOKEN_NAME)
            userdetails = [jobname,emailid,Testsuite]
        return render(request, "katalondata.html", {'userdetails': userdetails})

    #     try:
    #         user = RegisterdUser.objects.get(name=usrnme)
    #         if usrnme == user.name and psswrd == user.password:
    #             return redirect("loggedin")
    #         else:
    #             messages.info(request, "Incorrect password")
    #             return redirect("signin")
    #     except ObjectDoesNotExist:
    #         messages.info(request, "The user does not exist")
    #         return redirect("signin")
    #
    # else:
    #     return render(request, "signin.html")
