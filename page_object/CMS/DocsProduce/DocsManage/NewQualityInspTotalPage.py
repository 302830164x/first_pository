
from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class NewQualityInspTotalPage(BasePage):
    """新质检数据总览"""

    def get_NewQualityInspTotalPage_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])
