from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@data-row-key]"),
}


class DWDistributionPoolPage(BasePage):
    """DW分配池"""

    def get_DWDistributionPoolPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
