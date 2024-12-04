from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class WmsCouponDetail(BasePage):
    """奖券统计"""

    def get_WmsCouponDetail_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
