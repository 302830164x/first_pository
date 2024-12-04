from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[@data-row-key]"),
}


class SrSearchListV2Page(BasePage):
    """客户行为记录"""

    def get_SrSearchListV2Page_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
