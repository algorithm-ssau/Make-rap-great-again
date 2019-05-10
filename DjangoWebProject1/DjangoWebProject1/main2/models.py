from django.db import models

# Create your models here.


class Rapper(models.Model): 
 id_rapper = models.UUIDField(primary_key=True) 
 name = models.CharField(max_length=100) 
 biography = models.CharField(max_length=500) 
 photo = models.BinaryField(null=True) 

class Season(models.Model): 
 id_season = models.UUIDField(primary_key=True) 
 name = models.CharField(max_length=100) 
 year = models.IntegerField() 
 text = models.CharField(max_length=500) 
 photo = models.BinaryField(null=True) 
 grid = models.BinaryField(null=True)

class Punch(models.Model): 
 id_punch = models.UUIDField(primary_key=True) 
 id_rapper = models.ForeignKey(Rapper) 
 fabula = models.CharField(max_length=200,null=True) 
 id_season = models.ForeignKey(Season,null=True) 
 censure = models.IntegerField() 
 text = models.CharField(max_length=500) 