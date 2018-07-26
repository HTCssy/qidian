import os
import time

from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    #用户名
    username = models.CharField(unique=True, max_length=100)
    #密码
    password = models.CharField(max_length=255)
    #手机号
    iphone = models.CharField(max_length=255)
    #邮件
    email = models.CharField(max_length=255)
    #0是男  1是女
    gender = models.IntegerField(default=0)
    #申请时间
    create_time = models.DateTimeField(auto_now_add=True)
    #0存在  1删除
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = 'user'

"""
给图片重名了
"""
class ImageStorage(FileSystemStorage):
    IMG_PREFIX = 'IMG_'
    FILE_TIME = time.strftime('%Y%m%d%H%M%S')
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super().__init__(location, base_url)
        # 重写 _save方法

    # uploaad/img/img_afsfsfds.png
    # 修改文件的名称
    def _save(self, name, content):
        # 文件扩展名
        ext_name = name[name.rfind('.'):]
        # 文件目录
        image_path = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        image_name = self.IMG_PREFIX + self.FILE_TIME + ext_name
        image_file = os.path.join(image_path, image_name)
        # 调用父类方法
        return super()._save(image_file, content)

class UserDetails(models.Model):
    ud_id = models.AutoField(primary_key=True)
    #昵称
    nickname = models.CharField(max_length=100)
    #图像
    image = models.ImageField(max_length=100, upload_to='upload/img/%Y%m%d', storage=ImageStorage(), default=u"static/img/2.png")
    #生日
    birthday = models.DateField(default='1970-01-01')
    #地区
    area = models.CharField(max_length=100)
    #个人介绍
    intro = models.TextField()
    #关联用户
    user = models.ForeignKey(User, models.CASCADE)
    #0存在  1删除
    is_delete = models.IntegerField(default=0)

    #自定义表名
    class Meta:
        db_table = 'user_details'

