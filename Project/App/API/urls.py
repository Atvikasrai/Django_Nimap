from django.contrib import admin
from django.urls import include, path
from .import views

#----------------------------------------------------------------------------------------

urlpatterns = [

    path('clients/', views.clients, name='clients'),

    path('clients/<int:pk>/', views.clientsdetail, name='clientdetail'),

    path('projects/', views.allproject, name='allproject'),

    path('projects/<int:pk>/', views.projectdetails, name='projectdetails'),

    path('myprojects/', views.gotproject, name = 'gotproject'),

]