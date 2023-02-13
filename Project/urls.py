from django.urls import path,include
from .views import *

#########"ProjectUrls"
urlpatterns = [
    path('Ruby_Project/',Ruby,name = 'ruby_project'),
    path('Python_Project/',Python,name = 'python_project'),
    path('Go_Project/',Go,name = 'go_project'),
    path('Node_Project/',Node,name = 'node_project'),
    path('Css_Project/',Css,name = 'css_project'),
    path('Django_Project/',Django,name = 'django_project'),
    path('React_Project/',React,name = 'react_project'),
    path('Html_Project/',Html,name = 'html_project'),
    path('Java_Project/',Java,name = 'java_project'),
    path('C_Project/',C,name = 'c_project'),
    path('C_sharp_Project/',Csharp,name = 'csharp_project'),
    path('C_pluse_Project/',C_pluse,name = 'c_pluse_project'),
    path('Flutter_Project/',Flutter,name = 'flutter_project'),
    path('Javascript_Project/',Javascript,name = 'javascript_project'),

]
