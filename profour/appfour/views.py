from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def index(request):
    context_dict = {'text':'hello vivek', 'number':100}
    return render(request,'appfour/index.html',context_dict)

def relative(request):
    return render(request,'appfour/relative_url_temp.html')

def other(request):
    return render(request,'appfour/other.html')