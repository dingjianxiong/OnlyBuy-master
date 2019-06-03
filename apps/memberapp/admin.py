from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Promise)
# admin.site.register(GoodsType)
# admin.site.register(GoodsImg)
# admin.site.register(GoodsColor)
# admin.site.register(Goods)
# admin.site.register(GoodsDetail)
# admin.site.register(Banner)

from  extra_apps import xadmin
from apps.memberapp.models import *

class GoodsTypeXadmin(object):
    list_filter = ['title','desc', 'isDelete']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['title','desc', 'isDelete']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class GoodsXadmin(object):
    list_filter = ['title','price','desc','promise', 'listimg','isDelete','type']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['title','price','isDelete','type']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class GoodsDetailXadmin(object):
    list_filter = ['specifice','stock','goods']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['specifice','stock',]
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class BannerXadmin(object):
    list_filter = ['bannerimg','type']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['specifice','stock',]
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
class GoodsImgXadmin(object):
    list_filter = ['goodsimg','goodsimgbig','goods']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['goodsimg','goodsimgbig']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情

xadmin.site.register(Goods,GoodsXadmin)
xadmin.site.register(GoodsType,GoodsTypeXadmin)
xadmin.site.register(GoodsDetail,GoodsDetailXadmin)
xadmin.site.register(Banner,BannerXadmin)
xadmin.site.register(GoodsImg,GoodsImgXadmin)
