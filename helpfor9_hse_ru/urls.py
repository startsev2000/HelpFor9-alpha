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

    path('facultatives/', views.faculties_1, name="Список факультативов"),
    path('faculties/vostok', views.faculties_1, name="Востоковедение"),       
    path('faculties/natscience', views.faculties_2, name="Естественные науки"),       
    path('faculties/foreign', views.faculties_3, name="Иностранные языки"),       
    path('faculties/computers', views.faculties_4, name="Информатика"),   
    path('faculties/history', views.faculties_5, name="История"),         
    path('faculties/culthist', views.faculties_6, name="История культуры"),
    path('faculties/research', views.faculties_7, name="Исследовательская и проектная деятельность"),
    path('faculties/math', views.faculties_8, name="Математика"),
    path('faculties/mhk', views.faculties_9, name="МХК"),
    path('faculties/social', views.faculties_10, name="Общественные науки"),
    path('faculties/psychology', views.faculties_11, name="Психология"),
    path('faculties/words', views.faculties_12, name="Словесность"),
    path('faculties/tok', views.faculties_13, name="ТОК"),
    path('faculties/physed', views.faculties_14, name="Физическая культура"), 

    path('calendar/vostok', views.calendar_1, name="События востоковедения"),
    path('calendar/gum', views.calendar_2, name="События гуманитарных наук"),
    path('calendar/design', views.calendar_3, name="События дизайна"),
    path('calendar/natscience', views.calendar_4, name="События естественных наук"),
    path('calendar/math', views.calendar_5, name="События математики"),
    path('calendar/infomath', views.calendar_6, name="События матинфо"),
    path('calendar/psychology', views.calendar_7, name="События психологии"),
    path('calendar/matheconom', views.calendar_8, name="События матэка"),
    path('calendar/soceconom', views.calendar_9, name="События соцэка"),
    path('calendar/yurispr', views.calendar_10, name="События юриспруденции"),

]   