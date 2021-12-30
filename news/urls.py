from django.urls import path

from .views import NewsListApiView, NewsCreateView, NewsCreateApiView


urlpatterns = [
    path('', NewsListApiView.as_view(), name='news_list_api_url'),
    path('api/add', NewsCreateApiView.as_view(), name='news_create_api_url'),
    path('add/', NewsCreateView.as_view(), name='news_create_url')
]
