
from common.readelement import Element
from page.basepage import BasePage
from page_object.B.OrderManage.AccountReceivablePage import AccountReceivablePage
from page_object.B.OrderManage.InvoicePoolPage import InvoicePoolPage
from page_object.B.OrderManage.LogisticsInfoPage import LogisticsInfoPage
from page_object.B.OrderManage.MyOrderPage import MyOrderPage
from page_object.B.OrderManage.MyOrderWorkbenchPage import MyOrderWorkbenchPage
from page_object.B.OrderManage.OrderPerformPage import OrderPerformPage
from page_object.B.OrderManage.OrderWorkbenchProblemPage import OrderWorkbenchProblemPage
from page_object.B.OrderManage.OrderWorkbenchSoToDoPage import OrderWorkbenchSoToDoPage
from page_object.B.OrderManage.ProblemSupplyPage import ProblemSupplyPage
from page_object.B.OrderManage.TransactionRecordPage import TransactionRecordPage
from page_object.B.OrderManage.UnusualOrderPage import UnusualOrderPage

sekorm = Element('B_Element')


class OrderManagePage(BasePage):
    """订单与应收管理"""

    def go_MyOrderWorkbenchPage(self):
        """订单与应收管理－我的订单"""
        self.is_click(sekorm['订单与应收管理－我的订单'])
        return MyOrderWorkbenchPage(self.driver)

    def go_UnusualOrderPage(self):
        """订单与应收管理－潜在异常"""
        self.is_click(sekorm['订单与应收管理－潜在异常'])
        return UnusualOrderPage(self.driver)

    def go_ProblemSupplyPage(self):
        """订单与应收管理－问题供应"""
        self.is_click(sekorm['订单与应收管理－问题供应'])
        return ProblemSupplyPage(self.driver)

    def go_OrderWorkbenchProblemPage(self):
        """订单与应收管理－问题订单"""
        self.is_click(sekorm['订单与应收管理－问题订单'])
        return OrderWorkbenchProblemPage(self.driver)

    def go_MyOrderPage(self):
        """订单与应收管理－我的小量快购订单"""
        self.is_click(sekorm['订单与应收管理－我的小量快购订单'])
        return MyOrderPage(self.driver)

    def go_OrderPerformPage(self):
        """订单与应收管理－小量快购订单池"""
        self.is_click(sekorm['订单与应收管理－小量快购订单池'])
        return OrderPerformPage(self.driver)

    def go_OrderWorkbenchSoToDoPage(self):
        """订单与应收管理－SO待办池"""
        self.is_click(sekorm['订单与应收管理－SO待办池'])
        return OrderWorkbenchSoToDoPage(self.driver)

    def go_LogisticsInfoPage(self):
        """订单与应收管理－物流信息查询"""
        self.is_click(sekorm['订单与应收管理－物流信息查询'])
        return LogisticsInfoPage(self.driver)

    def go_TransactionRecordPage(self):
        """订单与应收管理－资金流水"""
        self.is_click(sekorm['订单与应收管理－资金流水'])
        return TransactionRecordPage(self.driver)

    def go_AccountReceivablePage(self):
        """订单与应收管理－应收账款工作台"""
        self.is_click(sekorm['订单与应收管理－应收账款工作台'])
        return AccountReceivablePage(self.driver)

    def go_InvoicePoolPage(self):
        """订单与应收管理－发票池"""
        self.is_click(sekorm['订单与应收管理－发票池'])
        return InvoicePoolPage(self.driver)


