from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Statistics.BrandConsumePage import BrandConsumePage
from page_object.B.Statistics.BrandStatPage import BrandStatPage
from page_object.B.Statistics.DigitalMarketingPage import DigitalMarketingPage
from page_object.B.Statistics.DinStatisticsPage import DinStatisticsPage
from page_object.B.Statistics.EpServiceStatPage import EpServiceStatPage
from page_object.B.Statistics.EpmPage import EpmPage
from page_object.B.Statistics.ForecastPage import ForecastPage
from page_object.B.Statistics.GoodsForecastPage import GoodsForecastPage
from page_object.B.Statistics.MemstatPage import MemstatPage
from page_object.B.Statistics.MonthShipmentDetailPage import MonthShipmentDetailPage
from page_object.B.Statistics.MonthShipmentPage import MonthShipmentPage
from page_object.B.Statistics.NewSdbPage import NewSdbPage
from page_object.B.Statistics.OnDataStatPage import OnDataStatPage
from page_object.B.Statistics.OnStatPage import OnStatPage
from page_object.B.Statistics.OnStoragePage import OnStoragePage
from page_object.B.Statistics.PotentialReqStatPage import PotentialReqStatPage
from page_object.B.Statistics.PotentialSdbPage import PotentialSdbPage
from page_object.B.Statistics.ProviderStatisticsPage import ProviderStatisticsPage
from page_object.B.Statistics.SampleUnMetViewPage import SampleUnMetViewPage
from page_object.B.Statistics.SdbPage import SdbPage
from page_object.B.Statistics.SdbReleaseManagementPage import SdbReleaseManagementPage
from page_object.B.Statistics.SearchBehaviorLogPage import SearchBehaviorLogPage
from page_object.B.Statistics.SearchTermStatisticsPage import SearchTermStatisticsPage
from page_object.B.Statistics.ServiceContentStatPage import ServiceContentStatPage
from page_object.B.Statistics.ServiceResourceStatPage import ServiceResourceStatPage
from page_object.B.Statistics.ServiceStatisticsPage import ServiceStatisticsPage
from page_object.B.Statistics.ShipmentStatPage import ShipmentStatPage
from page_object.B.Statistics.ShippingDetailsPage import ShippingDetailsPage
from page_object.B.Statistics.SrSearchListV2Page import SrSearchListV2Page
from page_object.B.Statistics.SrSearchSpListPage import SrSearchSpListPage
from page_object.B.Statistics.StatisticalToolsPage import StatisticalToolsPage
from page_object.B.Statistics.SupplierScorePage import SupplierScorePage
from page_object.B.Statistics.WebpuvCustomPage import WebpuvCustomPage
from page_object.B.Statistics.WebpuvPage import WebpuvPage

sekorm = Element('B_Element')


