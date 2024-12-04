from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.BaseData.BaseDataPage import BaseDataPage
from page_object.ECM.Content.ContentPage import ContentPage
from page_object.ECM.Delivery.DeliveryPage import DeliveryPage
from page_object.ECM.Member.MemberPage import MemberPage
from page_object.ECM.Operation.OperationPage import OperationPage
from page_object.ECM.Provider.ProviderPage import ProviderPage
from page_object.ECM.QA.QaPage import QaPage
from page_object.ECM.Statistics.StatisticsPage import StatisticsPage
from page_object.ECM.System.SystemPage import SystemPage

sekorm = Element('EcmElement')


class EcmIndexPage(BasePage):
    """登录页类"""

    def get_ecm_index_text(self):
        """获取登录后头部文本"""
        return self.element_text(sekorm['登录成功'])

    def quit_ecm_login(self):
        self.is_click(sekorm['退出登录'])
        self.is_click(sekorm['确认退出'])
        return self

    def go_ecm_login(self):
        from page_object.ECM.EcmLoginPage import EcmLoginPage
        return EcmLoginPage(self.driver)

    def click_content(self):
        """点击内容管理"""
        self.is_click(sekorm['内容管理'])
        return ContentPage(self.driver)

    def click_member(self):
        """点击会员管理"""
        self.is_click(sekorm['会员管理'])
        return MemberPage(self.driver)

    def click_operation(self):
        """点击运营管理"""
        self.is_click(sekorm['运营管理'])
        return OperationPage(self.driver)

    def click_delivery(self):
        """点击交付管理"""
        self.is_click(sekorm['交付管理'])
        return DeliveryPage(self.driver)

    def click_statistics(self):
        """点击数据统计"""
        self.is_click(sekorm['数据统计'])
        return StatisticsPage(self.driver)

    def click_qa(self):
        """点击Q&A管理"""
        self.is_click(sekorm['Q&A管理'])
        return QaPage(self.driver)

    def click_base(self):
        """点击基础资料"""
        self.is_click(sekorm['基础资料'])
        return BaseDataPage(self.driver)

    def click_provider(self):
        """点击服务商"""
        self.is_click(sekorm['服务商'])
        return ProviderPage(self.driver)

    def click_system(self):
        """点击系统管理"""
        self.is_click(sekorm['系统管理'])
        return SystemPage(self.driver)
