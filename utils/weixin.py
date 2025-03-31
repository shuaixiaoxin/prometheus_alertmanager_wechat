import json
import requests
from conf.settings import WX_AT


def send_wechat_alert(webhook_url, alert_data):
    """
    发送企业微信机器人告警消息
    :param webhook_url: 企业微信机器人Webhook地址
    :param alert_data: Prometheus告警数据
    """
    # 构造Markdown消息内容
    markdown_content = "### Prometheus告警通知\n"

    # 遍历所有告警条目
    for alert in alert_data.get('alerts', []):
        status = alert.get('status', 'unknown')
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})

        # 基础信息
        alert_name = labels.get('alertname', '未知告警')
        instance = labels.get('instance', '未知实例')
        severity = labels.get('severity', 'warning')

        # 状态颜色标识
        status_color = "告警状态: <font color=\"red\">**FIRING**</font>" if status == 'firing' else \
            "<font color=\"green\">**RESOLVED**</font>"

        # 构造告警块
        markdown_content += f"\n**[{severity.upper()}] {alert_name}**\n"
        markdown_content += f"- {status_color}\n"
        markdown_content += f"- 实例: {instance}\n"

        # 添加注解信息
        if 'summary' in annotations:
            markdown_content += f"- 摘要: {annotations['summary']}\n"
        if 'description' in annotations:
            markdown_content += f"- 详情: {annotations['description']}\n"

        # 添加其他标签（排除常见已用标签）
        other_labels = {k: v for k, v in labels.items()
                        if k not in ['alertname', 'instance', 'severity', 'job']}
        if other_labels:
            markdown_content += "- 其他标签:\n"
            for k, v in other_labels.items():
                markdown_content += f"  - {k}: {v}\n"

        # 添加告警链接（如果有）
        if 'generatorURL' in alert:
            markdown_content += f"- [查看告警详情]({alert['generatorURL']})\n"

        markdown_content += "\n---\n"
    if WX_AT:
        result = ''.join([f'<@{name}>' for name in WX_AT])
        markdown_content += result

    # 构造请求数据
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": markdown_content
        }
    }

    try:
        response = requests.post(
            url=webhook_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        if response.status_code != 200:
            print(f"消息发送失败，状态码: {response.status_code}, 响应内容: {response.text}")
            return False
        return True
    except Exception as e:
        print(f"请求发送失败: {str(e)}")
        return False

if __name__ == '__main__':
    pass