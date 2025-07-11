from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.item_view import ItemViewSet
from api.views import ArticleView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    # /articles/ - GET (list) và POST (create)
    path('articles/', ArticleView.as_view(), name='article-list-create'),
    # /articles/<pk>/ - GET (detail), PUT (update), DELETE (delete)
    path('articles/<int:pk>/', ArticleView.as_view(), name='article-detail'),
    path('', include(router.urls)),
]

