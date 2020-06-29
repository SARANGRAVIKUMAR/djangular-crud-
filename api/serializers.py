"""before sending the data to client we have to convert that data to json format thats the use of serializers as apis end result is json format """

from rest_framework import serializers
from .models import Article
 
 
 
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']