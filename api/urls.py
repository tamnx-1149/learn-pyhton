from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.item_view import ItemViewSet
from api.views import ArticleView
from api.views import CommentView
from api.views.user_follow_view import UserFollowAPIView
from api.views.user_view import UserView, LoginView, RegisterView, MeView
from api.views.article_favorite_view import ArticleFavoriteAPIView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('login/', LoginView.as_view(), name='auth_login'),

    # /articles/ - GET (list) và POST (create)
    path('articles/', ArticleView.as_view(), name='article-list-create'),
    # /articles/<pk>/ - GET (detail), PUT (update), DELETE (delete)
    path('articles/<slug:slug>/', ArticleView.as_view(), name='article-detail'),

    # /articles/<slug>/comments/ - GET (list) và POST (create)
    path('articles/<slug:slug>/comments/', CommentView.as_view(), name='comment-list-create'),
    # /comments/<pk>/ - DELETE (delete)
    path('articles/<slug:slug>/comments/<int:pk>/', CommentView.as_view(), name='comment-delete'),

    path('profiles/<str:username>/', UserView.as_view(), name='profile-detail'),

    path('me/', MeView.as_view(), name='user-me'),

    path('update-profile/', MeView.as_view(), name='update-profile'),

    path('', include(router.urls)),

    path('articles/<slug:slug>/favorites/', ArticleFavoriteAPIView.as_view(), name='article-favorite'),

    path('profiles/<str:username>/follow/', UserFollowAPIView.as_view(), name='user-follow'),  # POST (follow), GET (list)

    # path('profiles/<username:username>/follow/<int:followee_id>/', UserFollowAPIView.as_view(), name='user-unfollow'),  # DELETE (unfollow)
]
