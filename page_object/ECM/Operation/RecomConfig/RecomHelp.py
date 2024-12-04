from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class RecomHelp(BasePage):
    """推荐帮助信息"""

    def get_RecomHelp_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
