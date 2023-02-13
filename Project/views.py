from django.shortcuts import render
from .models import *


def Ruby(request):
    B1 = RubyProjectModel.objects.all()
    return render(request,'project/ruby_project.html',{'B1':B1})

def Python(request):
    B2 = PythonProjectModel.objects.all()
    return render(request,'project/python_project.html',{'B2':B2})

def Go(request):
    B3 = GoProjectModel.objects.all()
    return render(request,'project/go_project.html',{'B3':B3})

def Node(request):
    B4 = NodeProjectModel .objects.all()
    return render(request,'project/node_project.html',{'B4':B4})

def Css(request):
    B5 = CssProjectModel.objects.all()
    return render(request,'project/css_project.html',{'B5':B5})

def Django(request):
    B6 = DjangoProjectModel.objects.all()
    return render(request,'project/django_project.html',{'B6':B6})

def React(request):
    B7 = ReactProjectModel.objects.all()
    return render(request,'project/react_project.html',{'B7':B7})

def Html(request):
    B8 = HtmlProjectModel.objects.all()
    return render(request,'project/html_project.html',{'B8':B8})

def Java(request):
    B9 =JavaProjectModel.objects.all()
    return render(request,'project/java_project.html',{'B9':B9})

def C(request):
    B10 = CProjectModel.objects.all()
    return render(request,'project/c_project.html',{'B10':B10})

def Csharp(request):
    B11 = CsharpProjectModel.objects.all()
    return render(request,'project/csharp_project.html',{'B11':B11})

def C_pluse(request):
    B12 = C_pluseProjectModel.objects.all()
    return render(request,'project/c++_project.html',{'B12':B12})

def Flutter(request):
    B13 = FlutterProjectModel.objects.all()
    return render(request,'project/flutter_project.html',{'B13':B13})

def Javascript(request):
    B14 = JavascriptProjectModel.objects.all()
    return render(request,'project/javascript_project.html',{'B14':B14})


# Create your views here.
