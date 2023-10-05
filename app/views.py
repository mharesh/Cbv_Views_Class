from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import *
from app.forms import *
from app.forms import StudentForm

# Function Base View  for returning string
def fbv_string(request):
    return HttpResponse('This is fbv_string')

# Class Base View  for returning string
class Cbv_string(View):
    def get(self,request):
        return HttpResponse('This is cbv_string')

# rendering html page by using fbv   
def fbv_page(request):
    return render(request,'fbv_page.html')

# rendering html page by using cbv
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')

# insert data by using  FBV

def insert_by_fbv(request):
    SFO = StudentForm()
    d={'SFO':SFO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Inserted Data is Successfully..')
    return render(request,'insert_by_fbv.html',d)

# insert data by using CBV

class insert_by_cbv(View):
    def get(self,request):
        SFO = StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_by_cbv.html',d)
    
    def post(self,request):
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Inserted data CBV successfully....')
