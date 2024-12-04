
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class ChancePoolPage(BasePage):
    """全部需求/方案"""

    def get_ChancePoolPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])