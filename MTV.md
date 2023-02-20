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

Прописывание url adress http:// 127.0.0.1:8000/toys/1/
toys urls.py  urlpatterns вставляем струтуру 'cats/<int:catid>/'

urlpatterns = [
    path('',index), 
    path('cats/<int:catid>/', categories)
]

заходим в toys/views.py и добавляем в функцию def categories:

def categories(request, ** catid):
return HttpResponse(f"<h1>Статьи по  категориям</h1><p>{catid}</p>")

добавление регулярного выражения

re_path(r'^arhive/(?P<year>[0-9]{4})/',arhive),

заходим в toys/views.py и добавляем в функцию

def arhive(request, year):

#return HttpResponse(f"<h1>Архив по  годам</h1><p>{year}</p>")

Get запросы
заходим в toys/views.py и в функции def categories вставляем строку:

def categories(request, catid):

* print(request.GET)

return HttpResponse(f"<h1>Статьи по  категориям</h1><p>{catid}</p>")

Заходим в coolsite urls.py прописываем

hendler404=pageNotFound и создаем функцию

заходим в toys/views.py


Редиректы 301 и 302 заходим в views.py и создаем функцию с редиректом

def arhive(request, year):
    if int(year) >2020:
        #raise Http404
        return  redirect('/', permanent=True)


* Урок 4.Определение моделей. Миграции: создание и выполнение.

Заходим в toys/models.py

Создаем класс 

class Toys(models.Model):
     title = models.CharField(max_length= 255)  # заголовок
     content = models.TextField(blank=True) # содержание
     photo = models.IntegerField(upload_to="photos/%Y/%m/%d/")
     time_create = models.DateTimeField(auto_now_add=True)
     time_update = models.DateTimeField(auto_now=True)
     is_published = models.BooleanField(default=True)


Настройка Mediaurl and Media

Заходим в coolsite/settings.py и прописываем константы в самом низу

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media'


Заходим в coolsite/urls.py в режиме отладки добавляем еще один маршрут,после urlpatterns, для статических данных граффических файлов

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

DEBUG = TRUE!!!

команды в терминале
 python manage.py makemigrations


 python manage.py sqlmigrate toys 0001
 
Создание таблицы в базе данных:

 python manage.py migrate

