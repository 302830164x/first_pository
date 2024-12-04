from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class BillSourcePage(BasePage):
    """资讯计费原始报表"""

    def get_BillSourcePage_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
