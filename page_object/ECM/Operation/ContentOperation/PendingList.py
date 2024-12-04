from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class PendingList(BasePage):
    """待处理内容"""

    def get_PendingList_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
