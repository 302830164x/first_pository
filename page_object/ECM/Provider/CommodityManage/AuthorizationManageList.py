from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class AuthorizationManageList(BasePage):
    """ON授权管理"""

    def get_AuthorizationManageList_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
