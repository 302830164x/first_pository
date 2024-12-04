
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class BillRulePage(BasePage):
    """资讯计费规则配置"""

    def get_BillRulePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
