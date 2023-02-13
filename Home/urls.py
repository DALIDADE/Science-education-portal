from django.contrib import admin
from django.urls import path,include
from .views import *


#########"SapaklarUrls"
urlpatterns = [
    path('',Index,name = 'index'),
    path('Ruby/',Ruby,name = 'ruby'),
    path('Python/',Python,name = 'python'),
    path('Go/',Go,name = 'go'),
    path('Node/',Node,name = 'node'),
    path('Css/',Css,name = 'css'),
    path('Django/',Django,name = 'django'),
    path('React/',React,name = 'react'),
    path('Html/',Html,name = 'html'),
    path('Java/',Java,name = 'java'),
    path('C/',C,name = 'c'),
    path('Csharp/',Csharp,name = 'csharp'),
    path('C_pluse/',C_pluse,name = 'c_pluse'),
    path('Flutter/',Flutter,name = 'flutter'),
    path('Javascript/',Javascript,name = 'javascript'),

]
