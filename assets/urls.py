#!/usr/bin/env python
#coding:utf-8


from django.conf.urls import include, url
from assets import views

urlpatterns = [
    # 该url包括了客户端执行提交数据的url，也就是接口，后面带？参数的也是匹配这条utl规则
    url(r'report/$', views.asset_report, name='asset_report'),
    # url(r'report/bulk_create/$',views.bulk_create_assets,name='bulk_create_assets' ),
    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id, name='acquire_asset_id'),
    url(r'^report_test/$', views.asset_report_test),
    url(r'^acquire_asset_id_test/$', views.acquire_asset_id_test),
    url(r'^new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),
    url(r'^asset_list/$', views.asset_list, name="asset_list"),
    url(r'^asset_list/(\d+)/$', views.asset_detail, name="asset_detail"),
    url(r'^asset_list/list/$', views.get_asset_list, name="get_asset_list"),
    url(r'^asset_list/category/$', views.asset_category, name="asset_category"),
    url(r'^asset_event_logs/(\d+)/$', views.asset_event_logs, name="asset_event_logs"),
    url(r'^event_center/$',views.event_center,name="event_center"),
    # 机房管理 开始
    url(r'^idc/$', views.idc, name='idc'),
    url(r'^idc/add/$', views.idc_add, name='idc_add'),
    url(r'^idc/del/$', views.idc_del, name='idc_del'),
    url(r'^idc/edit/(?P<idc_id>\d+)/$', views.idc_edit, name='idc_edit'),
    url(r'^idc/cabinetlist/(?P<cabinet_id>\d+)/$', views.cabinet_list, name='idc_cabinet_list'),
    # 机房管理 结束
    # 机柜管理 开始
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
    url(r'^cabinet/del/$', views.cabinet_del, name='cabinet_del'),
    url(r'^cabinet/add/$', views.cabinet_add, name='cabinet_add'),
    url(r'^cabinet/server_list/(?P<cabinet_id>\d+)/$', views.server_list, name='cabinet_server_list'),
    url(r'^cabinet/edit/(?P<cabinet_id>\d+)/$', views.cabinet_edit, name='cabinet_edit'),
    # 机柜管理 结束
    
    # 属组管理 开始
    url(r'^group/$', views.group, name='group'),
    url(r'^group/add/$', views.group_add, name='group_add'),
    url(r'^group/edit/(?P<group_id>\d+)/$', views.group_edit, name='group_edit'),
    url(r'^group/del/$', views.group_del, name='group_del'),
    url(r'^group/server_list/(?P<group_id>\d+)/$', views.groupserver_list, name='group_server_list'),
    # 属组管理 结束

]