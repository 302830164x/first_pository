from page.basepage import BasePage
from page_object.Sekorm.User.OrderDetailPage import OrderDetailPage
from utils.times import sleep

Locator = {
    '订单搜索框': ('xpath', "//input[@class='member-search sk-fs14']"),
    '订单搜索按钮': ('xpath', "//button[contains(text(),'搜索')]"),
    '订单列表': ('xpath', "//div[@class='member-order-item']"),
    '订单时间': ('xpath', "//div[@class='member-order-item']/div/div/span[1]"),
    '订单类型': ('xpath', "//div[@class='member-order-item']/div/div/a"),
    '订单号': ('xpath', "//div[@class='member-order-item']/div/div/span[2]"),
    '厂牌': ('xpath', "//td[@class='brandName-img']"),
    '型号': ('xpath', "//td[@class='brandName-img']/following-sibling::td[1]"),
    '单价': ('xpath', "//span[@class='bold']"),
    '查看详情': ('xpath', "//a[contains(text(),'查看详情')]"),
    '查看更多': ('xpath', "//div[@class='expandMore']"),
}


class UserOrderPage(BasePage):
    """我的订单页"""

    def find_order_by_search(self, text):
        """通过搜索查询订单"""
        self.input_text(Locator['订单搜索框'], text)
        self.is_click(Locator['订单搜索按钮'])
        return self.element_text(Locator['型号'])

    def go_OrderDetailPage_by_check(self):
        """通过点击查看详情进入订单详情页"""
        self.input_text(Locator['订单搜索框'], '小量快购')
        self.is_click(Locator['订单搜索按钮'])
        self.is_click(Locator['查看详情'])
        self.switch_window()
        return OrderDetailPage(self.driver)

    def check_order_num(self):
        """检查订单数量"""
        num1 = self.elements_num(Locator['订单列表'])
        self.is_click(Locator['查看更多'])
        sleep()
        num2 = self.elements_num(Locator['订单列表'])
        return num1, num2
