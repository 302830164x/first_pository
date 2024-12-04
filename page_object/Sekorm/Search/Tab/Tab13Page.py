from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '搜索列表': ('xpath', "//div[@id='multiple-search_0']/div"),
}


class Tab13Page(BasePage):
    """tab=13的门楣"""

    def check_tab13_list_num(self):
        """检查tab13页面列表数据量"""
        return self.elements_num(Locator['搜索列表'])
