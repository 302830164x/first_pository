from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody/tr"),
}


class MemModifyContactStat(BasePage):
    """手机邮箱修改统计"""

    def get_MemModifyContactStat_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
