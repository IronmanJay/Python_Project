from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from django.db import models

# Create your models here.

class AddressManager(models.Manager):
    """地址模型管理类"""
    def get_default_address(self, user):
        """获取用户的默认地址"""

        # 获取用户默认收货地址
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist as e:
            address = None
        return address

class User(AbstractUser, BaseModel):
    '''用户模型类'''


    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class AddressManager(models.Manager):
    '''地址模型管理器类'''
    # 1、改变原有查询的结果集:all()
    # 2、封装方法:用于操作模型类对应的数据表（增删改查）
    def get_default_address(self,user):
        '''获取用户的默认收货地址'''
        # self.model:获取self对象所在的模型类
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            # 不存在默认收货地址
            address = None
        return address

class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收货地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器对象
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name