class StatisticsPage(BasePage):
    """统计报表"""

    def go_DigitalMarketingPage(self):
        """统计报表－数字营销"""
        self.is_click(sekorm['统计报表－数字营销'])
        return DigitalMarketingPage(self.driver)

    def go_ServiceStatisticsPage(self):
        """统计报表－服务统计"""
        self.is_click(sekorm['统计报表－服务统计'])
        return ServiceStatisticsPage(self.driver)

    def go_StatisticalToolsPage(self):
        """统计报表－数据统计通用工具"""
        self.is_click(sekorm['统计报表－数据统计通用工具'])
        return StatisticalToolsPage(self.driver)

    def go_WebpuvPage(self):
        """统计报表－页面统计"""
        self.is_click(sekorm['统计报表－页面统计'])
        return WebpuvPage(self.driver)

    def go_MemstatPage(self):
        """统计报表－会员统计"""
        self.is_click(sekorm['统计报表－会员统计'])
        return MemstatPage(self.driver)

    def go_WebpuvCustomPage(self):
        """统计报表－定制统计"""
        self.is_click(sekorm['统计报表－定制统计'])
        return WebpuvCustomPage(self.driver)

    def go_BrandStatPage(self):
        """统计报表－品牌资源统计"""
        self.is_click(sekorm['统计报表－品牌资源统计'])
        return BrandStatPage(self.driver)

    def go_OnStoragePage(self):
        """统计报表－ON运营台"""
        self.is_click(sekorm['统计报表－ON运营台'])
        return OnStoragePage(self.driver)

    def go_OnStatPage(self):
        """统计报表－ON资源统计"""
        self.is_click(sekorm['统计报表－ON资源统计'])
        return OnStatPage(self.driver)

    def go_ServiceContentStatPage(self):
        """统计报表－服务内容统计"""
        self.is_click(sekorm['统计报表－服务内容统计'])
        return ServiceContentStatPage(self.driver)

    def go_ServiceResourceStatPage(self):
        """统计报表－服务资源统计"""
        self.is_click(sekorm['统计报表－服务资源统计'])
        return ServiceResourceStatPage(self.driver)

    def go_BrandConsumePage(self):
        """统计报表－资源消费统计"""
        self.is_click(sekorm['统计报表－资源消费统计'])
        return BrandConsumePage(self.driver)

    def go_EpServiceStatPage(self):
        """统计报表－企业资源消费统计"""
        self.is_click(sekorm['统计报表－企业资源消费统计'])
        return EpServiceStatPage(self.driver)

    def go_EpmPage(self):
        """统计报表－企业关系维护"""
        self.is_click(sekorm['统计报表－企业关系维护'])
        return EpmPage(self.driver)

    def go_OnDataStatPage(self):
        """统计报表－ON数量统计"""
        self.is_click(sekorm['统计报表－ON数量统计'])
        return OnDataStatPage(self.driver)

    def go_ProviderStatisticsPage(self):
        """统计报表－SKU数据统计"""
        self.is_click(sekorm['统计报表－SKU数据统计'])
        return ProviderStatisticsPage(self.driver)

    def go_SampleUnMetViewPage(self):
        """统计报表－样品ON未满足视图"""
        self.is_click(sekorm['统计报表－样品ON未满足视图'])
        return SampleUnMetViewPage(self.driver)

    def go_SupplierScorePage(self):
        """统计报表－供应商评分"""
        self.is_click(sekorm['统计报表－供应商评分'])
        return SupplierScorePage(self.driver)

    def go_ShippingDetailsPage(self):
        """统计报表－物料出货明细表"""
        self.is_click(sekorm['统计报表－物料出货明细表'])
        return ShippingDetailsPage(self.driver)

    def go_MonthShipmentPage(self):
        """统计报表－出货统计表"""
        self.is_click(sekorm['统计报表－出货统计表'])
        return MonthShipmentPage(self.driver)

    def go_SearchTermStatisticsPage(self):
        """统计报表－搜索词统计"""
        self.is_click(sekorm['统计报表－搜索词统计'])
        return SearchTermStatisticsPage(self.driver)

    def go_SearchBehaviorLogPage(self):
        """统计报表－搜索行为日志"""
        self.is_click(sekorm['统计报表－搜索行为日志'])
        return SearchBehaviorLogPage(self.driver)

    def go_MonthShipmentDetailPage(self):
        """统计报表－出库详情表"""
        self.is_click(sekorm['统计报表－出库详情表'])
        return MonthShipmentDetailPage(self.driver)

    def go_PotentialReqStatPage(self):
        """统计报表－潜在需求表"""
        self.is_click(sekorm['统计报表－潜在需求表'])
        return PotentialReqStatPage(self.driver)

    def go_ForecastPage(self):
        """统计报表－样品预测"""
        self.is_click(sekorm['统计报表－样品预测'])
        return ForecastPage(self.driver)

    def go_ShipmentStatPage(self):
        """统计报表－客户出货统计"""
        self.is_click(sekorm['统计报表－客户出货统计'])
        return ShipmentStatPage(self.driver)

    def go_GoodsForecastPage(self):
        """统计报表－商品预测供需表"""
        self.is_click(sekorm['统计报表－商品预测供需表'])
        return GoodsForecastPage(self.driver)

    def go_SdbPage(self):
        """统计报表－平台SDB"""
        self.is_click(sekorm['统计报表－平台SDB'])
        return SdbPage(self.driver)

    def go_NewSdbPage(self):
        """统计报表－平台SDB"""
        self.is_click(sekorm['统计报表－新平台SDB'])
        return NewSdbPage(self.driver)

    def go_SdbReleaseManagementPage(self):
        """统计报表－平台SDB"""
        self.is_click(sekorm['统计报表－供应释放'])
        return SdbReleaseManagementPage(self.driver)

    def go_PotentialSdbPage(self):
        """统计报表－潜在需求SDB"""
        self.is_click(sekorm['统计报表－潜在需求SDB'])
        return PotentialSdbPage(self.driver)

    def go_SrSearchListV2Page(self):
        """统计报表－客户行为记录"""
        self.is_click(sekorm['统计报表－客户行为记录'])
        return SrSearchListV2Page(self.driver)

    def go_SrSearchSpListPage(self):
        """统计报表－服务商行为记录"""
        self.is_click(sekorm['统计报表－服务商行为记录'])
        return SrSearchSpListPage(self.driver)

    def go_DinStatisticsPage(self):
        """统计报表－OT统计"""
        self.is_click(sekorm['统计报表－OT统计'])
        return DinStatisticsPage(self.driver)

