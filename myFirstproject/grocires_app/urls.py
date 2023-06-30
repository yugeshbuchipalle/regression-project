from . import views
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.app_homepage, name='app_homepage'),
    path('page1', views.app_homepage1, name='app_homepage1'),
    path('page2', views.app_homepage2, name='app_homepage2'),
    path('base', views.app_homepage3, name='app_homepage3'),
    path('ft1_testcases', views.ft1_testcases, name='ft1_testcases'),
    path('register',views.register,name="register"),
    path('about_us', views.about_us, name="about_us"),
    path('services', views.services, name="services"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('register', views.register, name="register"),
    path('signin', views.signin, name='signin'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name="logout")
]