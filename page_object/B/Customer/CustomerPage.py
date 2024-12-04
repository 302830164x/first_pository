from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Customer.CreditPay.CreditPaymentPage import CreditPaymentPage
from page_object.B.Customer.CreditPay.PaymentOrderReviewPage import PaymentOrderReviewPage
from page_object.B.Customer.CreditPay.WriteOffListPage import WriteOffListPage
from page_object.B.Customer.CustomerBenchPage import CustomerBenchPage
from page_object.B.Customer.CustomerPoolPage import CustomerPoolPage
from page_object.B.Customer.EpTagEditPage import EpTagEditPage
from page_object.B.Customer.PCNEOL.NoPcneolEmailNotifyPage import NoPcneolEmailNotifyPage
from page_object.B.Customer.PCNEOL.PcneolEmailNotifyPage import PcneolEmailNotifyPage
from page_object.B.Customer.PCNEOL.PnConfirmPoolPage import PnConfirmPoolPage
from page_object.B.Customer.PrivateCustomerBenchPage import PrivateCustomerBenchPage
from page_object.B.Customer.Restrict.RestrictSearchPage import RestrictSearchPage
from page_object.B.Customer.RiskEpPage import RiskEpPage
from page_object.B.Customer.SeminarInfoPage import SeminarInfoPage

sekorm = Element('B_Element')


class CustomerPage(BasePage):
    """客户工作台"""

    def go_CustomerBenchPage(self):
        """客户工作台-全部客户"""
        self.is_click(sekorm['客户工作台-全部客户'])
        return CustomerBenchPage(self.driver)

    def go_PrivateCustomerBenchPage(self):
        """客户工作台-我的客户"""
        self.is_click(sekorm['客户工作台-我的客户'])
        return PrivateCustomerBenchPage(self.driver)

    def go_CustomerPoolPage(self):
        """客户工作台-新客户"""
        self.is_click(sekorm['客户工作台-新客户'])
        return CustomerPoolPage(self.driver)

    def go_RestrictSearchPage(self):
        """客户工作台-管制客户-管制查询"""
        self.is_click(sekorm['客户工作台-管制客户'])
        self.is_click(sekorm['客户工作台-管制客户-管制查询'])
        return RestrictSearchPage(self.driver)

    def go_CreditPaymentPage(self):
        """客户工作台-客户信用-授信客户"""
        self.is_click(sekorm['客户工作台-客户信用'])
        self.is_click(sekorm['客户工作台-客户信用-授信客户'])
        return CreditPaymentPage(self.driver)

    def go_PaymentOrderReviewPage(self):
        """客户工作台-客户信用-账期订单审核"""
        self.is_click(sekorm['客户工作台-客户信用'])
        self.is_click(sekorm['客户工作台-客户信用-账期订单审核'])
        return PaymentOrderReviewPage(self.driver)

    def go_WriteOffListPage(self):
        """客户工作台-客户信用-核销清单"""
        self.is_click(sekorm['客户工作台-客户信用'])
        self.is_click(sekorm['客户工作台-客户信用-核销清单'])
        return WriteOffListPage(self.driver)

    def go_RiskEpPage(self):
        """客户工作台-采集信息客户池"""
        self.is_click(sekorm['客户工作台-采集信息客户池'])
        return RiskEpPage(self.driver)

    def go_PcneolEmailNotifyPage(self):
        """客户工作台-PCN、EOL通知-客户通知池"""
        self.is_click(sekorm['客户工作台-PCN、EOL通知'])
        self.is_click(sekorm['客户工作台-PCN、EOL通知-客户通知池'])
        return PcneolEmailNotifyPage(self.driver)

    def go_NoPcneolEmailNotifyPage(self):
        """客户工作台-PCN、EOL通知-未分发客户"""
        self.is_click(sekorm['客户工作台-PCN、EOL通知'])
        self.is_click(sekorm['客户工作台-PCN、EOL通知-未分发客户'])
        return NoPcneolEmailNotifyPage(self.driver)

    def go_PnConfirmPoolPage(self):
        """客户工作台-PCN、EOL通知-型号确认池"""
        self.is_click(sekorm['客户工作台-PCN、EOL通知'])
        self.is_click(sekorm['客户工作台-PCN、EOL通知-型号确认池'])
        return PnConfirmPoolPage(self.driver)

    def go_SeminarInfoPage(self):
        """客户工作台-活动营销"""
        self.is_click(sekorm['客户工作台-活动营销'])
        return SeminarInfoPage(self.driver)

    def go_EpTagEditPage(self):
        """客户工作台-添加移除标签"""
        self.is_click(sekorm['客户工作台-添加移除标签'])
        return EpTagEditPage(self.driver)
