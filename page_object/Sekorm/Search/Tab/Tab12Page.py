from common.readelement import Element
from page.basepage import BasePage

Locator = {
    'ON名称': ('xpath', "//a[@class='model-on']"),
}


class Tab12Page(BasePage):
    """tab=12的门楣"""

    def check_tab12_list_num(self):
        """检查tab12页面列表数据量"""
        return self.elements_num(Locator['ON名称'])
