
from django.conf.urls import url

from apps.book import views

urlpatterns = [
    #导航
    url(r'nav/', views.nav),
    #全部书名信息
    url(r'bookname/', views.book_name_all),
    #一级分类
    url(r'bookclass/', views.book_class),
    #二级分类
    url(r'bookclass1/', views.book_class_1),
    #本周强推
    url(r'week/', views.week),
    #玄幻
    url(r'xuanhuan/', views.xuanhuan),
    url(r'xuanhuan_name/', views.xuanhuan_name),
    #奇幻
    url(r'qihuan/', views.qihuan),
    url(r'qihuan_name/', views.qihuan_name),
    #武侠
    url(r'wuxia/', views.wuxia),
    url(r'wuxia_name/', views.wuxia_name),
    #仙侠
    url(r'xianxia/', views.xianxia),
    url(r'xianxia_name/', views.xianxia_name),
    #都市
    url(r'dushi/', views.dushi),
    url(r'dushi_name/', views.dushi_name),
    #现实
    url(r'xianshi/', views.xianshi),
    url(r'xianshi_name/', views.xianshi_name),
    #军事
    url(r'junshi/', views.junshi),
    url(r'junshi_name/', views.junshi_name),
    #历史
    url(r'lishi/', views.lishi),
    url(r'lishi_name/', views.lishi_name),
    #游戏
    url(r'youxi/', views.youxi),
    url(r'youxi_name/', views.youxi_name),
    #体育
    url(r'tiyu/', views.tiyu),
    url(r'tiyu_name/', views.tiyu_name),
    #科幻
    url(r'kehuan/', views.kehuan),
    url(r'kehuan_name/', views.kehuan_name),
    #灵异
    url(r'lingyi/', views.lingyi),
    url(r'lingyi_name/', views.lingyi_name),
    #女生网
    url(r'nvshengwang/', views.nvshengwang),
    url(r'nvshengwang_name/', views.nvshengwang_name),
    #二次元
    url(r'erciyuan/', views.erciyuan),
    url(r'erciyuan_name/', views.erciyuan_name),
]
