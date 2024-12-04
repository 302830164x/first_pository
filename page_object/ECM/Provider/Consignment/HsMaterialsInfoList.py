from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class HsMaterialsInfoList(BasePage):
    """厚声物料表"""

    def get_HsMaterialsInfoList_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
