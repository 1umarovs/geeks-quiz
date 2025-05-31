from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]
