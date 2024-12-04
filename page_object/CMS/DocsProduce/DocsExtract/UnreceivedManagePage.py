from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '资料列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class UnreceivedManagePage(BasePage):
    """待领取资料"""

    def get_UnreceivedManagePage_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
