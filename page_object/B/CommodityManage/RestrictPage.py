
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class RestrictPage(BasePage):
    """交易受限型号"""

    def get_RestrictPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])