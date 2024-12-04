from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class EcpTaskJobTrigger(BasePage):
    """任务调度日志"""

    def get_EcpTaskJobTrigger_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
