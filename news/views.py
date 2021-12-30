from django import views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import News
from .serializers import NewsSerializer


class NewsListApiView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class NewsCreateApiView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]


class NewsCreateView(LoginRequiredMixin, views.View):

    def get(self, request):
        objects = News.objects.all()
        return render(request, 'news/news_create.html', context={'news': objects})
