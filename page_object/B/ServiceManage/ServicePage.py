
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@class='ant-table-row ant-table-row-level-0']"),
}


class ServicePage(BasePage):
    """服务新增"""

    def get_ServicePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])