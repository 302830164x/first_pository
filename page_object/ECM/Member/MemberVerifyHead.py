from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "(//li[@class='portrait-pass-msg'])"),
}


class MemberVerifyHead(BasePage):
    """头像审核"""

    def get_MemberVerifyHead_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
