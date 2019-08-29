from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.ChartData.as_view(), name='index'),
    path('data', views.statsData.as_view(), name='data'),
    #url(r'^$', HomeView.as_view(), name='home'),
    #path('stat/', StatView.as_view(), name='stat'),
]
