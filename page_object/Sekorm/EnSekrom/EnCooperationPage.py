from page.basepage import BasePage

Locator = {
    '背景模块': ('xpath', "//div[@id='join_sekorm']"),
    '填写表单': ('xpath', "//div[@class='partner-join']"),
    '模块标题': ('xpath', "//div[@class='collaborative-object']/h4"),
    '提交按钮': ('xpath', "//button[normalize-space()='Apply Now']"),
    '提示语': ('xpath', "//p[@id='tmpComode-error']"),
    '底部申请按钮': ('xpath', "//a[normalize-space()='Apply Now']"),
}


class EnCooperationPage(BasePage):
    """英文站合作页"""

    def check_en_cooperation_layout(self):
        """检查英文站合作页布局"""
        self.move_to_element(Locator['背景模块'])
        self.move_to_element(Locator['填写表单'])
        self.move_to_element(Locator['提交按钮'])
        self.move_to_element(Locator['底部申请按钮'])
        return self.element_text(Locator['模块标题'])

    def check_en_cooperation_button(self):
        """检查英文站合作页提交按钮"""
        self.is_click(Locator['提交按钮'])
        return self.element_text(Locator['提示语'])
