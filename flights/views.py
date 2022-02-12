import code
from distutils.log import info
from django.http import HttpResponse
from django.shortcuts import render
from .models import flights,airport
from django.http import HttpResponse

# Create your views here.
def all_flights (request):
    Flights=flights.objects.filter().all()
    return render(request,"flights/all_flights.html",{"flights":Flights})

def one(request,id):
    detail = flights.objects.filter(id=id).first()
    if detail==None:
        return HttpResponse("Flight not Available, Check later!")
    return render(request,"flights/flight.html",{"detail":detail})


def time(request,id):
    duration= flights.objects.filter(id=id).first()
    return render(request,"flights/dura.html",{"duration":duration})

#Making a form from anexisting model
from django import forms           
class addflight(forms.ModelForm):
    class Meta:
        model=flights
        fields=["origin","dest"]
import random
def addflights (request):
    form = addflight()
    if request.method=="POST":
        form = addflight(request.POST)
        if form.is_valid():
            origin =form.cleaned_data["origin"]
            dest=form.cleaned_data["dest"]
            dur=int(random.randint(100, 500))
            new=flights(origin=origin,dest=dest,dur=dur)
            new.save()
            print("Flight Saved!!🛫")
    return render(request,"flights/add.html",{"form":form})

class addport(forms.ModelForm):
    class Meta:
        model = airport
        fields=["name","code"]

def addports(request):
    fill=addport()
    if request.method=="POST":
        fill=addport(request.POST)
        if fill.is_valid():
            check=airport.objects.filter(code=fill.cleaned_data["code"]).first()
            if check == None:
                name=fill.cleaned_data["name"]
                code=fill.cleaned_data["code"]
                save=airport(name=name,code=code)
                save.save()
                fmsg=f"{name} has been added to out database"
                return render(request ,"flights/addport.html",{"fill":fill,"fmsg":fmsg})
            else:
                msg= "Airport can not be added, Every Airport must have a unique code identifier!"
                return render(request ,"flights/addport.html",{"fill":fill,"msg":msg,})
    return render(request ,"flights/addport.html",{"fill":fill})

# Excluding fields
from .models import students

class addstud(forms.ModelForm):
    class Meta:
        model = students
        exclude = ["sex"]

def addstuds(request):
    form = addstud()
    if request.method=="POST":
        form=addstud(request.POST)
        if form.is_valid():
            #student is an instance of watever is filled in the form
            student = form.save(commit=False)
            student.sex="male"
            student.save()
    return render(request,"flights/addstud.html",{"form":form})