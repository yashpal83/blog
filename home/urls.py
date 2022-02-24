from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('usersignup', views.usersignup, name = "usersignup"),
    path('userlogin', views.userlogin, name = "userlogin"),
    path('userlogout', views.userlogout, name = "userlogout"),
    path('search', views.search, name = "search")
]