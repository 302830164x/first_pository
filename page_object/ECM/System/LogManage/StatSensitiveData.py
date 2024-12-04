from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class StatSensitiveData(BasePage):
    """内部内容访问日志"""

    def get_StatSensitiveData_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
