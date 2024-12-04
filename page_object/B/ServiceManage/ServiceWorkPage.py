from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@data-row-key]"),
}


class ServiceWorkPage(BasePage):
    """服务工作台"""

    def get_ServiceWorkPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
