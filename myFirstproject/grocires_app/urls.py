from . import views
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.app_homepage, name='app_homepage'),
    path('page1', views.app_homepage1, name='app_homepage1'),
    path('page2', views.app_homepage2, name='app_homepage2'),
    path('ft1_testcases', views.ft1_testcases, name='ft1_testcases')
]