from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrfimport csrf_exempt


def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        # many=True becoz its a Query set
        serializer = ArticleSerializer(articles, many=True)
        # The first parameter, data , should be a dict instance. If the safe parameter is set to False , any object can be passed for serialization; otherwise only dict instances are allowed
        return (JsonResponse(serializer.data, safe=False))

    elif request.method == "POST":
        # When receiving data from a web server, the data is always a string. Parse the data with JSON.parse() , and the data becomes a JavaScript object
        data = JSONParser().parse(request)
        #after converting the data to javascript object we have to serialize the data 
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return (JsonResponse(serializer.error, status=400))

@csrf_exepmt
def article_detail(request, pk):
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
 
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
 
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
