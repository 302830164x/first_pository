from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//li[@class='ant-list-item']"),
}


class ProductFunDecPage(BasePage):
    """功能介绍"""

    def get_ProductFunDecPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
