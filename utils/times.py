# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/10/06
# @Author  : xiao xin
# @File    : times.py
"""
from datetime import datetime, timedelta, timezone


def utc_to_bj(utc_time):
    """
    utc字符串时间转utc+8
    :param utc_time:
    :return:
    """
    try:
        utc_time = datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        beijing_time = utc_time + timedelta(hours=8)
        return beijing_time.strftime("%Y/%m/%d %H:%M:%S")
    except Exception as e:
        return utc_time


def utc_future_time(minutes):
    """
    utc未来时间
    :param minutes:
    :return:
    """
    now = datetime.utcnow()
    ends_at = now + timedelta(minutes=int(minutes))
    data = {"startsAt": now.isoformat() + "Z", "endsAt": ends_at.isoformat() + "Z"}
    return data


def format_time(timestamp):
    """
    格式化时间
    :param timestamp:
    :return:
    """
    timestamp_dt = datetime.utcfromtimestamp(timestamp) + timedelta(hours=8)
    formatted_time = timestamp_dt.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time


def utc8_to_timestamp(time_str):
    """
    utc+8时间转为时间戳
    :param time_str:
    :return:
    """
    dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    dt = dt.replace(tzinfo=timezone.utc)
    timestamp = dt.timestamp()
    return timestamp
