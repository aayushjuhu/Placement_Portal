from django.contrib import admin
from django.urls import path,include
from papp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('placements', views.placements, name='placements'),
    path('higherstudies', views.higherstudies, name='higherstudies'),
    path('entre', views.entre, name='entre'),
    path('totalstuds', views.totalstuds, name='totalstuds'),
    path('logoutuser', views.logoutuser, name='logoutuser')

]