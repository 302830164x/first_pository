import json
import requests
from utils import times
from utils.logger import log

# 用于调试 https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=11496470-86a3-47a8-9f9b-4b7f6f176cf6
# 正式使用 https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fcf215bf-ba11-4055-8851-85400d449d04

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fcf215bf-ba11-4055-8851-85400d449d04"
header = {
    'Content-Type': 'application/json',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def send_start(total_testcase):
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content":
                '''<font color=\"info\">UI自动化脚本开始执行</font>，请相关同事注意。
                >开始时间：<font color=\"comment\">{}</font>
                >UI用例总数：<font color=\"comment\">{}条</font>
                >[项目地址](http://172.16.9.105:8889/job/UI自动化脚本/)'''.format(times.dt_strftime("%Y-%m-%d %H:%M:%S"),
                                                                         total_testcase)
        }
    }
    requests.post(url=url, headers=header, data=json.dumps(payload))
    log.info('企业微信通知发送成功,开始执行用例')


def send_ending(cost_time, total_testcase, passed, failed, error):
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content":
                '''<font color=\"info\">UI自动化脚本执行完毕</font>，请相关同事注意。
                >执行时长：<font color=\"comment\">{}</font>
                >UI用例总数：<font color=\"comment\">{}条</font>，通过 <font color=\"info\">{}条</font>，失败 <font color=\"warning\">{}条</font>，异常 <font color=\"warning\">{}处</font>
                >[项目地址](http://172.16.9.105:8889/job/UI自动化脚本/)
                >[测试报告](http://172.16.9.105:8889/job/UI自动化脚本/allure/)'''.format(
                    cost_time, total_testcase, passed, failed, error)
        }
    }
    requests.post(url=url, headers=header, data=json.dumps(payload))
    log.info('企业微信通知发送成功，开始生成报告')
