from common.readelement import Element
from page.basepage import BasePage
from page_object.B.ContentManage.AgencyAgreementPage import AgencyAgreementPage
from page_object.B.ContentManage.EcnewPage import EcnewPage
from page_object.B.ContentManage.FinishManagementPage import FinishManagementPage
from page_object.B.ContentManage.MaterialManagementPage import MaterialManagementPage
from page_object.B.ContentManage.ReferencePage import ReferencePage
from page_object.B.ContentManage.SelectionPage import SelectionPage
from page_object.B.ContentManage.SpEcdocPage import SpEcdocPage
from page_object.B.ContentManage.SubmitEcdocPage import SubmitEcdocPage

sekorm = Element('B_Element')


class ContentManagePage(BasePage):
    """内容管理"""

    def go_EcnewPage(self):
        """内容管理－文章管理"""
        self.is_click(sekorm['内容管理－文章管理'])
        return EcnewPage(self.driver)

    def go_SubmitEcdocPage(self):
        """内容管理－资料管理"""
        self.is_click(sekorm['内容管理－资料管理'])
        return SubmitEcdocPage(self.driver)

    def go_SpEcdocPage(self):
        """内容管理－公告管理"""
        self.is_click(sekorm['内容管理－公告管理'])
        return SpEcdocPage(self.driver)

    def go_AgencyAgreementPage(self):
        """内容管理－代理协议管理"""
        self.is_click(sekorm['内容管理－代理协议管理'])
        return AgencyAgreementPage(self.driver)

    def go_MaterialManagementPage(self):
        """内容管理－视频素材管理"""
        self.is_click(sekorm['内容管理－视频素材管理'])
        return MaterialManagementPage(self.driver)

    def go_FinishManagementPage(self):
        """内容管理－视频成品管理"""
        self.is_click(sekorm['内容管理－视频成品管理'])
        return FinishManagementPage(self.driver)

    def go_SelectionPage(self):
        """内容管理－选型器"""
        self.is_click(sekorm['内容管理－选型器'])
        return SelectionPage(self.driver)

    def go_ReferencePage(self):
        """内容管理－对照表"""
        self.is_click(sekorm['内容管理－对照表'])
        return ReferencePage(self.driver)
