from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class OperateList(BasePage):
    """运营内容管理"""

    def get_OperateList_list_num(self):
        """获取列表内容条数"""
        sleep(10)
        return self.elements_num(Locator['列表'])
