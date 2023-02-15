from  django.urls import path

from  .views import *

urlpatterns = [
    path('',index),  # http://127.0.01:8000/toys/
    path('cats/', categories) # http://127.0.01:8000/toys/cats/
]