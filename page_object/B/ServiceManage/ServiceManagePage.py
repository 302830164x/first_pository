from common.readelement import Element
from page.basepage import BasePage
from page_object.B.ServiceManage.AskPriceUnmetPage import AskPriceUnmetPage
from page_object.B.ServiceManage.BusinessDemandPage import BusinessDemandPage
from page_object.B.ServiceManage.CallCenter import CallCenter
from page_object.B.ServiceManage.CallCenterAgentManage import CallCenterAgentManage
from page_object.B.ServiceManage.EcoPartnersPage import EcoPartnersPage
from page_object.B.ServiceManage.EnServicePage import EnServicePage
from page_object.B.ServiceManage.LabOrderPage import LabOrderPage
from page_object.B.ServiceManage.MaterialCustomPage import MaterialCustomPage
from page_object.B.ServiceManage.MidCarEDIList import MidCarEDIList
from page_object.B.ServiceManage.PrizeServicePoolPage import PrizeServicePoolPage
from page_object.B.ServiceManage.RecruitServicePage import RecruitServicePage
from page_object.B.ServiceManage.ResourceWorkbench import ResourceWorkbench
from page_object.B.ServiceManage.SampleHandlePage import SampleHandlePage
from page_object.B.ServiceManage.SampleUnmetPage import SampleUnmetPage
from page_object.B.ServiceManage.SelectionUnmetPage import SelectionUnmetPage
from page_object.B.ServiceManage.ServiceDeploymentPage import ServiceDeploymentPage
from page_object.B.ServiceManage.ServiceLog.SrImptPage import SrImptPage
from page_object.B.ServiceManage.ServiceLog.SrSelPage import SrSelPage
from page_object.B.ServiceManage.ServiceLog.SrTypePage import SrTypePage
from page_object.B.ServiceManage.ServicePage import ServicePage
from page_object.B.ServiceManage.ServiceProcessPage import ServiceProcessPage
from page_object.B.ServiceManage.ServiceProcessParentChildPage import ServiceProcessParentChildPage
from page_object.B.ServiceManage.ServicePromotePage import ServicePromotePage
from page_object.B.ServiceManage.ServiceWorkPage import ServiceWorkPage

sekorm = Element('B_Element')


class ServiceManagePage(BasePage):
    """服务管理"""

    def go_ServiceWorkPage(self):
        """服务管理－服务工作台"""
        self.is_click(sekorm['服务管理－服务工作台'])
        return ServiceWorkPage(self.driver)

    def go_ServiceProcessPage(self):
        """服务管理－研发需求池"""
        self.is_click(sekorm['服务管理－研发需求池'])
        return ServiceProcessPage(self.driver)

    def go_BusinessDemandPage(self):
        """服务管理－商务需求池"""
        self.is_click(sekorm['服务管理－商务需求池'])
        return BusinessDemandPage(self.driver)

    def go_ServicePage(self):
        """服务管理－服务新增"""
        self.is_click(sekorm['服务管理－服务新增'])
        return ServicePage(self.driver)

    def go_ServicePromotePage(self):
        """服务管理－服务部署"""
        self.is_click(sekorm['服务管理－服务部署'])
        return ServicePromotePage(self.driver)

    def go_ServiceDeploymentPage(self):
        """服务管理－服务部署"""
        self.is_click(sekorm['服务管理－服务部署'])
        return ServiceDeploymentPage(self.driver)

    def go_EnServicePage(self):
        """服务管理－亚洲服务新增"""
        self.is_click(sekorm['服务管理－亚洲服务新增'])
        return EnServicePage(self.driver)

    def go_LabOrderPage(self):
        """服务管理－实验室预约处理"""
        self.is_click(sekorm['服务管理－实验室预约处理'])
        return LabOrderPage(self.driver)

    def go_MaterialCustomPage(self):
        """服务管理－材料定制"""
        self.is_click(sekorm['服务管理－材料定制'])
        return MaterialCustomPage(self.driver)

    def go_EcoPartnersPage(self):
        """服务管理－供应商合作申请"""
        self.is_click(sekorm['服务管理－供应商合作申请'])
        return EcoPartnersPage(self.driver)

    def go_RecruitServicePage(self):
        """服务管理－招募服务处理"""
        self.is_click(sekorm['服务管理－招募服务处理'])
        return RecruitServicePage(self.driver)

    def go_SampleUnmetPage(self):
        """服务管理－服务未满足"""
        self.is_click(sekorm['服务管理－服务未满足'])
        return SampleUnmetPage(self.driver)

    def go_SampleHandlePage(self):
        """服务管理－样品申请"""
        self.is_click(sekorm['服务管理－样品申请'])
        return SampleHandlePage(self.driver)

    def go_ServiceProcessParentChildPage(self):
        """服务管理－新样品申请"""
        self.is_click(sekorm['服务管理－新样品申请'])
        return ServiceProcessParentChildPage(self.driver)

    def go_AskPriceUnmetPage(self):
        """服务管理－询价&询交期未满足"""
        self.is_click(sekorm['服务管理－询价&询交期未满足'])
        return AskPriceUnmetPage(self.driver)

    def go_SelectionUnmetPage(self):
        """服务管理－选型帮助未满足"""
        self.is_click(sekorm['服务管理－选型帮助未满足'])
        return SelectionUnmetPage(self.driver)

    def go_PrizeServicePoolPage(self):
        """服务管理－奖品服务"""
        self.is_click(sekorm['服务管理－奖品服务'])
        return PrizeServicePoolPage(self.driver)

    def go_CallCenter(self):
        """服务管理－呼叫系统"""
        self.is_click(sekorm['服务管理－呼叫系统'])
        return CallCenter(self.driver)

    def go_CallCenterAgentManage(self):
        """服务管理－客服座席管理"""
        self.is_click(sekorm['服务管理－客服坐席管理'])
        return CallCenterAgentManage(self.driver)

    def go_ResourceWorkbench(self):
        """服务管理－资源工作台"""
        self.is_click(sekorm['服务管理－资源工作台'])
        return ResourceWorkbench(self.driver)

    def go_MidCarEDIList(self):
        """服务管理－中车EDI"""
        self.is_click(sekorm['服务管理－中车EDI'])
        return MidCarEDIList(self.driver)

    def go_SrSelPage(self):
        """服务管理－服务记录－记录查询"""
        self.is_click(sekorm['服务管理－服务记录'])
        self.is_click(sekorm['服务管理－服务记录－记录查询'])
        self.switch_window()
        return SrSelPage(self.driver)

    def go_SrImptPage(self):
        """服务管理－服务记录－记录查询"""
        self.is_click(sekorm['服务管理－服务记录'])
        self.is_click(sekorm['服务管理－服务记录－记录导入'])
        return SrImptPage(self.driver)

    def go_SrTypePage(self):
        """服务管理－服务记录－记录查询"""
        self.is_click(sekorm['服务管理－服务记录'])
        self.is_click(sekorm['服务管理－服务记录－服务类型管理'])
        return SrTypePage(self.driver)
