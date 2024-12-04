from common.readelement import Element
from page.basepage import BasePage
from page_object.B.AuditCenterPage import AuditCenterPage
from page_object.B.Commodities.CommoditiesPage import CommoditiesPage
from page_object.B.CommodityManage.CommodityManagePage import CommodityManagePage
from page_object.B.ContentManage.ContentManagePage import ContentManagePage
from page_object.B.Customer.CustomerPage import CustomerPage
from page_object.B.DWPerformance.DWAchievementPage import DWAchievementPage
from page_object.B.GroupEmailPage import GroupEmailPage
from page_object.B.NotifyCenterPage import NotifyCenterPage
from page_object.B.OrderManage.OrderManagePage import OrderManagePage
from page_object.B.OutPlanPage import OutPlanPage
from page_object.B.PriceQuotation.PriceQuotationPage import PriceQuotationPage
from page_object.B.ProductFunDecPage import ProductFunDecPage
from page_object.B.ProjectWorkbench.ProjectWorkbenchPage import ProjectWorkbenchPage
from page_object.B.PurchasePage import PurchasePage
from page_object.B.ReplaceRecommend.ReplaceRecommendPage import ReplaceRecommendPage
from page_object.B.SalesPerformance.SalesPerformancePage import SalesPerformancePage
from page_object.B.Selection.SelectionPage import SelectionPage
from page_object.B.SeminarDataPage import SeminarDataPage
from page_object.B.ServiceManage.ServiceManagePage import ServiceManagePage
from page_object.B.Settings.SettingsPage import SettingsPage
from page_object.B.Shops.ShopsPage import ShopsPage
from page_object.B.Statistics.StatisticsPage import StatisticsPage
from page_object.B.Supplier.SupplierPage import SupplierPage
from page_object.B.Tag.TagPage import TagPage
from page_object.B.UserCenterPage import UserCenterPage
from page_object.B.UserContactPage import UserContactPage

sekorm = Element('B_Element')
Locator = {
    '列表': ('xpath', "//li[@class='ant-list-item']"),
}


class BIndexPage(BasePage):
    """首页"""

    def get_b_index_text(self):
        """获取登录后头部文本"""
        return self.element_text(sekorm['登录成功'])

    def get_BIndexPage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])

    def quit_b_login(self):
        self.is_click(sekorm['退出登录'])
        self.is_click(sekorm['确认退出'])
        return self

    def go_b_login(self):
        from page_object.B.BLoginPage import BLoginPage
        return BLoginPage(self.driver)

    def go_BIndexPage(self):
        """首页"""
        self.is_click(sekorm['首页'])
        return BIndexPage(self.driver)

    def go_ProductFunDecPage(self):
        """功能介绍"""
        self.is_click(sekorm['功能介绍'])
        return ProductFunDecPage(self.driver)

    def go_UserCenterPage(self):
        """个人中心"""
        self.is_click(sekorm['个人中心'])
        return UserCenterPage(self.driver)

    def go_UserContactPage(self):
        """通讯录"""
        self.is_click(sekorm['通讯录'])
        return UserContactPage(self.driver)

    def go_NotifyCenterPage(self):
        """通知中心"""
        self.is_click(sekorm['通知中心'])
        return NotifyCenterPage(self.driver)

    def go_AuditCenterPage(self):
        """审批中心"""
        self.is_click(sekorm['审批中心'])
        return AuditCenterPage(self.driver)

    def go_OutPlanPage(self):
        """外出计划"""
        self.is_click(sekorm['外出计划'])
        return OutPlanPage(self.driver)

    def go_CustomerPage(self):
        """客户工作台"""
        self.is_click(sekorm['客户工作台'])
        return CustomerPage(self.driver)

    def go_SupplierPage(self):
        """供应商工作台"""
        self.is_click(sekorm['供应商工作台'])
        return SupplierPage(self.driver)

    def go_SeminarDataPage(self):
        """研讨会数据"""
        self.is_click(sekorm['研讨会数据'])
        return SeminarDataPage(self.driver)

    def go_PurchasePage(self):
        """采购订单"""
        self.is_click(sekorm['采购订单'])
        return PurchasePage(self.driver)

    def go_PriceQuotationPage(self):
        """价格与报价管理"""
        self.is_click(sekorm['价格与报价管理'])
        return PriceQuotationPage(self.driver)

    def go_ProjectWorkbenchPage(self):
        """项目工作台"""
        self.is_click(sekorm['项目工作台'])
        self.go_to_element(sekorm['项目工作台'])
        return ProjectWorkbenchPage(self.driver)

    def go_ShopsPage(self):
        """店铺"""
        self.is_click(sekorm['店铺'])
        return ShopsPage(self.driver)

    def go_CommoditiesPage(self):
        """商品"""
        self.is_click(sekorm['商品'])
        self.go_to_element(sekorm['商品'])
        return CommoditiesPage(self.driver)

    def go_ServiceManagePage(self):
        """服务管理"""
        self.is_click(sekorm['服务管理'])
        self.go_to_element(sekorm['服务管理'])
        return ServiceManagePage(self.driver)

    def go_SelectionPage(self):
        """选型帮助"""
        self.is_click(sekorm['选型帮助'])
        self.go_to_element(sekorm['选型帮助'])
        return SelectionPage(self.driver)

    def go_ReplaceRecommendPage(self):
        """替代推荐"""
        self.is_click(sekorm['替代推荐'])
        self.go_to_element(sekorm['替代推荐'])
        return ReplaceRecommendPage(self.driver)

    def go_CommodityManagePage(self):
        """ON管理"""
        self.is_click(sekorm['ON管理'])
        self.go_to_element(sekorm['ON管理'])
        return CommodityManagePage(self.driver)

    def go_OrderManagePage(self):
        """订单与应收管理"""
        self.is_click(sekorm['订单与应收管理'])
        self.go_to_element(sekorm['订单与应收管理'])
        return OrderManagePage(self.driver)

    def go_TagPage(self):
        """标签管理"""
        self.is_click(sekorm['标签管理'])
        self.go_to_element(sekorm['标签管理'])
        return TagPage(self.driver)

    def go_ContentManagePage(self):
        """内容管理"""
        self.is_click(sekorm['内容管理'])
        self.go_to_element(sekorm['内容管理'])
        return ContentManagePage(self.driver)

    def go_StatisticsPage(self):
        """统计报表"""
        self.is_click(sekorm['统计报表'])
        self.go_to_element(sekorm['统计报表'])
        return StatisticsPage(self.driver)

    def go_GroupEmailPage(self):
        """邮件发送清单"""
        self.is_click(sekorm['邮件发送清单'])
        return GroupEmailPage(self.driver)

    def go_SalesPerformancePage(self):
        """销售业绩归属"""
        self.is_click(sekorm['销售业绩归属'])
        self.go_to_element(sekorm['销售业绩归属'])
        return SalesPerformancePage(self.driver)

    def go_DWAchievementPage(self):
        """DW核算管理"""
        self.is_click(sekorm['DW核算管理'])
        self.go_to_element(sekorm['DW核算管理'])
        return DWAchievementPage(self.driver)

    def go_SettingsPage(self):
        """设置"""
        self.is_click(sekorm['设置'])
        self.go_to_element(sekorm['设置'])
        return SettingsPage(self.driver)
