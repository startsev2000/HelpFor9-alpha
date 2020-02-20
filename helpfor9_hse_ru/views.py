from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Facultative

facultatives = {'vostok': 'Востоковедение',
                'natscience': 'Естественные науки',
                'foreign': 'Иностранные языки',
                'computers': 'Информатика',
                'research': 'Исследование и проекты',
                'history': 'История',
                'culthist': 'История культуры',
                'math': 'Математика',
                'mhk': 'МХК',
                'social': 'Общественные науки',
                'psychology': 'Психология',
                'words': 'Словесность',
                'tok': 'ТОК',
                'physed': 'Физическая культура',
                }


def get_base_context(request):
    return {'title': 'HelpFor9'}


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


def faculties(request):
    context = get_base_context(request)
    context.update({'list_facs': facultatives.items()})

    return render(request, 'Facultatives/facultatives.html', context)


def faculties_1(request, facultative):  # Востоковедение
    context = get_base_context(request)
    context.update({'list_facs': facultatives.items()})
    context.update({'facultatives': Facultative.objects.filter(department=facultatives[facultative])})
    return render(request, 'Facultatives/facultatives1.html', context)


def calendar_1(request):
    return render(request, 'calendar.html')


def calendar_2(request):
    return render(request, 'calendar.html')


def calendar_3(request):
    return render(request, 'calendar.html')


def calendar_4(request):
    return render(request, 'calendar.html')


def calendar_5(request):
    return render(request, 'calendar.html')


def calendar_6(request):
    return render(request, 'calendar.html')


def calendar_7(request):
    return render(request, 'calendar.html')


def calendar_8(request):
    return render(request, 'calendar.html')


def calendar_9(request):
    return render(request, 'calendar.html')


def calendar_10(request):
    return render(request, 'calendar.html')
