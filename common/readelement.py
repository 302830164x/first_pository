#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

import yaml

from config.conf import cm


class Element(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))

    def dump(self, data):
        """追加写入数据"""
        # 先判断yaml文件有没有相同的元素数据，没有再追加写入
        with open(self.element_path, 'a', encoding='utf8') as f:
            for key in data:
                if self.data.get(key) is None:
                    yaml.dump({key: data[key]}, f, default_flow_style=False, encoding='utf8', allow_unicode=True)


if __name__ == '__main__':
    index = Element('SekormElement')
    print(index['首页3'])
