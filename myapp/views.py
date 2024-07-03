from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Добро пожаловать на главную страницу.")

def data_view(request):
    return HttpResponse("Это страница данных.")

def test_view(request):
    return HttpResponse("Это тестовая страница.")
