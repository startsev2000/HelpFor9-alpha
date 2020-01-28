from django.db import models

class Administrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)

class Facultative(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=30)
