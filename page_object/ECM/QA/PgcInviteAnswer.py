from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class PgcInviteAnswer(BasePage):
    """邀请解答记录"""

    def get_PgcInviteAnswer_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
