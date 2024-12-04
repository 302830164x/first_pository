from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class WmsCommentNopass(BasePage):
    """审核不通过列表"""

    def get_WmsCommentNopass_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
