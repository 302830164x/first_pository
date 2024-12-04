
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class ServiceProcessParentChildPage(BasePage):
    """新样品申请"""

    def get_ServiceProcessParentChildPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])