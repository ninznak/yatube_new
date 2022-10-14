from django.urls import path
from django.contrib import admin
from . import views

app_name='posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_posts'),
    path('name/', views.name, name = 'name'),
    path('yandex/', views.yandex, name='yandex'),
    path('admin/', admin.site.urls)
]

