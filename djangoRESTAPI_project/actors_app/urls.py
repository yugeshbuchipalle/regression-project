from . import views
from django.urls import path

urlpatterns = [path('',views.ActorsList.as_view()),]