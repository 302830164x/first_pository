from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class QuickPrhCheckAccount(BasePage):
    """财务对账"""

    def get_QuickPrhCheckAccount_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
