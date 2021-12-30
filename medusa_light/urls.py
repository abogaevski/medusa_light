from django.urls import path, include

urlpatterns = [
    path('', include('common.urls')),
    path('news/', include('news.urls')),
]
