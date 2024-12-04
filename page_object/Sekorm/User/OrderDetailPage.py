from page.basepage import BasePage

Locator = {
    '订单号': ('xpath', "//p[@class='orderDetail-orderCode']"),
    '订单状态': ('xpath', "//span[@class='orderDetail-state']"),
    '加入型号清单': ('xpath', "//a[@id='join_cart_top']"),
    '订单状态进度条': ('xpath', "//div[@class=' od-cont clearfix commodity-od-content']"),
    '配送信息': ('xpath', "(//div[@class='od-list-outer'])[1]"),
    '支付信息': ('xpath', "(//div[@class='od-list-outer'])[2]"),
    '发票信息': ('xpath', "(//div[@class='od-list-outer'])[3]"),
    '商品型号': ('xpath', "//a[@class='model-on']"),
    '商品厂牌': ('xpath', "//a[@class='model-brand']"),
    '订单金额': ('xpath', "//span[@class='total-amount-content']"),
}


class OrderDetailPage(BasePage):
    """订单详情页"""

    def check_order_detail_layout(self):
        """检查订单详情页布局"""
        self.move_to_element(Locator['订单号'])
        self.move_to_element(Locator['订单状态'])
        self.move_to_element(Locator['加入型号清单'])
        self.move_to_element(Locator['订单状态进度条'])
        self.move_to_element(Locator['配送信息'])
        self.move_to_element(Locator['支付信息'])
        self.move_to_element(Locator['发票信息'])
        self.move_to_element(Locator['商品厂牌'])
        self.move_to_element(Locator['订单金额'])
        return self.element_text(Locator['商品型号'])
