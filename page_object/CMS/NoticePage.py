from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class NoticePage(BasePage):
    """公告发布"""

    def get_NoticePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])