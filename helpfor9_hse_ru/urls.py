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
    path('facultatives/<str:facultative>', views.faculties_1),
    path('calendar/', views.calendar, name="Календарь"),


]
