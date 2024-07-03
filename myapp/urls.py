from django.urls import path
from .views import data_view, test_view, index_view

urlpatterns = [
    path('', index_view, name='index'),  # Добавьте этот маршрут для корневого пути
    path('data/', data_view, name='data'),
    path('test/', test_view, name='test'),
]
