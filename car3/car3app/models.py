
from django.db import models
from django.contrib import admin
class Car3(models.Model):
    car_name = models.CharField()
    colour = models.CharField()
    release_date = models.DateField()
    car_model = models.CharField()
    

class Car3Admin(admin.ModelAdmin):
    list_display = ('car_name','colour','release_date','car_model')
# Create your models here.
