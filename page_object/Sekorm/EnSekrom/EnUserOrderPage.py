from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnSupplyPage import EnSupplyPage

Locator = {
    '订单池为空-图标': ('xpath', "//img[@class='mr20']"),
    '订单池为空-提示语': ('xpath', "//p[@class='tip']"),
    '订单池为空-跳转按钮': ('xpath', "//a[normalize-space()='Go shopping']"),
    '订单号': ('xpath', "//a[@class='orderDetail line-type']"),
}


class EnUserOrderPage(BasePage):
    """英文站我的订单"""

    def check_empty_order_list(self):
        """检查英文站-我的订单为空"""
        self.move_to_element(Locator['订单池为空-图标'])
        text = self.element_text(Locator['订单池为空-提示语'])
        self.is_click(Locator['订单池为空-跳转按钮'])
        return text, EnSupplyPage(self.driver)

    def check_en_order_list(self):
        """检查英文站-我的订单"""
        num = self.elements_num(Locator['订单号'])
        self.is_click(Locator['订单号'])
        self.switch_window()
        return num

