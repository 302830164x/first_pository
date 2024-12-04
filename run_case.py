#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import subprocess


def main():
    """主函数"""
    steps = [
        # 清除allure-results中历史的原始pytest报告数据
        # --dist=loadscope pytest-xdist默认是无序执行的，可以通过 --dist 参数来控制顺序,将按照同一个模块module下的函数和同一个测试类class下的方法来分组
        # --reruns 3 --reruns-delay 3 失败用例重跑3次，--reruns-delay 3 每次等待3秒再重跑，是pytest-rerunfailures插件的参数
        "pytest --alluredir report/allure-results --clean-alluredir -n 3 --dist=loadscope --reruns 1 --reruns-delay 1",
        # "allure generate report/allure-results -c -o report/allure-report",  # 导出HTML报告到allure-report
        # "allure open report/allure-report"  # 在浏览器打开HTML报告
    ]
    for step in steps:
        subprocess.run("call " + step, shell=True)  # 在shell新开进程执行上述命令


if __name__ == "__main__":
    main()
