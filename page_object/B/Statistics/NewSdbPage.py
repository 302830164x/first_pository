from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@class='ant-table-row customer-row ant-table-row-level-0']"),
}


class NewSdbPage(BasePage):
    """新平台SDB"""

    def get_NewSdbPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
