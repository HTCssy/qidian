from django.contrib import admin

# Register your models here.
# Register your models here.
# import xadmin
#
# from .models import User
# # 全局配置
#
# from xadmin import views
#
#
# # 开启主题修改
# class BaseStyleSettings:
#     enable_themes = True
#     use_boot_swatch = True
#     reversion = True
#
#
# xadmin.site.register(views.BaseAdminView, BaseStyleSettings)
#
#
# class GlobalSettings:
#     site_title = '天猫后台管理系统'
#     site_footer = '千锋互联科技有限公司'
#     menu_style = 'accordion'  # 后台菜单样式修改
#
#
# xadmin.site.register(views.CommAdminView, GlobalSettings)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['u_id','username','password','create_time','is_status']
#     # 搜索
#     search_fields = ['u_id','username','is_status']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(User, AddressAdmin)

# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['banner_id', 'title','image','detail_url','order','create_time']
#     # 搜索
#     search_fields = ['banner_id']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(Banner, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['shop_id', 'name','sub_title','original_price','promote_price','stock','cate','create_date']
#     # 搜索
#     search_fields = ['name','sub_title','shop_id']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(Shop, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['car_id', 'number','shop','user_main','order','status']
#     # 搜索
#     search_fields = ['car_id','number','status']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(ShopCar, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['shop_img_id', 'shop','type']
#     # 搜索
#     search_fields = ['shop_img_id']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(ShopImage, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['sub_menu_id', 'name','cate']
#     # 搜索
#     search_fields = ['sub_menu_id','name']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(SubMenu, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['sub_menu2_id', 'name','sub_menu']
#     # 搜索
#     search_fields = ['sub_menu2_id','name']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(SubMenu2, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['review_id', 'content','create_date','shop','user_main']
#     # 搜索
#     search_fields = ['review_id','content','user_main']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(Review, AddressAdmin)
#
# class AddressAdmin:
#     # 后台界面要显示的字段
#     list_display = ['ORDER_STATUS', 'oid','order_code','address','post','receiver','mobile','user_message','create_date','pay_date','delivery_date','confirm_date','status','user_main']
#     # 搜索
#     search_fields = ['oid','user_main','mobile']
#     # 分页显示的条数
#     list_per_page = 10
# xadmin.site.register(Order, AddressAdmin)
