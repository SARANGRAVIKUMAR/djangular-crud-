from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename="article")


urlpatterns = [
    # so to go to ArticleVieSet in the url we have to type viewset/article
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', ArticleAPIView.as_view()),  # class based api_voew
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),  # generic view

]



""" GET ->getting the data 
    POST ->posting the data
    PUT ->updating the data 
    DELETE ->deleting the data"""