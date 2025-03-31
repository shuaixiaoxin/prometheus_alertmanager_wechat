# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/10/06
# @Author  : xiao xin
# @File    : settings.py
"""
# ======== 必填配置 ========
# Prometheus服务地址（包含端口）
PROMETHEUS_URL = "http://192.168.1.100:9090"

# AlertManager服务地址（包含端口）
ALERTMANAGER_URL = "http://192.168.1.101:9093"

# 企业微信机器人Webhook URL
WEIXIN = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=your-robot-key"

# ======== 可选配置 ========
# 需要@的企业微信成员ID（多个用英文逗号分隔）
WX_AT = []
