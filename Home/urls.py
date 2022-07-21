from django.contrib import admin
from django.urls import path
from Home import views 
urlpatterns = [
    path('', views.index,name='Home'),

    # path('about', views.about,name='about'),

    path('competitions', views.competitions,name='competitions'),  

    path('contact', views.contact,name='contact'),

    path('Home',views.Home,name='Home'),  

    path('Competitions',views.competitions,name='Comeptitions'),

    path('profile',views.profile,name ='profile'),

    # path('journal',views.journal,name='journal'),

    path('about',views.about,name='about')

]   