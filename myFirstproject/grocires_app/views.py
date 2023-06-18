from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app_homepage(request):
    return render(request, 'project.html')

def app_homepage1(request):
    return render(request, 'job.html')

def app_homepage2(request):
    return render(request, 'testsuite.html')

def ft1_testcases(request):
    return render(request, 'FT1 testcases.html')
