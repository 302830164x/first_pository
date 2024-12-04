
from common.readelement import Element
from page.basepage import BasePage
from page_object.B.DWPerformance.DWAccountingOrderPoolPage import DWAccountingOrderPoolPage
from page_object.B.DWPerformance.DWDistributionPoolPage import DWDistributionPoolPage
from page_object.B.DWPerformance.DWPerformancePage import DWPerformancePage
from page_object.B.DWPerformance.DinDistributionPoolPage import DinDistributionPoolPage

sekorm = Element('B_Element')


class DWAchievementPage(BasePage):
    """DW核算管理"""

    def go_DWPerformancePage(self):
        """DW核算管理－DW-PN设置"""
        self.is_click(sekorm['DW核算管理－DW-PN设置'])
        return DWPerformancePage(self.driver)

    def go_DWAccountingOrderPoolPage(self):
        """DW核算管理－DW核算订单池"""
        self.is_click(sekorm['DW核算管理－DW核算订单池'])
        return DWAccountingOrderPoolPage(self.driver)

    def go_DinDistributionPoolPage(self):
        """DW核算管理－DIN分配池"""
        self.is_click(sekorm['DW核算管理－DIN分配池'])
        return DinDistributionPoolPage(self.driver)

    def go_DWDistributionPoolPage(self):
        """DW核算管理－DW分配池"""
        self.is_click(sekorm['DW核算管理－DW分配池'])
        return DWDistributionPoolPage(self.driver)