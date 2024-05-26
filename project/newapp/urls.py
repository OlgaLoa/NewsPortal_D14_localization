from django.urls import path
# Импортируем созданное нами представление
from .views import (NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, subscriptions)
from django.views.decorators.cache import cache_page


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='news_list'), #(убрала) вернет функцию оборачиваемую в декоратор cache_page со временем кэширования 60 сек
   path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
   path('search/', NewsSearch.as_view(), name='news_search'),

   path('news/create/', cache_page(300)(NewsCreate.as_view()), name='news_create'),
   path('article/create/', cache_page(300)(NewsCreate.as_view()), name='article_create'),

   path('news/<int:pk>/update/', cache_page(300)(NewsUpdate.as_view()), name='news_update'),
   path('article/<int:pk>/update/', cache_page(300)(NewsUpdate.as_view()), name='article_update'),


   path('news/<int:pk>/delete/', cache_page(300)(NewsDelete.as_view()), name='news_delete'),
   path('article/<int:pk>/delete/', cache_page(300)(NewsDelete.as_view()), name='article_delete'),

   path('subscriptions/', subscriptions, name='subscriptions'),
]
