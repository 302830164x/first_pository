
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '资料列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class PreviewDetailPage(BasePage):
    """预览日志明细"""

    def get_PreviewDetailPage_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['资料列表'])