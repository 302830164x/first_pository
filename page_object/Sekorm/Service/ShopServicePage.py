from page.basepage import BasePage

Locator = {
    '确认弹窗-服务标题': ('xpath', "//div[@class='modal-header']/h3"),
    '确认弹窗-ON名称': ('xpath', "//div[@class='join-cart']//h3[@class='on']"),
    '确认弹窗-ON厂牌': ('xpath', "//div[@class='join-cart']//p[@class='brand']"),
    '确认弹窗-购买数量': ('xpath', "//input[@id='trade_number']"),
    '确认弹窗-单价': ('xpath', "//p[@id='allow_price']"),
    '确认弹窗-仓库、现货和交期': ('xpath', "//p[@id='pay_local']"),
    '确认弹窗-订单小计': ('xpath', "//p[@class='price text-ellipsis']//i[@id='price']"),
    '确认弹窗-打开型号清单': ('xpath', "//a[@id='seePurchase']"),
    '确认弹窗-加入型号清单': ('xpath', "//a[@id='join_cart']"),
    '确认弹窗-立即结算': ('xpath', "//button[@id='trade_account']"),
    # 订单填写及核对页面
    '订单填写及核对': ('xpath', "//ul[@class='trade-top clearfix']/li"),
    '收货地址': ('xpath', "//div[@id='has_address']"),
    '新增收货地址': ('xpath', "//span[@class='addNewAddress ']"),
    '发票信息': ('xpath', "//div[@id='invoice']"),
    '发票类型': ('xpath', "//li[@class='ordinary-invoice invoice-active']"),
    '发票抬头': ('xpath', "//div[@class='invoice-info-radio clearfix']"),
    '商品清单': ('xpath', "//div[@class='order-list order-list-spec cart-supply']"),
    'ON名称': ('xpath', "//a[@class='model-on']"),
    '配送方式': ('xpath', "//div[@class='logistics-method']"),
    '运费': ('xpath', "(//div[@class='order-total-money']//span)[1]"),
    '订单小计': ('xpath', "(//div[@class='order-total-money']//span)[2]"),
    '应付总额': ('xpath', "//i[@id='totalAmountShow']"),
    '提交订单': ('xpath', "//span[@id='submitOrder']"),
    '买卖合同': ('xpath', "//a[@id='salesMap']"),
    '取消按钮': ('xpath', "//button[contains(text(),'取消')]"),
    '平台LOGO': ('xpath', "//img[@alt='世强硬创平台']"),
}


class ShopServicePage(BasePage):
    """小量快购服务页"""

    def check_join_cart(self):
        """小量快购服务弹窗"""
        text = self.element_text(Locator['确认弹窗-服务标题'])
        self.move_to_element(Locator['确认弹窗-ON名称'])
        self.move_to_element(Locator['确认弹窗-ON厂牌'])
        self.move_to_element(Locator['确认弹窗-购买数量'])
        self.move_to_element(Locator['确认弹窗-单价'])
        self.move_to_element(Locator['确认弹窗-仓库、现货和交期'])
        self.move_to_element(Locator['确认弹窗-订单小计'])
        self.move_to_element(Locator['确认弹窗-打开型号清单'])
        self.move_to_element(Locator['确认弹窗-加入型号清单'])
        self.is_click(Locator['确认弹窗-立即结算'])
        return text

    def check_submit_order(self):
        """订单核对页"""
        text = self.element_text(Locator['订单填写及核对'])
        self.move_to_element(Locator['收货地址'])
        self.move_to_element(Locator['新增收货地址'])
        self.move_to_element(Locator['发票信息'])
        self.move_to_element(Locator['发票类型'])
        self.move_to_element(Locator['发票抬头'])
        self.move_to_element(Locator['商品清单'])
        self.move_to_element(Locator['ON名称'])
        self.move_to_element(Locator['配送方式'])
        self.move_to_element(Locator['运费'])
        self.move_to_element(Locator['订单小计'])
        self.move_to_element(Locator['应付总额'])
        self.move_to_element(Locator['买卖合同'])
        self.is_click(Locator['提交订单'])
        self.is_click(Locator['取消按钮'])
        self.is_click(Locator['平台LOGO'])
        return text
