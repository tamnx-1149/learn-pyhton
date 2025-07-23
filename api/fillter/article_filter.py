# filters.py
import django_filters
from api.models import Article


class ArticleFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name='tags__name', lookup_expr='exact')  # lọc theo tên tag

    class Meta:
        model = Article
        fields = ['author', 'tag']  # Các field lọc
