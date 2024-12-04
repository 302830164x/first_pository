from page.basepage import BasePage

Locator = {
    '页面iframe': ('xpath', "//div[@id='reactContent']//iframe"),
    '标题': ('xpath', "//div[@class='ant-card-head-title']"),
}


class QuickPrhPayManage(BasePage):
    """待确认收款"""

    def get_QuickPrhPayManage_text(self):
        """获取列表内容"""
        self.switch_to_iframe(Locator['页面iframe'])
        text1 = self.element_text(Locator['标题'])
        text2 = self.get_assert_text('span', '订单号')
        self.switch_to_content()
        return text1, text2
