from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class CommodityManageList(BasePage):
    """商品管理"""

    def get_CommodityManageList_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
