from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Welcome Home page")
