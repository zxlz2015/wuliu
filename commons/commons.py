# coding=utf-8

import datetime
import time
from logistics import config


def str_to_date(str):
    if str is None:
        return ''
    elif str == '':
        return ''
    return datetime.datetime.strptime(str, config.DATE_FORMAT)


def date_to_str(date):
    if isinstance(date, time.struct_time):
        return time.strftime(config.DATE_FORMAT, date)
    elif isinstance(date, datetime.datetime):
        return datetime.datetime.strftime(date, config.DATE_FORMAT)
    else:
        return None

