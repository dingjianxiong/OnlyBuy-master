import django_filters
from .models import Goods
class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品的过滤类
    '''
    min_price=django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price=django_filters.NumberFilter(field_name='price',lookup_expr='lte')
    # 商品模糊查询
    name = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model=Goods
        fields=['min_price','max_price','name']