from page.basepage import BasePage

Locator = {
    '确认弹窗-服务标题': ('xpath', "//div[@class='modal-header']/h3"),
    '确认弹窗-ON名称': ('xpath', "//div[@class='join-cart']//h3[@class='on']"),
    '确认弹窗-ON厂牌': ('xpath', "//div[@class='join-cart']//p[@class='brand']"),
    '确认弹窗-申请数量': ('xpath', "//input[@id='trade_number']"),
    '确认弹窗-单价': ('xpath', "//p[@id='allow_price']"),
    '确认弹窗-现货': ('xpath', "//p[@id='allow_sall']"),
    '确认弹窗-仓库': ('xpath', "//p[@id='pay_local']"),
    '确认弹窗-预计交期': ('xpath', "//div[@id='delivery']"),
    '确认弹窗-订单小计': ('xpath', "//i[@id='price']"),
    '确认弹窗-打开型号清单': ('xpath', "//a[@id='sample_cart_main']"),
    '确认弹窗-加入型号清单': ('xpath', "//a[@id='join_cart']"),
    '确认弹窗-立即申请': ('xpath', "//button[@id='trade_account']"),
    '确认弹窗-提示语': ('xpath', "//span[@class='sample-apply-tips']"),
    # 服务填写及核对页面
    '服务标题': ('xpath', "//span[@class='select-help-title']"),
    '服务简介': ('xpath', "//div[contains(@class,'cd-service-content')]"),
    '型号': ('xpath', "//div[@id='pnCode']"),
    '厂牌': ('xpath', "//div[@id='brand']"),
    '单价': ('xpath', "//span[@id='singlePrice']"),
    '现货': ('xpath', "//span[@id='availableSale']"),
    '需求数量': ('xpath', "//input[@name='awardNum']"),
    '期望交期': ('xpath', "//input[@name='strExpectDate']"),
    '添加型号': ('xpath', "//a[contains(text(),'去添加更多型号>')]"),
    '项目名称': ('xpath', "//input[@id='projectName']"),
    '需求描述': ('xpath', "//textarea[@id='demandDesc']"),
    '收货信息': ('xpath', "//div[contains(@class,'service-ads')]"),
    '公司': ('xpath', "//input[@id='business_companyName']"),
    '工作邮箱': ('xpath', "//input[@id='business_email']"),
    '姓名': ('xpath', "//input[@id='business_trueName']"),
    '联系电话': ('xpath', "//input[@id='business_mobile']"),
    '申请须知': ('xpath', "//div[@class='note-values']"),
    '提交': ('xpath', "//input[@id='submit_form']"),
    '必填提示': ('xpath', "//p[@class='vformMsnReg']"),
}


class SampleApplicationPage(BasePage):
    """样品申请服务页"""

    def check_sample_join_cart(self):
        """样品申请服务页"""
        text1 = self.element_text(Locator['确认弹窗-服务标题'])
        text2 = self.element_text(Locator['确认弹窗-提示语'])
        self.move_to_element(Locator['确认弹窗-ON名称'])
        self.move_to_element(Locator['确认弹窗-ON厂牌'])
        self.input_text(Locator['确认弹窗-申请数量'], 1)
        self.move_to_element(Locator['确认弹窗-仓库'])
        self.move_to_element(Locator['确认弹窗-订单小计'])
        self.move_to_element(Locator['确认弹窗-打开型号清单'])
        self.move_to_element(Locator['确认弹窗-加入型号清单'])
        self.is_click(Locator['确认弹窗-立即申请'])
        return text1, text2

    def check_SampleApplicationPage(self):
        """样品申请提交核对页"""
        for i, key in enumerate(Locator):
            if 12 < i < 31:
                self.move_to_element(Locator[key])
        self.is_click(Locator['提交'])
        text1 = self.element_text(Locator['服务标题'])
        text2 = self.element_text(Locator['必填提示'])
        return text1, text2
