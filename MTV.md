* Ведение
1.cd coolsite 
2.python manage.py runserver
* 2 урок. MTV
1.cd coolsite 
2.python manage.py startapp <имя директории на сайте>  toys
python manage.py startapp toys
3.Регистрация toys
coolsite -директория
заходим settings.py
INSTALLED_APPS редактируем + добавляем путь к toys из пакета
-'toys.apps.ToysConfig' 
4.Заходим во toys/views 
объявляем функцию:
def index(request):
    return HttpResponse("Страница приложения toys")
5. /coolsite/urls.py добавляем маршрут
  path('toys/', index), # http:// 127.0.0.1:8000/toys/ 
и перезапускаем страницу в браузере
* Урок 3. Маршрутизация. обработка исключений запросов, перенаправления.
