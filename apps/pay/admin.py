from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Bank)
# admin.site.register(Banklist)

from extra_apps import xadmin
from .models import *
# from extra_apps.xadmin.views import *

class BankXadmin(object):
    list_filter = ['bank','bankid', 'status','user']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['bank','bankid', 'status']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class BanklistXadmin(object):
    list_filter = ['bank','bankimg']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['bank','bankid', 'status']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情

xadmin.site.register(Bank,BankXadmin)
xadmin.site.register(Banklist,BanklistXadmin)
