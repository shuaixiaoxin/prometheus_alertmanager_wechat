import requests
from flask import Flask, request, jsonify
from utils.times import utc_future_time
from utils.weixin import send_wechat_alert


app = Flask(__name__)
app.config.from_object('conf.settings')



@app.route('/')
def hello():
    return "Welcome to prometheus alertmanager!"



@app.route('/alarm', methods=['POST'])
def alarm():
    """发送告警"""
    try:
        data = request.json
        send_wechat_alert(app.config['WEIXIN'], data)
        return jsonify({"code": "0", "message": "消息发送成功"}), 200
    except Exception as e:
        app.logger.error(f"处理告警时发生错误: {e}")
        return jsonify({"code": "2", "message": str(e)}), 500


@app.route('/alerts', methods=['GET'])
def alerts():
    """
    查询所有告警信息
    :return:
    """
    response = requests.get(f"{app.config['ALERTMANAGER_URL']}/alerts")
    return jsonify(response.json())


@app.route('/silences', methods=['GET'])
def get_silences():
    """
    查看所有静默的告警列表
    :return:
    """
    response = requests.get(f"{app.config['ALERTMANAGER_URL']}/silences")
    return jsonify(response.json())


@app.route('/silence/<silence_id>', methods=['GET'])
def get_silence(silence_id):
    """
    查看某条静默的告警
    :param silence_id:
    :return:
    """
    response = requests.get(f"{app.config['ALERTMANAGER_URL']}/silence/{silence_id}")
    return jsonify(response.json())


@app.route('/silence/<job_value>/<minutes>', methods=['POST'])
def add_silence(job_value, minutes):
    """
    添加静默
    :return:
    """
    times = utc_future_time(minutes)
    data = {
        "matchers": [{"name": "job", "value": job_value, "isRegex": False}],
        "startsAt": times['startsAt'],
        "endsAt": times['endsAt'],
        "createdBy": "Flask System",
        "comment": "silence",
        "id": None
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{app.config['ALERTMANAGER_URL']}/silences", json=data, headers=headers)
    return jsonify(response.json()), response.status_code


@app.route('/silence/<silence_id>', methods=['DELETE'])
def delete_silence(silence_id):
    """
    删除静默
    :param silence_id:
    :return:
    """
    response = requests.delete(f"{app.config['ALERTMANAGER_URL']}/silence/{silence_id}")
    return {"code": response.status_code}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
