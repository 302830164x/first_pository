from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class KeywordNewShelvesContent(BasePage):
    """货架内容查看"""

    def get_KeywordNewShelvesContent_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
