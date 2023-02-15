from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return HttpResponse("Страница приложения toys")

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по  категориям</h1><p>{catid}</p>")

def arhive(request, year):
    if int(year) >2020:
        return  redirect('/', permanent=True)

    return HttpResponse(f"<h1>Архив по  годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')