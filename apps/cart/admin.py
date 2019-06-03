from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Cart)
# admin.site.register(Favorite)
# admin.site.register(Buynow)
#
from extra_apps import xadmin
from apps.cart.models import *


class CartXadmin(object):
    list_filter = ['user','goods', 'color','spec','price','amount']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = [ 'color','spec','price','amount']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情


xadmin.site.register(Cart,CartXadmin)