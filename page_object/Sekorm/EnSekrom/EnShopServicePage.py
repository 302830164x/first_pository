from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnOnPage import EnOnPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage

Locator = {
    '确认弹窗-服务标题': ('xpath', "//div[@class='modal-header']/h3"),
    '确认弹窗-ON名称': ('xpath', "//div[@class='join-cart']//h3[@class='on']"),
    '确认弹窗-ON厂牌': ('xpath', "//div[@class='join-cart']//p[@class='brand']"),
    '确认弹窗-购买数量': ('xpath', "//input[@id='trade_number']"),
    '确认弹窗-单价': ('xpath', "//span[@id='allow_price']"),
    '确认弹窗-现货': ('xpath', "//span[@id='allow_stock']"),
    '确认弹窗-仓库': ('xpath', "//span[@id='allow_shipFrom']"),
    '确认弹窗-预计交期': ('xpath', "//span[@class='information-content delivery-content-edd pull-right']"),
    '确认弹窗-订单小计': ('xpath', "//i[@id='price']"),
    '确认弹窗-加入购物车': ('xpath', "//a[@id='join_cart']"),
    '确认弹窗-成功加入提示': ('xpath', "//span[@class='order-msg-succ-title']"),
    '确认弹窗-关闭按钮': ('xpath', "//a[@id='continue_shop']"),
    '确认弹窗-打开购物车': ('xpath', "//a[@id='view_cart']"),

    '订单审核-页面标题': ('xpath', "//li[normalize-space()='Order Filling and Checking']"),
    '订单审核-地址': ('xpath', "//div[@class='user-info clearfix']"),
    '订单审核-新增地址': ('xpath', "//span[@class='addNewAddress ']"),
    '订单审核-编辑地址': ('xpath', "//span[@class='edit-addr']"),
    '订单审核-地址必填提示': ('xpath', "//p[@class='vformMsnInd']"),
    '订单审核-保存地址': ('xpath', "//input[@value='Confirm']"),
    '订单审核-企业信息': ('xpath', "//div[@class='order-submit-enterprise-container']"),
    '订单审核-配送方式': ('xpath', "//div[@class='order-submit-delivery-container']"),
    '订单审核-商品信息': ('xpath', "//div[@class='order-list cart-supply']"),
    '订单审核-店铺名称': ('xpath', "//span[@class='shop-name']"),
    '订单审核-型号': ('xpath', "//a[@class='model-on']"),
    '订单审核-厂牌': ('xpath', "//a[@class='model-brand']"),
    '订单审核-描述': ('xpath', "//div[@class='supply-desc text-left']"),
    '订单审核-仓库': ('xpath', "//span[@class='pay-local-content']"),
    '订单审核-单价': ('xpath', "//div[@class='price-content']"),
    '订单审核-数量': ('xpath', "//div[@class='amount-content']"),

    '订单审核-订单合计': ('xpath', "//i[@id='totalAmountShow']"),
    '订单审核-提交订单': ('xpath', "//span[@id='submitOrder']"),
    '订单审核-必填提示': ('xpath', "//p[@class='vformMsnReg']"),
    '订单审核-买卖合同': ('xpath', "//a[@id='salesMap']"),
    '订单审核-勾选合同': ('xpath', "//i[@class='icon-checkbox']"),

}


class EnShopServicePage(BasePage):
    """英文站小量快购服务页"""

    def check_join_cart(self):
        """英文站小量快购服务弹窗"""
        from page_object.Sekorm.EnSekrom.EnUserListPage import EnUserListPage
        self.move_to_element(Locator['确认弹窗-服务标题'])
        self.move_to_element(Locator['确认弹窗-ON名称'])
        self.move_to_element(Locator['确认弹窗-ON厂牌'])
        self.move_to_element(Locator['确认弹窗-购买数量'])
        self.move_to_element(Locator['确认弹窗-单价'])
        self.move_to_element(Locator['确认弹窗-现货'])
        self.move_to_element(Locator['确认弹窗-仓库'])
        self.move_to_element(Locator['确认弹窗-预计交期'])
        self.move_to_element(Locator['确认弹窗-订单小计'])
        self.is_click(Locator['确认弹窗-加入购物车'])
        text = self.element_text(Locator['确认弹窗-成功加入提示'])
        self.is_click(Locator['确认弹窗-打开购物车'])
        return text, EnUserListPage(self.driver)

    def check_order_filling(self):
        """英文站小量快购订单审核"""
        self.move_to_element(Locator['订单审核-地址'])
        self.move_to_element(Locator['订单审核-企业信息'])
        self.move_to_element(Locator['订单审核-配送方式'])
        self.move_to_element(Locator['订单审核-商品信息'])
        self.move_to_element(Locator['订单审核-订单合计'])
        return self.element_text(Locator['订单审核-页面标题'])

    def check_en_order_address(self):
        """英文站订单审核 地址编辑检查"""
        self.is_click(Locator['订单审核-编辑地址'])
        self.is_click(Locator['订单审核-保存地址'])
        self.is_click(Locator['订单审核-新增地址'])
        self.is_click(Locator['订单审核-保存地址'])
        return self.element_text(Locator['订单审核-地址必填提示'])

    def check_en_sales_agreement(self):
        """英文站检查买卖合同"""
        self.is_click(Locator['订单审核-买卖合同'])
        self.switch_window()
        return self

    def check_en_order_on_info(self):
        """英文站检查订单审核页ON信息"""
        self.move_to_element(Locator['订单审核-型号'])
        self.move_to_element(Locator['订单审核-厂牌'])
        self.move_to_element(Locator['订单审核-描述'])
        self.move_to_element(Locator['订单审核-仓库'])
        self.move_to_element(Locator['订单审核-单价'])
        self.move_to_element(Locator['订单审核-数量'])
        return self.element_text(Locator['订单审核-店铺名称'])

    def click_en_order_on(self):
        """点击英文站订单审核页ON型号"""
        self.is_click(Locator['订单审核-型号'])
        self.switch_window()
        return EnOnPage(self.driver)

    def click_en_order_brand(self):
        """点击英文站订单审核页ON型号"""
        self.is_click(Locator['订单审核-厂牌'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_en_order_submit(self):
        """点击英文站订单审核页提交按钮"""
        self.is_click(Locator['订单审核-勾选合同'])
        self.is_click(Locator['订单审核-提交订单'])
        return self.element_text(Locator['订单审核-必填提示'])
