import logging
import sys

import colorlog

from config.conf import cm


class Loggings:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            # 日志格化字符串
            console_fmt = '%(log_color)s %(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'
            file_fmt = '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

            # 控制台输出不同级别日志颜色设置
            color_config = {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'purple',
            }

            console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
            file_formatter = logging.Formatter(fmt=file_fmt)

            # 创建一个handle写入文件
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler(stream=sys.stdout)
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            fh.setFormatter(file_formatter)
            ch.setFormatter(console_formatter)

            # # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)


log = Loggings().logger

if __name__ == '__main__':
    log.info('lalaland')
