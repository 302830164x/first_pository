from page.basepage import BasePage

Locator = {
    # 服务填写及核对页面
    '服务标题': ('xpath', "//span[@class='select-help-title']"),
    '服务简介': ('xpath', "//div[contains(@class,'cd-service-content')]"),
    '型号': ('xpath', "//*[@id='pnCode']"),
    '厂牌': ('xpath', "//*[@id='brand']"),
    '需求数量': ('xpath', "//input[@class='pcs ask-price-num']"),
    '期望交期': ('xpath', "//input[@class='date-input ask-price-num expect_date']"),
    '添加型号': ('xpath', "//a[contains(text(),'去添加更多型号>')]"),
    '需求描述': ('xpath', "//textarea[@id='demandDesc']"),
    '公司': ('xpath', "//input[@id='business_companyName']"),
    '工作邮箱': ('xpath', "//input[@id='business_email']"),
    '姓名': ('xpath', "//input[@id='business_trueName']"),
    '联系电话': ('xpath', "//input[@id='business_mobile']"),
    '提交': ('xpath', "//input[@id='submit_form']"),
    '必填提示': ('xpath', "//p[@class='vformMsnReg companyAndNameErrMsg']"),
    # 确认弹窗
    '确认弹窗-服务标题': ('xpath', "//div[@class='modal-header']/h3"),
    '确认弹窗-ON名称': ('xpath', "//div[@class='join-cart']//h3[@class='on']"),
    '确认弹窗-ON厂牌': ('xpath', "//div[@class='join-cart']//p[@class='brand']"),
    '确认弹窗-申请数量': ('xpath', "//input[@id='trade_number']"),
    '确认弹窗-单价': ('xpath', "//p[@id='allow_price']"),
    '确认弹窗-仓库、现货和交期': ('xpath', "//p[@id='pay_local']"),
    '确认弹窗-订单小计': ('xpath', "//i[@id='price']"),
    '确认弹窗-打开型号清单': ('xpath', "//a[@id='sample_cart_main']"),
    '确认弹窗-加入型号清单': ('xpath', "//a[@id='join_cart']"),
    '确认弹窗-立即查询': ('xpath', "//button[@id='trade_account']"),
}


class AskTimePage(BasePage):
    """交期查询服务页"""

    def check_AskTimePage(self):
        """交期查询服务页"""
        for i, key in enumerate(Locator):
            if i < 13:
                self.move_to_element(Locator[key])
        self.input_text(Locator['公司'], ' ')
        self.is_click(Locator['提交'])
        text1 = self.element_text(Locator['服务标题'])
        text2 = self.element_text(Locator['必填提示'])
        return text1, text2

    def check_ask_price_join_cart(self):
        """交期查询服务确认弹窗"""
        text1 = self.element_text(Locator['确认弹窗-服务标题'])
        self.move_to_element(Locator['确认弹窗-ON名称'])
        self.move_to_element(Locator['确认弹窗-ON厂牌'])
        self.input_text(Locator['确认弹窗-申请数量'], 1)
        self.move_to_element(Locator['确认弹窗-打开型号清单'])
        self.move_to_element(Locator['确认弹窗-加入型号清单'])
        self.is_click(Locator['确认弹窗-立即查询'])
        return text1
