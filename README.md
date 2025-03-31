# Prometheus-AlertManager 企业微信告警机器人

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 目录
- [功能简介](#功能简介)
- [安装指南](#安装指南)
- [配置说明](#配置说明)
- [使用教程](#使用教程)

## 功能简介
将Prometheus的AlertManager告警通过企业微信机器人推送到指定群聊，支持：
- 告警消息格式化
- @指定成员或全体成员
- 多实例告警聚合
- 自定义消息模板

## 安装指南

### 环境要求
- Python 3.6+
- pip 包管理工具

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/yourname/prometheus_alertmanager_wechat.git
cd prometheus_alertmanager_wechat
```
2. 安装依赖
```bash
pip install -r requirements.txt
```

## 配置说明

### 主要配置文件 settings.py
```bash
# Prometheus服务地址（需包含http协议和端口）
PROMETHEUS_URL = "http://prometheus.example.com:9090"

# AlertManager服务地址
ALERTMANAGER_URL = "http://alertmanager.example.com:9093"

# 企业微信机器人Webhook
WEIXIN = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=your_key"

# 需要@的成员（多个用英文逗号分隔）
WX_AT = "['user1', 'user2']"  # 或 "all" 通知全体
```

## 使用教程

### 启动服务
```bash
python app.py
```

`可使用supervisor管理进程`

### alertmanager配置文件

```bash
webhook_configs:
      - url: 'http://127.0.0.1:5000/alarm'
```

`重启alertmanager进行测试验证`
