from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class AutoRegPending(BasePage):
    """待注册记录"""

    def get_AutoRegPending_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
