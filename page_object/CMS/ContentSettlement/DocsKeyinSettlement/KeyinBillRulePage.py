from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//div[@class='ant-table-scroll']//tr[@data-row-key]"),
}


class KeyinBillRulePage(BasePage):
    """资料keyin规则配置"""

    def get_KeyinBillRulePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
