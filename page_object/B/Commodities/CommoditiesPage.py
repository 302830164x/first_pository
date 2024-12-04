from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Commodities.CommodityPage import CommodityPage
from page_object.B.Commodities.DiscountPage import DiscountPage
from page_object.B.Commodities.FreightManagePage import FreightManagePage
from page_object.B.Commodities.LabelManageListPage import LabelManageListPage
from page_object.B.Commodities.StockManagementPage import StockManagementPage
from page_object.B.Commodities.StorehouseManagePage import StorehouseManagePage

sekorm = Element('B_Element')


class CommoditiesPage(BasePage):
    """商品"""

    def go_CommodityPage(self):
        """商品-商品管理"""
        self.is_click(sekorm['商品-商品管理'])
        return CommodityPage(self.driver)

    def go_StockManagementPage(self):
        """商品-库存管理"""
        self.is_click(sekorm['商品-库存管理'])
        return StockManagementPage(self.driver)

    def go_LabelManageListPage(self):
        """商品-商品标签"""
        self.is_click(sekorm['商品-商品标签'])
        return LabelManageListPage(self.driver)

    def go_DiscountPage(self):
        """商品-商品促销"""
        self.is_click(sekorm['商品-商品促销'])
        return DiscountPage(self.driver)

    def go_StorehouseManagePage(self):
        """商品-仓库管理"""
        self.is_click(sekorm['商品-仓库管理'])
        return StorehouseManagePage(self.driver)

    def go_FreightManagePage(self):
        """商品-运费管理"""
        self.is_click(sekorm['商品-运费管理'])
        return FreightManagePage(self.driver)
