from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Shops.SalesManagementPage import SalesManagementPage
from page_object.B.Shops.ShopPage import ShopPage

sekorm = Element('B_Element')


class ShopsPage(BasePage):
    """店铺"""

    def go_ShopPage(self):
        """店铺-店铺管理"""
        self.is_click(sekorm['店铺-店铺管理'])
        return ShopPage(self.driver)

    def go_SalesManagementPage(self):
        """店铺-售卖管理"""
        self.is_click(sekorm['店铺-售卖管理'])
        return SalesManagementPage(self.driver)