from django.db import models


class Administrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)


class Facultative(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    DEPARTMENTS = [
        ('Востоковедение', 'Востоковедение'),
        ('Естественные науки', 'Естественные науки'),
        ('Иностранные языки', 'Иностранные языки'),
        ('Информатика', 'Информатика'),
        ('Исследовательская и проектная деятельность',
         'Исследовательская и проектная деятельность'),
        ('История', 'История'),
        ('История культуры', 'История культуры'),
        ('Математика', 'Математика'),
        ('МХК', 'МХК'),
        ('Общественные науки', 'Общественные науки'),
        ('Психология', 'Психология'),
        ('Словесность', 'Словесность'),
        ('ТОК', 'ТОК'),
        ('Физическая культура', 'Физическая культура')
    ]

    department = models.CharField(
        max_length=50, choices=DEPARTMENTS, default=0)


class Event(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    COURSES = [
        ('Востоковедение', 'Востоковедение'),
        ('Гуманитарные науки', 'Гуманитарные науки'),
        ('Дизайн', 'Дизайн'),
        ('Естественные науки', 'Естественные науки'),
        ('Математика', 'Математика'),
        ('Информатика, инженерия и математика',
         'Информатика, инженерия и математика'),
        ('Психология', 'Психология'),
        ('Экономика и математика', 'Экономика и математика'),
        ('Экономика и социальные науки', 'Экономика и социальные науки'),
        ('Юриспруденция', 'Юриспруденция')
    ]

    course = models.CharField(max_length=50, choices=COURSES, default=0)
