from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'subject', 'content', 'pub_date']
