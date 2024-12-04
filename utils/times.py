#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import time
from functools import wraps
from datetime import datetime, timedelta


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt="%Y%m%d"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("校验元素Done！用时%.3f秒！" % (timestamp() - start))
        return res

    return wrapper


def calculate_duration(start_time, end_time):
    """根据时间戳计算消耗时长"""

    start = datetime.fromtimestamp(start_time)
    end = datetime.fromtimestamp(end_time)
    duration = end - start

    # 将总秒数转换为小时、分钟和秒钟
    hours = duration // timedelta(hours=1)
    minutes = (duration % timedelta(hours=1)) // timedelta(minutes=1)
    seconds = (duration % timedelta(minutes=1)) // timedelta(seconds=1)
    duration_formatted = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return duration_formatted


if __name__ == '__main__':
    # 示例用法
    start_timestamp = timestamp()
    sleep(5)
    end_timestamp = timestamp()

    print(calculate_duration(start_timestamp, end_timestamp))

