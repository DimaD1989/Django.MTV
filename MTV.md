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

* CRUD - основы ORM по работе с моделями

запустить команду 
cd coolsite
python manage.py shell
 
сделать импорт 

 from toys.models import Toys

заполтим данные наших полей. Для этого введем данные

Toys(title= 'Чеберашка',content='Описание игрушки') и нажем энтер

<Toys: Toys object (None)>

сохраним данные в таблице. для этого введе переменную

 t1 = _

 t1
<Toys: Toys object (None)>

и сохраним данные в нашей таблицею для этого введем команду

t1.save().
 
t1.id 
2
t1.title
'Чебурашка'
t1.time_create
datetime.datetime(2023, 3, 2, 9, 50, 19, 616485, tzinfo=datetime.timezone.utc)

t1.pk
2

id = pk

sql запрос для выплнения этой записи

импортируем модуль

from django.db import connection

и через него обратимся к коллекции

connection.queries выполнем ее

[{'sql': 'INSERT INTO "toys_toys" ("title", "content", "photo", "time_create", "time_upd
ate", "is_published") VALUES (\'Чеберашка\', \'Описание игрушки\', \'\', \'2023-03-02 09
:46:24.328446\', \'2023-03-02 09:46:24.328446\', 1) RETURNING "toys_toys"."id"', 'time':
 '0.000'}, {'sql': 'INSERT INTO "toys_toys" ("title", "content", "photo", "time_create",
 "time_update", "is_published") VALUES (\'Чебурашка\', \'Описание игрушки\', \'\', \'202
3-03-02 09:50:19.616485\', \'2023-03-02 09:50:19.616485\', 1) RETURNING "toys_toys"."id"', 'time': '0.000'}]


t4 = Toys()
                                         
t4.title = 'Зайчик'

t4.сontent = 'Описание игрушки'

t4.save() 

# objects 

Toys.objects  

<django.db.models.manager.Manager object at 0x00000261B833D810>

ДОБАВЛЕНИЕ ЗАПИСИ

t5 = Toys.objects.create(title='Паук', content='Коричневый') - сразу попадает в базу данных

ЧТЕНИЕ ДАННЫХ ИЗ ТАБЛИЦЫ

 Toys.objects.all()  

<QuerySet [<Toys: Toys object (1)>, <Toys: Toys object (2)>, <Toys: Toys object (3)>, <Toys: Toys object (4)>, <Toys: Toys object (5)>]>

Для отображения полей в models.py пропишим функцию:

def __str__(self):
     return self.title

выйти из оболочки джанго.

exit()

и зайдем обратно

python manage.py shell

 импортируем клас Toys

from toys.models import Toys 

Toys.objects.all()

<QuerySet [<Toys: Чеберашка>, <Toys: Чебурашка>, <Toys: Пикачу>, <Toys: Зайчик>, <Toys: Паук>]>

Оращение к списку

t = _
t[0]
<Toys: Чеберашка>

длина списка

len(t)

len(t)

5

 проитеррируем список
for ti in  t:
    print(ti.title)

Чеберашка
Чебурашка
Пикачу
Зайчик
Паук

Фильтрация
 
Toys.objects.filter(title='Паук')                            

<QuerySet [<Toys: Паук>]>
 
Toys.objects.filter(pk__gte=2)                       
<QuerySet [<Toys: Чебурашка>, <Toys: Пикачу>, <Toys: Зайчик>, <Toys: Паук>]>

Toys.objects.exclude(pk=2)      
<QuerySet [<Toys: Чеберашка>, <Toys: Пикачу>, <Toys: Зайчик>, <Toys: Паук>]>

 Toys.objects.get(pk=2)     
<Toys: Чебурашка>

отличие методов  filter от get

метод get  генерирует исключенияоб ошибке,  filter нет

СОРТИРОВКА

Toys.objects.filter(pk__lte=4).order_by('title')
<QuerySet [<Toys: Зайчик>, <Toys: Пикачу>, <Toys: Чеберашка>, <Toys: Чебурашка>]>

Toys.objects.order_by('title')                   
<QuerySet [<Toys: Зайчик>, <Toys: Паук>, <Toys: Пикачу>, <Toys: Чеберашка>, <Toys: Чебурашка>]>


Toys.objects.order_by('-time_update')    
<QuerySet [<Toys: Паук>, <Toys: Зайчик>, <Toys: Пикачу>, <Toys: Чебурашка>, <Toys: Чеберашка>]>

 Toys.objects.order_by('time_update')  
<QuerySet [<Toys: Чеберашка>, <Toys: Чебурашка>, <Toys: Пикачу>, <Toys: Зайчик>, <Toys: Паук>]>

'-' -  сортирует с конца

ЗАМЕНА ЗАПИСЕЙ

прочесть ее из бд
tu = Toys.objects.get(pk=2)

tu.title = 'Котик'

tu.content = 'Серый' 

tu.save()


УДАЛЕНИЕ ЗАПИСИ

td = Toys.objects.filter(pk__gte=4) 

td

<QuerySet [<Toys: Зайчик>, <Toys: Паук>]>

td.delete()

(2, {'toys.Toys': 2})






















