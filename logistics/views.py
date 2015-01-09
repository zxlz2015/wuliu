# coding=utf-8

from django.shortcuts import render_to_response, Http404, HttpResponse

import datetime
import config
from commons import commons
from logistics.models import LogisticsInfo, LogisticsInfoLog, Accessories
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            # 获得当前登录用户
            accessories = Accessories.objects.get(id='1')
        except Exception:
            raise Exception
        if accessories:
            # 发布物流信息
            logistic_info = LogisticsInfo()
            logistic_info.accessories = accessories
            logistic_info.product_name = request.POST.get('product_name', None)
            logistic_info.product_weight = float(request.POST.get('product_weight'))
            logistic_info.freight = request.POST.get('freight')
            logistic_info.logistics_to_accessories_at = commons.str_to_date(
                request.POST.get('logistics_to_accessories_at'))
            logistic_info.loading_time = request.POST.get('loading_time')  # 应该是float，用户输入，以小时为单位
            logistic_info.logistics_to_destination_at = commons.str_to_date(
                request.POST.get('logistics_to_destination_at'))
            logistic_info.destination_access = request.POST.get('destination_access')
            logistic_info.destination_contact = request.POST.get('destination_contact')
            logistic_info.destination_phone = request.POST.get('destination_phone')
            logistic_info.description = request.POST.get('description')
            logistic_info.status = 1  # 状态为发布
            logistic_info.save()

            # 物流信息为发布状态的日志
            date_now = datetime.datetime.now()  # 获得当前时间
            print(date_now)
            content = u'发布公司:%s,' % accessories.name
            content += u'发布人:%s,' % accessories.accounts.name
            content += u'发布账号:%s,' % accessories.accounts.login_name
            content += u'发布时间:%s,' % date_now
            content += u'产品名称:%s,' % logistic_info.product_name
            content += u'产品重量:%s,' % str(logistic_info.product_weight)
            content += u'运费:%s,' % str(logistic_info.freight)
            content += u'要求车辆到厂时间:%s,' % commons.date_to_str(logistic_info.logistics_to_accessories_at)
            content += u'装货预估时间:%s小时,' % str(logistic_info.loading_time)
            content += u'要求到达目的地时间:%s,' % commons.date_to_str(logistic_info.logistics_to_destination_at)
            content += u'目的地地址:%s,' % logistic_info.destination_access
            content += u'目的地联系人:%s,' % logistic_info.destination_contact
            content += u'目的地联系人手机号:%s,' % logistic_info.destination_phone
            content += u'备注:%s,' % logistic_info.description
            content += u'状态:%s,' % unicode(config.LOGISTICS_INFO_STATUS.get(1), "utf-8")
            content += u'记录时间:%s!' % date_now

            # s = ''.join(['aaaa', 'cccc', 'dddd%s' % 'a', 'eee', 'ff'])
            logistics_info_logging(logistic_info, content, 1)

            return render_to_response('logistics/message.html', {'logistic_info': logistic_info})
        else:
            return render_to_response('logistics/error.html', {'message': '用户不存在，请登录！'})
    else:
        return render_to_response('logistics/home.html')


def logistics_info_logging(logistic_info, content, status):
    date_now = datetime.datetime.now()
    print(date_now)
    logistic_info_log = LogisticsInfoLog()
    logistic_info_log.logistics_info = logistic_info
    logistic_info_log.create_at = date_now
    logistic_info_log.content = content
    logistic_info_log.status = status
    logistic_info_log.save()


def message(request):
    return render_to_response('logistics/message.html')


def logistics_list(request):
    return render_to_response('logistics/list.html')


def logistics_log(request):
    return render_to_response('logistics/log.html')


def logistics_map(request):
    return render_to_response('logistics/map.html')


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', locals())


def mypage(request):
    current_section = 'mysection test'
    title = 'mypage test'
    return render_to_response('mypage.html', locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('dateapp/hours_ahead.html', {
        'hour_offset': offset,
        'next_time': dt,
    })


def current_url_view_good(request):
    '''
    request.path	除域名以外的请求路径，以正斜杠开头	"/hello/"
    request.get_host()	主机名（比如，通常所说的域名）	"127.0.0.1:8000" or "www.example.com"
    request.get_full_path()	请求路径，可能包含查询字符串	"/hello/?print=true"
    request.is_secure()	如果通过HTTPS访问，则此方法返回True， 否则返回False	True 或者 False
    '''
    return HttpResponse('Welcome to the page at %s %s' % (request.get_host(), request.path))


def ua_display_good1(request):
    '''
    HTTP_REFERER，进站前链接网页，如果有的话。 （请注意，它是REFERRER的笔误。）
    HTTP_USER_AGENT，用户浏览器的user-agent字符串，如果有的话。 例如： "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17" .
    REMOTE_ADDR 客户端IP，如："12.345.67.89" 。(如果申请是经过代理服务器的话，那么它可能是以逗号分割的多个IP地址，如："12.345.67.89,23.456.78.90" 。)
    '''
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)


def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


def display_meta(request):
    '''
    简单的view函数来显示 request.META 的所有数据，
    这样就知道里面有什么了。
    '''
    values = request.META.items()
    values.sort()
    return render_to_response('display_meta.html', {'values': values})


def foobar_view(request, template_name):
    return render_to_response(template_name)