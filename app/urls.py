from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('remove_todo/<int:pk>/', views.remove_todo, name='remove_todo')
]
