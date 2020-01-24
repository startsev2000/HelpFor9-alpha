from django.db import models

class Administrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)

class Facultative(models.Model):
    facultative_name = models.CharField(max_length=200)
    facultative_date = models.DateField()
    facultative_time = models.TimeField()
    facultative_place = models.CharField(max_length=30) #краткое название здания
    facultative_teacher = models.CharField(max_length=200)

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_place = models.CharField(max_length=30)
