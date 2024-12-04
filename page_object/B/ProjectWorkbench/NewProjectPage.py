
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row project-row ant-table-row-level-0')]"),
}



class NewProjectPage(BasePage):
    """新项目"""

    def get_NewProjectPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])