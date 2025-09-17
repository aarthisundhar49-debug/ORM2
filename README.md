# Ex02 Django ORM Web Application
## Date: 16.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
~~~
models.py
from django.db import models
from django.contrib import admin
class Car3(models.Model):
    car_name = models.CharField()
    colour = models.CharField()
    release_date = models.DateField()
    car_model = models.CharField()
    
class Car3Admin(admin.ModelAdmin):
    list_display = ('car_name','colour','release_date','car_model')

admin.py
from django.contrib import admin
from.models import Car3,Car3Admin
admin.site.register(Car3,Car3Admin)
~~~

## OUTPUT
![alt text](<Screenshot 2025-09-16 155745.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
