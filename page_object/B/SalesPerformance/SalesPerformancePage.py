from common.readelement import Element
from page.basepage import BasePage
from page_object.B.SalesPerformance.ConFirmPerFormancePage import ConFirmPerFormancePage
from page_object.B.SalesPerformance.EnterPerFormancePage import EnterPerFormancePage
from page_object.B.SalesPerformance.MyPerformanceSharePage import MyPerformanceSharePage
from page_object.B.SalesPerformance.PerFormanceSharingPage import PerFormanceSharingPage

sekorm = Element('B_Element')


class SalesPerformancePage(BasePage):
    """销售业绩归属"""

    def go_PerFormanceSharingPage(self):
        """销售业绩归属－业绩分成设置"""
        self.is_click(sekorm['销售业绩归属－业绩分成设置'])
        return PerFormanceSharingPage(self.driver)

    def go_ConFirmPerFormancePage(self):
        """销售业绩归属－确认业绩比例"""
        self.is_click(sekorm['销售业绩归属－确认业绩比例'])
        return ConFirmPerFormancePage(self.driver)

    def go_EnterPerFormancePage(self):
        """销售业绩归属－录入业绩比例"""
        self.is_click(sekorm['销售业绩归属－录入业绩比例'])
        return EnterPerFormancePage(self.driver)

    def go_MyPerformanceSharePage(self):
        """销售业绩归属－我的业绩分成"""
        self.is_click(sekorm['销售业绩归属－我的业绩分成'])
        return MyPerformanceSharePage(self.driver)
