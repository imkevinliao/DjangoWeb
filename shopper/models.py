from django.db import models

# Create your models here.
from django.db import models

STATE = (
    ('待支付','待支付'),
    ('已支付','已支付'),
    ('发货中','发货中'),
    ('已签收','已签收'),
    ('退货中','退货中'),

)

class CartInfos(models.Model):
    id = models.AutoField(primary_key = True)
    quantity = models.IntegerField('购买数量')
    commodityInfos_id=models.IntegerField('商品ID')
    user_id = models.IntegerField('用户ID')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural='购物车'

class OrderInfos(models.Model):
    id = models.AutoField(primary_key=True)