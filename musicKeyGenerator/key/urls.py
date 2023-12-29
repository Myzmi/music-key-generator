from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("selKey", views.key, name="selKey"),
    path("<str:note>/<str:type>", views.keyPage, name="keyPage"),
    path("randomKey", views.randomKey, name="randomKey")
]