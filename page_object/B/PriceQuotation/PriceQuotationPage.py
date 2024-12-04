from common.readelement import Element
from page.basepage import BasePage
from page_object.B.PriceQuotation.ForeignExchangeRatePage import ForeignExchangeRatePage
from page_object.B.PriceQuotation.OfferApplyForMarketPage import OfferApplyForMarketPage
from page_object.B.PriceQuotation.OfferApplyPage import OfferApplyPage
from page_object.B.PriceQuotation.PriceWorkBenchForSalerPage import PriceWorkBenchForSalerPage
from page_object.B.PriceQuotation.PriceWorkBenchPage import PriceWorkBenchPage
from page_object.B.PriceQuotation.SbcPage import SbcPage
from page_object.B.PriceQuotation.SbcToDoPage import SbcToDoPage
from page_object.B.PriceQuotation.SrpToDoPage import SrpToDoPage

sekorm = Element('B_Element')


class PriceQuotationPage(BasePage):
    """价格与报价管理"""

    def go_ForeignExchangeRatePage(self):
        """价格与报价管理-常用外汇汇率"""
        self.is_click(sekorm['价格与报价管理-常用外汇汇率'])
        return ForeignExchangeRatePage(self.driver)

    def go_PriceWorkBenchPage(self):
        """价格与报价管理-SRP价格"""
        self.is_click(sekorm['价格与报价管理-SRP价格'])
        return PriceWorkBenchPage(self.driver)

    def go_PriceWorkBenchForSalerPage(self):
        """价格与报价管理-SRP价格(销售)"""
        self.is_click(sekorm['价格与报价管理-SRP价格(销售)'])
        return PriceWorkBenchForSalerPage(self.driver)

    def go_SbcPage(self):
        """价格与报价管理-SBC价格"""
        self.is_click(sekorm['价格与报价管理-SBC价格'])
        return SbcPage(self.driver)

    def go_SrpToDoPage(self):
        """价格与报价管理-SRP待办池"""
        self.is_click(sekorm['价格与报价管理-SRP待办池'])
        return SrpToDoPage(self.driver)

    def go_SbcToDoPage(self):
        """价格与报价管理-SBC待办池"""
        self.is_click(sekorm['价格与报价管理-SBC待办池'])
        return SbcToDoPage(self.driver)

    def go_OfferApplyPage(self):
        """价格与报价管理-销售报价管理"""
        self.is_click(sekorm['价格与报价管理-销售报价管理'])
        return OfferApplyPage(self.driver)

    def go_OfferApplyForMarketPage(self):
        """价格与报价管理-市场报价管理"""
        self.is_click(sekorm['价格与报价管理-市场报价管理'])
        return OfferApplyForMarketPage(self.driver)
