from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@class='ant-table-row ant-table-row-level-0']"),
}


class SearchTermStatisticsPage(BasePage):
    """搜索词统计"""

    def get_SearchTermStatisticsPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
