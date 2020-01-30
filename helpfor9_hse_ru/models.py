from django.db import models

class Administrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)

class Facultative(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    dep1 = 'В'; dep2 = 'E'; dep3 = 'FL'
    dep4 = 'C'; dep5 = 'RaP'; dep6 = 'H'
    dep7 = 'HoC'; dep8 = 'M'; dep9 = 'WAC'
    dep10 = 'SC'; dep11 = 'PS'; dep12 = 'L'
    dep13 = 'T'; dep14 = 'PE'

    DEPARTMENTS =  [        #Список кафедр
            (dep1, 'Востоковедение'),
            (dep2, 'Естественные науки'),
            (dep3, 'Иностранные языки'),
            (dep4, 'Информатика'),
            (dep5, 'Исследовательская и проектная деятельность'),
            (dep6, 'История'),
            (dep7, 'История культуры'),
            (dep8, 'Математика'),
            (dep9, 'МХК'),
            (dep10, 'Общественные науки'),
            (dep11, 'Психология'),
            (dep12, 'Словесность'),
            (dep13, 'ТОК'),
            (dep14, 'Физическая культура')
        ]
    
    department = models.CharField(max_length=3, choices=DEPARTMENTS, default=0)


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=30)

    cour1 = 'В'; cour2 = 'Г'; cour3 = 'Д'; cour4 = 'Е'; cour5 = 'М' 
    cour6 = 'И'; cour7 = 'П'; cour8 = 'Э'; cour9 = 'С'; cour10 = 'Ю' 
    
    COURSES = [         #список направлений
        (cour1, 'Востоковедение'),
        (cour2, 'Гуманитарные науки'),
        (cour3, 'Дизайн'),
        (cour4, 'Естественные науки'),
        (cour5, 'Математика'),
        (cour6, 'Информатика, инженерия и математика'),
        (cour7, 'Психология'),
        (cour8, 'Экономика и математика'),
        (cour9, 'Экономика и социальные науки'),
        (cour10, 'Юриспруденция')
    ]

    course = models.CharField(max_length=1, choices=COURSES, default=0)
