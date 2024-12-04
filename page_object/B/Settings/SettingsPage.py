from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Settings.EpTeamStructurePage import EpTeamStructurePage
from page_object.B.Settings.BrandTagsManagePage import BrandTagsManagePage
from page_object.B.Settings.EnterpriseTagsManagePage import EnterpriseTagsManagePage
from page_object.B.Settings.ExternalSystemAuthorizationPage import ExternalSystemAuthorizationPage
from page_object.B.Settings.ExternalSystemManagePage import ExternalSystemManagePage
from page_object.B.Settings.ExternalSystemPage import ExternalSystemPage
from page_object.B.Settings.SupplierTagsManagePage import SupplierTagsManagePage
from page_object.B.Settings.WorkflowManageListPage import WorkflowManageListPage

sekorm = Element('B_Element')


class SettingsPage(BasePage):
    """设置"""

    def go_EnterpriseTagsManagePage(self):
        """设置－客户标签管理"""
        self.is_click(sekorm['设置－客户标签管理'])
        return EnterpriseTagsManagePage(self.driver)

    def go_SupplierTagsManagePage(self):
        """设置－供应商标签管理"""
        self.is_click(sekorm['设置－供应商标签管理'])
        return SupplierTagsManagePage(self.driver)

    def go_BrandTagsManagePage(self):
        """设置－品牌标签管理"""
        self.is_click(sekorm['设置－品牌标签管理'])
        return BrandTagsManagePage(self.driver)

    def go_ExternalSystemPage(self):
        """设置－第三方系统"""
        self.is_click(sekorm['设置－第三方系统'])
        return ExternalSystemPage(self.driver)

    def go_ExternalSystemManagePage(self):
        """设置－第三方系统管理"""
        self.is_click(sekorm['设置－第三方系统管理'])
        return ExternalSystemManagePage(self.driver)

    def go_ExternalSystemAuthorizationPage(self):
        """设置－第三方系统授权"""
        self.is_click(sekorm['设置－第三方系统授权'])
        return ExternalSystemAuthorizationPage(self.driver)

    def go_WorkflowManageListPage(self):
        """设置－审批流程管理"""
        self.is_click(sekorm['设置－审批流程管理'])
        return WorkflowManageListPage(self.driver)

    def go_EpTeamStructurePage(self):
        """设置－组织架构"""
        self.is_click(sekorm['设置－组织架构'])
        return EpTeamStructurePage(self.driver)
