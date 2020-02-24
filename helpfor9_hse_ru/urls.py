from django.contrib import admin
from django.urls import include, path


from helpfor9_hse_ru import views

urlpatterns = [
    path('', views.index, name="index"),

    path('calculator/', views.calculator, name="calculator"),
    path('calculator/vostok', views.calculator_1, name="Балл востока"),
    path('calculator/gum', views.calculator_2, name="Балл гума"),
    path('calculator/design', views.calculator_3, name="Балл дизайна"),
    path('calculator/natscience', views.calculator_4, name="Балл химбио"),
    path('calculator/math', views.calculator_5, name="Балл математики"),
    path('calculator/infomath', views.calculator_6, name="Балл матинфо"),
    path('calculator/psychology', views.calculator_7, name="Балл психологии"),
    path('calculator/matheconom', views.calculator_8, name="Балл матэка"),
    path('calculator/soceconom', views.calculator_9, name="Балл соцэка"),
    path('calculator/yurispr', views.calculator_10, name="Балл юриспруденции"),

    path('vostok', views.info_1, name="Востоковедение"),
    path('gum', views.info_2, name="Гуманитарные науки"),
    path('design', views.info_3, name="Дизайн"),
    path('natscience', views.info_4, name="Естественные науки"),
    path('math', views.info_5, name="Математика"),
    path('infomath', views.info_6, name="Информатика, инженерия и математика"),
    path('psychology', views.info_7, name="Психология"),
    path('matheconom', views.info_8, name="Экономика и математика"),
    path('soceconom', views.info_9, name="Экономика и социальные науки"),
    path('yurispr', views.info_10, name="Юриспруденция"),

    path('facultatives/', views.faculties, name="Список факультативов"),
    path('facultatives/vostok', views.faculties_1, name="Востоковедение"),
    path('facultatives/natscience', views.faculties_2, name="Естественные науки"),
    path('facultatives/foreign', views.faculties_3, name="Иностранные языки"),
    path('facultatives/computers', views.faculties_4, name="Информатика"),
    path('facultatives/research', views.faculties_5,
         name="Исследовательская и проектная деятельность"),
    path('facultatives/history', views.faculties_6, name="История"),
    path('facultatives/culthist', views.faculties_7, name="История культуры"),
    path('facultatives/math', views.faculties_8, name="Математика"),
    path('facultatives/mhk', views.faculties_9, name="МХК"),
    path('facultatives/social', views.faculties_10, name="Общественные науки"),
    path('facultatives/psychology', views.faculties_11, name="Психология"),
    path('facultatives/words', views.faculties_12, name="Словесность"),
    path('facultatives/tok', views.faculties_13, name="ТОК"),
    path('facultatives/physed', views.faculties_14, name="Физическая культура"),

    path('calendar/', views.calendar, name="Календарь"),
]
