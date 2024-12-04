from page_object.Sekorm.SekormCommon import SekormCommon

Locator = {
    '服务标题': ('xpath', "//span[@class='select-help-title']"),
    '提问内容': ('xpath', "//textarea[@id='askQuestion']"),
    '上传图片': ('xpath', "//li[@id='askAddImg']"),
    '公司': ('xpath', "//input[@id='business_companyName']"),
    '工作邮箱': ('xpath', "//input[@id='business_email']"),
    '姓名': ('xpath', "//input[@id='business_trueName']"),
    '联系电话': ('xpath', "//input[@id='business_mobile']"),
    '提交按钮': ('xpath', "//input[@id='submit_form']"),
}


class AskServicePage(SekormCommon):
    """技术问答服务页"""

    def check_AskServicePage(self):
        """检查 技术问答服务页"""
        for i in Locator:
            self.move_to_element(Locator[i])
        self.is_click(Locator['提交按钮'])
        return self
