from django.shortcuts import render
from .models import *

def Index(request):
    return render(request,'index.html')


####################"SapaklarView"
def Ruby(request):
    A1 = RubyModel.objects.all()
    return render(request,'button/ruby.html',{'A1':A1})

def Python(request):
    A2 = PythonModel.objects.all()
    return render(request,'button/python.html',{'A2':A2})

def Go(request):
    A3 = GoModel.objects.all()
    return render(request,'button/go.html',{'A3':A3})

def Node(request):
    A4 = NodeModel .objects.all()
    return render(request,'button/node.html',{'A4':A4})

def Css(request):
    A5 = CssModel.objects.all()
    return render(request,'button/css.html',{'A5':A5})

def Django(request):
    A6 = DjangoModel.objects.all()
    return render(request,'button/django.html',{'A6':A6})

def React(request):
    A7 = ReactModel.objects.all()
    return render(request,'button/react.html',{'A7':A7})

def Html(request):
    A8 = HtmlModel.objects.all()
    return render(request,'button/html.html',{'A8':A8})

def Java(request):
    A9 =JavaModel.objects.all()
    return render(request,'button/java.html',{'A9':A9})

def C(request):
    A10 = CModel.objects.all()
    return render(request,'button/c.html',{'A10':A10})

def Csharp(request):
    A11 = CsharpModel.objects.all()
    return render(request,'button/csharp.html',{'A11':A11})

def C_pluse(request):
    A12 = C_pluseModel.objects.all()
    return render(request,'button/c++.html',{'A12':A12})

def Flutter(request):
    A13 = FlutterModel.objects.all()
    return render(request,'button/flutter.html',{'A13':A13})

def Javascript(request):
    A14 = JavascriptModel.objects.all()
    return render(request,'button/javascript.html',{'A14':A14})

