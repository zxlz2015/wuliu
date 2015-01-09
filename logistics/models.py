# coding=utf-8
from django.db import models
import datetime


class Accounts(models.Model):
    login_name = models.CharField(max_length=30)
    login_password = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    accounts_img = models.URLField(null=True)
    status = models.IntegerField()
    email = models.EmailField(null=True)
    create_at = models.DateTimeField(default=datetime.datetime.now())


class Accessories(models.Model):
    name = models.CharField(max_length=30)
    access = models.CharField(max_length=200)
    enterprise_num = models.CharField(max_length=30)
    enterprise_img = models.ImageField(blank=True, null=True)
    enterprise_organization_num = models.CharField(max_length=30)
    enterprise_organization_img = models.ImageField(blank=True, null=True)
    accounts = models.ForeignKey(Accounts)


class LogisticsCar(models.Model):
    contact_num = models.CharField(max_length=30)
    contact_img = models.ImageField(blank=True, null=True)
    car_num = models.CharField(max_length=10)
    car_img = models.ImageField(blank=True, null=True)
    car_know_num = models.CharField(max_length=30, blank=True, null=True)
    car_engine_num = models.CharField(max_length=30, blank=True, null=True)
    car_driving_license_img = models.ImageField(blank=True, null=True)
    car_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    accounts = models.ForeignKey(Accounts)
    accessories = models.ManyToManyField(Accessories)


class LogisticsInfo(models.Model):
    accessories = models.ForeignKey(Accessories)    # 汽配企业(外键)
    logistics_car = models.ForeignKey(LogisticsCar, null=True)  # 物流车辆(外键)
    # create_at = models.DateTimeField(default=datetime.datetime.now())  # 创建时间
    # start_at = models.DateField(null=True)  # 开始时间
    # finish_at = models.DateField(null=True)  # 完成时间
    product_name = models.CharField(max_length=30)  # 产品名称
    product_weight = models.DecimalField(max_digits=10, decimal_places=2)   # 产品重量
    freight = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)   # 运费
    logistics_to_accessories_at = models.DateTimeField(default=datetime.datetime.now())    # 要求车辆到场时间
    loading_time = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)  # 装货预计时间
    logistics_to_destination_at = models.DateTimeField(default=datetime.datetime.now())    # 要求到达目的地时间
    destination_access = models.CharField(max_length=200)   # 目的地地址
    destination_contact = models.CharField(max_length=30)   # 目的地联系人
    destination_phone = models.CharField(max_length=20)  # 目的地联系人手机号
    description = models.TextField(null=True, blank=True)   # 备注
    status = models.IntegerField()  # 状态 -1.失败;0.撤销;1.发布;2.重发;3.开始;4.到厂;5.装货;6.离厂;7.到达;8.卸货;9.完成;


class LogisticsInfoLog(models.Model):
    '''
    日志内容格式应该为:
    发布公司:XXX,
    发布人:XXX,
    发布账号:XXX,
    产品名称:XXX，
    产品重量:XXX,
    运费:XXX,
    要求车辆到厂时间:XXX,
    装货预估时间:XXX,
    要求到达目的地时间:%s,
    目的地地址:XXX,
    目的地联系人:XXX,
    目的地联系人手机号:XXX,
    备注:XXX,
    状态:XXX,
    记录时间:XXX，
    '''
    create_at = models.DateTimeField()  # 创建时间
    logistics_info = models.ForeignKey(LogisticsInfo)   # 物流信息
    content = models.TextField()    # 日志内容
    status = models.IntegerField()  # 物流状态


class CommonlyUseInfo(models.Model):
    logistics_info = models.ForeignKey(LogisticsInfo)
    accessories = models.ForeignKey(Accessories)
    name = models.CharField(max_length=30)


class PendingInfo(models.Model):
    logistics_info = models.ForeignKey(LogisticsInfo)
    logistics_car = models.ForeignKey(LogisticsCar)
    message = models.TextField(null=True)


class Messages(models.Model):
    reply = models.ForeignKey(Accounts, null=True)
    send_id = models.CharField(max_length=50)
    receive_id = models.CharField(max_length=50)
    content = models.TextField()
    send_at = models.DateTimeField(default=datetime.datetime.now())
    status = models.IntegerField(default=1)


class CarOpinionFeedback(models.Model):
    logistics_car = models.ForeignKey(LogisticsCar)
    title = models.CharField(max_length=50)
    content = models.TextField()
    reason = models.IntegerField()


class AccessoriesOpinionFeedback(models.Model):
    accessories = models.ForeignKey(Accessories)
    title = models.CharField(max_length=50)
    content = models.TextField()
    reason = models.IntegerField()
