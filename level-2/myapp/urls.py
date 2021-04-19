from django.contrib import admin
from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns =[
    path('', views.home, name = 'home'),
    # path('azwad/', views.azwad, name = 'azwad'),
    path('form/', views.form, name = "form"),

]