from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('dbsearch', views.dbsearch , name='dbsearch'),
    path('qaapp', views.QAapp , name='QAapp'),
    path('sentapp', views.sentapp , name='sentapp'),
    path('textgen', views.textgen , name='textgen'),
    # path('upload_file', views.upload_file , name='upload_file'),
]
