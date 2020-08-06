from django.contrib import admin

# Register your models here.
from .models import *


class PlateAdmin(admin.ModelAdmin):
    list_display = ['id', 'P_title', 'ctime', 'uptime']
    list_display_links = ['id', 'P_title', 'ctime', 'uptime']
    search_fields = ['id', 'P_title', 'ctime', 'uptime']
    list_filter = ['P_title']
    date_hierarchy = 'ctime'


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'A_title', 'A_plate', 'ctime', 'uptime']
    list_display_links = ['id', 'A_title', 'A_plate', 'ctime', 'uptime']
    search_fields = ['id', 'A_title', 'A_plate', 'ctime', 'uptime']
    list_filter = ['A_plate']
    date_hierarchy = 'ctime'


class WebsiteAdmin(admin.ModelAdmin):
    # 显示
    list_display = ['id', 'title', 'info', 'logo', 'url', 'ctime', 'uptime', 'classify']
    # 搜索
    search_fields = ('title', 'info', 'logo', 'url', 'ctime', 'uptime', 'classify')
    # 显示时点击
    list_display_links = ('id', 'title', 'info', 'logo', 'url', 'ctime', 'uptime', 'classify')
    # 右侧赛选
    list_filter = ['classify']
    # 按时间搜索
    date_hierarchy = 'ctime'


class WebSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'web_logo', 'domain', 'site_description', 'site_seo_description',
                    'site_keywords','github','author','authorSite']

    list_display_links = ['id', 'site_name', 'web_logo', 'domain', 'site_description', 'site_seo_description',
                    'site_keywords','github','author','authorSite']



admin.site.register(Plate, PlateAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(WebSite, WebsiteAdmin)
admin.site.register(WebSetting, WebSettingAdmin)
