from django.urls import path, re_path

from  .views import *

urlpatterns = [
    path('',index),  # http://127.0.01:8000/toys/
    path('cats/<int:catid>/', categories), # http://127.0.01:8000/toys/cats/
    re_path(r'^arhive/(?P<year>[0-9]{4})/',arhive),
]

