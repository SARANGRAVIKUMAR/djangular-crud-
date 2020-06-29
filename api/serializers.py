"""before sending the data to client we have to convert that data to json format thats the use of serializers as apis end result is json format """

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    """If we want to be able to return complete object instances based on the validated data we need to implement one or both of the .create() and .update() 
    methods these methods are used while using serializers.Serializer while using ModelSerializer we dont have to use these steps"""

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self,instance,validated_data):                   
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.email=validated_data.get('email',instance.email)
        instance.date=validated_data.get('date',instance.date)
        instance.save()
        return(instance)