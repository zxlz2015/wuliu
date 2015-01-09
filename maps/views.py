# coding=utf-8

from django.shortcuts import render_to_response

from django.template import RequestContext


def index(request):
    return render_to_response('map/map.html',
                              {'x': 39.916527, 'y': 116.397128},
                              context_instance=RequestContext(request))


def list(request):
    return render_to_response('map/list.html',
                              context_instance=RequestContext(request))


def log_list(request):
    return render_to_response('map/log_list.html',
                              context_instance=RequestContext(request))


def orderList(request):
    return render_to_response('map/orderList.html',
                              context_instance=RequestContext(request))


def message(request):
    return render_to_response('map/message.html',
                              context_instance=RequestContext(request))


def error(request):
    return render_to_response('map/error.html',
                              context_instance=RequestContext(request))


def log(request):
    return render_to_response('map/log.html',
                              context_instance=RequestContext(request))


def test(request):
    return render_to_response('test/test.html',
                              context_instance=RequestContext(request))


def home(request):
    return render_to_response('map/home.html', context_instance=RequestContext(request))


def login(request):
    return render_to_response('map/login.html',
                              context_instance=RequestContext(request))


def register(request):
    return render_to_response('map/register.html',
                              context_instance=RequestContext(request))


def json(request):
    return render_to_response('json/message.json',
                              context_instance=RequestContext(request))

