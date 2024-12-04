from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//p[contains(@class,'notify-center-list-p')]"),
}


class NotifyCenterPage(BasePage):
    """通知中心"""

    def get_NotifyCenterPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
