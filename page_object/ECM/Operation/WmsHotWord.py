from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class WmsHotWord(BasePage):
    """搜索热词设置"""

    def get_WmsHotWord_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
