from django.urls import path
from . import views

urlpatterns = [
    path('articles/',views.article_list),
    path('detail/<int:pk>/',views.article_detail)
]
