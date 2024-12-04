from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class ForeignExchangeRatePage(BasePage):
    """常用外汇汇率"""

    def get_ForeignExchangeRatePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
