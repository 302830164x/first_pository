

from common.readelement import Element
from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '列表': ('xpath', "//div[@class='BaseTable__row']"),
}


class OnFirstConsumePage(BasePage):
    """第一次消费ON清单"""

    def get_OnFirstConsumePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])