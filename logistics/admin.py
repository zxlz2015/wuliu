# coding=utf-8

from django.contrib import admin

from logistics.models import Accounts, Accessories, AccessoriesOpinionFeedback
from logistics.models import LogisticsCar, LogisticsInfo, LogisticsInfoLog, CarOpinionFeedback
from logistics.models import CommonlyUseInfo, Messages, PendingInfo


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('login_name', 'name', 'phone', 'email')
    search_fields = ('login_name', 'name', 'phone', 'email')


class AccessoriesAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('name', 'access', 'enterprise_num', 'enterprise_organization_num')
    # 可以查询的字段
    search_fields = ('name', 'access', 'enterprise_num', 'enterprise_organization_num')
    # 选择外键
    raw_id_fields = ('accounts',)


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(AccessoriesOpinionFeedback)
admin.site.register(LogisticsCar)
admin.site.register(LogisticsInfo)
admin.site.register(LogisticsInfoLog)
admin.site.register(CarOpinionFeedback)
admin.site.register(CommonlyUseInfo)
admin.site.register(Messages)
admin.site.register(PendingInfo)
