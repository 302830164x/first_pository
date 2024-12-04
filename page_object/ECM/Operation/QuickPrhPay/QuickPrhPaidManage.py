from page.basepage import BasePage

Locator = {
    '页面iframe': ('xpath', "//div[@id='reactContent']//iframe"),
    '标题': ('xpath', "//div[@class='ant-card-head-title']"),
}


class QuickPrhPaidManage(BasePage):
    """已确认收款"""

    def get_QuickPrhPaidManage_text(self):
        """获取列表内容"""
        self.switch_to_iframe(Locator['页面iframe'])
        text1 = self.element_text(Locator['标题'])
        text2 = self.get_assert_text('a', '详情')
        self.switch_to_content()
        return text1, text2
