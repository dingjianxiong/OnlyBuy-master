from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Order)
# admin.site.register(OrderGoods)
# admin.site.register(Logistics)
# admin.site.register(LogisticsInfo)

from extra_apps import xadmin
from .models import *

class OrderXadmin(object):
    list_filter = ['orderNo','ads', 'ads','trmoney','amount','bank','dealtime','status','user']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['orderNo','ads', 'ads','trmoney','amount','bank','dealtime','status']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class OrderGoodsXadmin(object):
    list_filter = ['title','price', 'desc','amount','color','spec','goodsimg','trprice']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['bank','bankid', 'status']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class LogisticsXadmin(object):
    list_filter = ['logistics_company','express_number', 'order']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['logistics_company','express_number']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
xadmin.site.register(Order,OrderXadmin)
xadmin.site.register(OrderGoods,OrderGoodsXadmin)
xadmin.site.register(Logistics,LogisticsXadmin)