from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//div[@class='ant-table-scroll']//tr[@data-row-key]"),
}


class TransBillRulePage(BasePage):
    """翻译规则配置"""

    def get_TransBillRulePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
