from django.db import models

# Create your models here.
class Classes(models.Model):
    classname = models.CharField(max_length=60)
    teacher = models.CharField(max_length=62)
    no_of_studs = models.IntegerField(default=0)

    def __str__(self):
        return f"Welcome to {self.classname}. Population: {self.no_of_studs + 1}"

class entry(models.Model):
    Book_name = models.CharField(max_length=50)
    NOC = models.IntegerField()
    DOE = models.DateField()

    def __str__(self):
        return f"{self.Book_name}"

class students(models.Model):
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    # many to one relationship
    class_name = models.ForeignKey(Classes,on_delete = models.CASCADE)
    gender = [("male","Male"),("female","Female"),("custom","Custom")]
    sex = models.CharField(max_length = 10,choices= gender)

    def __str__(self):
        return f"{self.Name}'s profile"

class book(models.Model):
    Name = models.CharField(max_length=80)
    choices = [("yes","Published"),("no","Not Published")]
    published = models.CharField(max_length=10,choices=choices)

    def __str__(self):
        return f"{self.Name} is {self.published}"

# Manipulating data in models
class airport(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=5)
    def __str__(self):
        return f'{self.code} | {self.name}'

class flights(models.Model):
    # related_name gives us access to flight from airport models
    origin = models.ForeignKey(airport, related_name="departures", on_delete=models.CASCADE)
    dest = models.ForeignKey(airport, related_name="arrivals", on_delete=models.CASCADE)
    dur = models.IntegerField()

    def delay(self, period):
        self.dur += period
        self.save()

    def __str__(self):
        return f"{self.origin} to {self.dest} - {self.dur}"

# creating row data in models
#creating rows in de airport model
# >>> ibomair = airport(name = "Ibom Air",code="IBA")
# >>> ibomair.save()
# creating rows in the flights model
# flight1 = flights(origin=lag,dest=ibomair,dur=60)
# >>> flight1.save()

#retrieving data from a model
#  airport.objects.filter().all()  

# retieving certain 

# Returning all
#  airport.objects.filter(code="LGA").all() 
# Returning first
# >>> airport.objects.filter(code="LGA").first() 
# you can also manipulte the queryset as a list
# airport.objects.filter(code="LGA").all()[0] # Indexing

# in place of . use __ (you cant use . in filter only__)
#  flights.objects.filter(origin__code="IBA").all() 

# comparing
# flights.objects.filter(dur__gt=30).all()  
# <QuerySet [<flights: LGA | Lagos Air to IBA | Ibom Air - 60>, <flights: IBA | Ibom Air to MMA | Murtala Mohamed International Airport - 120>]>
# others are: __lt,__gte,__lte

# using "like" in python
#  flights.objects.filter(dest__name__icontains="bo").all()

# chaining filters(like and)
# flights.objects.filter(dest__name__icontains="bo").filter(origin__code__icontains="l").all() 
# or
# flights.objects.filter(origin__name__icontains="bo",dest__code__icontains="M").all()

# to use OR
# from django.db.models import Q
#  flights.objects.filter(Q(origin__code="MMA")|Q(dest__code="MMA")).all() 

# Looping through QuerSets
# for code in airport.objects.all():
# ...     print(code.code)
# ... 
# IBA
# LGA
# MMA


# UPDATING MODELS
# you first need to capture what you want to update
# first=airport.objects.first()


#Then modify
# first.code="IBM"
# >>> first.save()

# Modefying references
# >>> flight1=flights.objects.first()
# >>> flight1
# <flights: LGA | Lagos Air to IBM | Ibom Air - 60>
# hold the new instance in a variable ##
# >>> change = airport.objects.last()
# >>> flight1.dest=change
# >>> flight1.save()

# to delete
# flight1.delete()