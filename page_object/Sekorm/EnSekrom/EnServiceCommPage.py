from page.basepage import BasePage

Locator = {
    '服务标题': ('xpath', "//span[@class='select-help-title']"),
    '服务简介': ('xpath', "//div[@class='cd-content']"),
    '型号': ('xpath', "//div[@id='pnCode']"),
    '厂牌': ('xpath', "//div[@id='brand']"),

    '需求数量': ('xpath', "//input[@id='applyNum']"),
    '期望交期': ('xpath', "//input[@id='expect_date']"),
    '需求描述': ('xpath', "//textarea[@id='projectDesc']"),
    '公司': ('xpath', "//input[@id='business_company']"),
    '工作邮箱': ('xpath', "//input[@id='business_email']"),
    '姓名': ('xpath', "//input[@id='business_name']"),
    '验证码': ('xpath', "//input[@id='business_mobileCode']"),
    '提交': ('xpath', "//input[@id='submit_form']"),
    '必填提示': ('xpath', "//p[@class='vformMsnReg companyErrMsg']"),
}


class EnServiceCommPage(BasePage):
    """英文站通用服务页"""

    def check_RFQ_layout(self):
        """RFQ服务页"""
        for i, key in enumerate(Locator):
            if i < 12:
                self.move_to_element(Locator[key])
        self.is_click(Locator['提交'])
        text1 = self.element_text(Locator['服务标题'])
        text2 = self.element_text(Locator['必填提示'])
        return text1, text2
