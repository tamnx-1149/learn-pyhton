from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.item_view import ItemViewSet
from api.views import ArticleView
from api.views import CommentView
from api.views.user_view import UserView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    # /articles/ - GET (list) và POST (create)
    path('articles/', ArticleView.as_view(), name='article-list-create'),
    # /articles/<pk>/ - GET (detail), PUT (update), DELETE (delete)
    path('articles/<slug:slug>/', ArticleView.as_view(), name='article-detail'),

    # /articles/<slug>/comments/ - GET (list) và POST (create)
    path('articles/<slug:slug>/comments/', CommentView.as_view(), name='comment-list-create'),
    # /comments/<pk>/ - DELETE (delete)
    path('comments/<int:pk>/', CommentView.as_view(), name='comment-delete'),

    path('profiles/<str:username>/', UserView.as_view(), name='profile-detail'),

    path('', include(router.urls)),
]
