
	
from django.urls import path
from .views import ArticleAPIView, ArticleDetails
 
urlpatterns = [
 
 
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
 
]