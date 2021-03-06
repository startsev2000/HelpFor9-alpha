from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Facultative

def index(request):
    return render(request, 'index.html')


def calendar(request):
    events = Event.objects.all()

    return render(request, 'calendar.html', {'events': events})


def calculator(request):
    return render(request, 'Calculator/calculator.html')


def calculator_1(request):  # Востоковедение

    return render(request, 'Calculator/calculator1.html')


def calculator_2(request):
    return render(request, 'Calculator/calculator2.html')  # Гуманитарные науки


def calculator_3(request):
    return render(request, 'Calculator/calculator3.html')  # Дизайн


def calculator_4(request):
    return render(request, 'Calculator/calculator4.html')  # Естественные науки


def calculator_5(request):
    return render(request, 'Calculator/calculator5.html')  # Математика


def calculator_6(request):
    # Информатика, инженерия и математика
    return render(request, 'Calculator/calculator6.html')


def calculator_7(request):
    return render(request, 'Calculator/calculator7.html')  # Психология


def calculator_8(request):
    # Экономика и математика
    return render(request, 'Calculator/calculator8.html')


def calculator_9(request):
    # Экономика и социальные науки
    return render(request, 'Calculator/calculator9.html')


def calculator_10(request):
    return render(request, 'Calculator/calculator10.html')  # Юриспруденция


def info_1(request):
    return render(request, 'info1.html')


def info_2(request):
    return render(request, 'info2.html')


def info_3(request):
    return render(request, 'info3.html')


def info_4(request):
    return render(request, 'info4.html')


def info_5(request):
    return render(request, 'info5.html')


def info_6(request):
    return render(request, 'info6.html')


def info_7(request):
    return render(request, 'info7.html')


def info_8(request):
    return render(request, 'info8.html')


def info_9(request):
    return render(request, 'info9.html')


def info_10(request):
    return render(request, 'info10.html')

def faculties(request):  # Востоковедение

    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives.html', {'facultatives': facultatives})


def faculties_1(request):  # Востоковедение

    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives1.html', {'facultatives': facultatives})


def faculties_2(request):  # Естественные науки
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives2.html', {'facultatives': facultatives})


def faculties_3(request):  # Иностранные языки
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives3.html', {'facultatives': facultatives})


def faculties_4(request):  # Информатика
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives4.html', {'facultatives': facultatives})


def faculties_5(request):  # Исследовательская и проектная деятельность учащихся
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives5.html', {'facultatives': facultatives})


def faculties_6(request):  # История
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives6.html', {'facultatives': facultatives})


def faculties_7(request):  # История культуры
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives7.html', {'facultatives': facultatives})


def faculties_8(request):  # Математика
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives8.html', {'facultatives': facultatives})


def faculties_9(request):  # МХК
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives9.html', {'facultatives': facultatives})


def faculties_10(request):  # Общественные науки
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives10.html', {'facultatives': facultatives})


def faculties_11(request):  # Психология
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives11.html', {'facultatives': facultatives})


def faculties_12(request):  # Словесность
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives12.html', {'facultatives': facultatives})


def faculties_13(request):  # ТОК
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives13.html', {'facultatives': facultatives})


def faculties_14(request):  # Физическая культура
    facultatives = Facultative.objects.all()

    return render(request, 'Facultatives/facultatives14.html', {'facultatives': facultatives})
