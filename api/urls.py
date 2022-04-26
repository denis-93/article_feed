from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, ArticleViewSet

router = DefaultRouter()
router.register('articles',ArticleViewSet, basename='article')


app_name = 'api'
urlpatterns = [
    path('registration/', CreateUserView.as_view()),
    path('', include(router.urls)),
]