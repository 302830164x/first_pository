from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '多选框': ('xpath', "//div[@id='type']//div[@role='combobox']"),
    '我发起的': ('xpath', "//li[contains(text(),'我发起的')]"),
    '已通过标签': ('xpath', "//span[contains(@class,'status-tag status-closed')][contains(text(),'已通过')]"),
}


class AuditCenterPage(BasePage):
    """审批中心"""

    def check_my_submit(self):
        """检查我发起的"""
        self.js_click(Locator['多选框'])
        sleep()
        self.js_click(Locator['我发起的'])

