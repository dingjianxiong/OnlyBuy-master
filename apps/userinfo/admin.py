from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(UserInfo)
# admin.site.register(Address)
# from extra_apps import xadmin
from .models import *

from extra_apps import xadmin
# from extra_apps.xadmin.views import *
# from extra_apps.xadmin.plugins.auth import UserAdmin, User

# class Xadminsetting(object):
#     site_title='OnlyBuy后台管理系统'
#     site_footer='欢迎来到 www.com'
#     #左侧菜单栏可折叠
#     menu_style='目录'
# class SettingXadmin(object):
#     # 启用主题管理器
#     enable_themes = True
#     # 使用主题
#     use_bootswatch = True
#
#
# from extra_apps.xadmin import views  # 导入views模块
#
#
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册到xadmin中
# xadmin.site.register(views.CommAdminView, Xadminsetting)  # 注册到xadmin中
class EmailVerifyRecordXadmin(object):
    list_filter = ['code','email', 'send_type','send_time']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['code','email']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情

class AddressXadmin(object):
    list_filter = ['consignee','ads', 'mobile','defaultads','zipcode','alias']  # 排序
    list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
    refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
    search_fields = ['consignee','ads', 'mobile','defaultads']
    list_per_Page = 20
    show_all_rel_details = True  # 设置为True，显示所有字段的详情
# class UserInfoXAdmin(object):
#     list_filter = ['headp','nickname', 'mobile','email','sex']  # 排序
#     list_export = ('xls', 'json',)  # 数据导出格式，默认支持四种格式
#     refresh_times = (3, 5)  # 3秒或者5秒刷新一次数据
#     search_fields = ['headp','nickname', 'mobile','email','sex']
#     list_per_Page = 20
#     show_all_rel_details = True  # 设置为True，显示所有字段的详情
# xadmin.site.register(UserInfo, UserInfoXAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordXadmin)
# xadmin.site.register(CommAdminView, Xadminsetting )
# xadmin.site.register(BaseAdminView,SettingXadmin)
xadmin.site.register(Address,AddressXadmin)