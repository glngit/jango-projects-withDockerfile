from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    companey = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Bangjobs(models.Model):
    date=models.DateField()
    companey=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField(10)

class Chennaijobs(models.Model):
    date=models.DateField()
    companey=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class Punejobs(models.Model):
    date=models.DateField()
    companey=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField(10)
