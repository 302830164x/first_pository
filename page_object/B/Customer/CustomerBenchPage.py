from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//div[@class='custom-info line-ellipsis']"),
}


class CustomerBenchPage(BasePage):
    """全部客户"""

    def get_CustomerBenchPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
