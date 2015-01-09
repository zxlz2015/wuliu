# coding=utf-8

from django.shortcuts import render_to_response

from ServerWeb import new_service


def chats(request):
    return render_to_response('chats/clientWeb.html')