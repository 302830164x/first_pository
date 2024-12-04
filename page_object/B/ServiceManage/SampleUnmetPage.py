
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class SampleUnmetPage(BasePage):
    """服务未满足"""

    def get_SampleUnmetPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])