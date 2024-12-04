from common.readelement import Element
from page.basepage import BasePage
from page_object.B.CommodityManage.CustomerMaterialPage import CustomerMaterialPage
from page_object.B.CommodityManage.DeliveryAddrPage import DeliveryAddrPage
from page_object.B.CommodityManage.DiscountPage import DiscountPage
from page_object.B.CommodityManage.DynamictablePage import DynamictablePage
from page_object.B.CommodityManage.MultiLangOnManagePage import MultiLangOnManagePage
from page_object.B.CommodityManage.MultiLangOnSpManagePage import MultiLangOnSpManagePage
from page_object.B.CommodityManage.MultiLangOnVerifyPage import MultiLangOnVerifyPage
from page_object.B.CommodityManage.MyFilePage import MyFilePage
from page_object.B.CommodityManage.OnDocPage import OnDocPage
from page_object.B.CommodityManage.OnFirstConsumePage import OnFirstConsumePage
from page_object.B.CommodityManage.OnFirstConsumeToDoPage import OnFirstConsumeToDoPage
from page_object.B.CommodityManage.OnInventoryCheckPage import OnInventoryCheckPage
from page_object.B.CommodityManage.OnManagePage import OnManagePage
from page_object.B.CommodityManage.OnSpManagePage import OnSpManagePage
from page_object.B.CommodityManage.OnTransPage import OnTransPage
from page_object.B.CommodityManage.OnWeightSizePage import OnWeightSizePage
from page_object.B.CommodityManage.OnWorkPage import OnWorkPage
from page_object.B.CommodityManage.PreScreeningPage import PreScreeningPage
from page_object.B.CommodityManage.RestrictPage import RestrictPage
from page_object.B.CommodityManage.SaleProxyPage import SaleProxyPage
from page_object.B.CommodityManage.SupplySetPage import SupplySetPage

sekorm = Element('B_Element')


class CommodityManagePage(BasePage):
    """商品管理"""

    def go_OnManagePage(self):
        """ON管理－ON管理"""
        self.is_click(sekorm['ON管理－ON管理'])
        return OnManagePage(self.driver)

    def go_OnSpManagePage(self):
        """ON管理－ON服务商信息"""
        self.is_click(sekorm['ON管理－ON服务商信息'])
        return OnSpManagePage(self.driver)

    def go_MultiLangOnManagePage(self):
        """ON管理－ON多语言管理"""
        self.is_click(sekorm['ON管理－ON多语言管理'])
        return MultiLangOnManagePage(self.driver)

    def go_MultiLangOnSpManagePage(self):
        """ON管理－ON服务商信息Ex"""
        self.is_click(sekorm['ON管理－ON服务商信息Ex'])
        return MultiLangOnSpManagePage(self.driver)

    def go_MultiLangOnVerifyPage(self):
        """ON管理－ON审核"""
        self.is_click(sekorm['ON管理－ON审核'])
        return MultiLangOnVerifyPage(self.driver)

    def go_OnDocPage(self):
        """ON管理－资料关联ON"""
        self.is_click(sekorm['ON管理－资料关联ON'])
        return OnDocPage(self.driver)

    def go_OnTransPage(self):
        """ON管理－型号参数校对"""
        self.is_click(sekorm['ON管理－型号参数校对'])
        return OnTransPage(self.driver)

    def go_OnWeightSizePage(self):
        """ON管理－ON重量和尺寸维护"""
        self.is_click(sekorm['ON管理－ON重量和尺寸维护'])
        return OnWeightSizePage(self.driver)

    def go_SaleProxyPage(self):
        """ON管理－库存管理"""
        self.is_click(sekorm['ON管理－库存管理'])
        return SaleProxyPage(self.driver)

    def go_DynamictablePage(self):
        """ON管理－预期库存检查表"""
        self.is_click(sekorm['ON管理－预期库存检查表'])
        return DynamictablePage(self.driver)

    def go_OnInventoryCheckPage(self):
        """ON管理－库存检查"""
        self.is_click(sekorm['ON管理－库存检查'])
        return OnInventoryCheckPage(self.driver)

    def go_SupplySetPage(self):
        """ON管理－快购设置"""
        self.is_click(sekorm['ON管理－快购设置'])
        return SupplySetPage(self.driver)

    def go_DiscountPage(self):
        """ON管理－促销管理"""
        self.is_click(sekorm['ON管理－促销管理'])
        return DiscountPage(self.driver)

    def go_CustomerMaterialPage(self):
        """ON管理－客户物料"""
        self.is_click(sekorm['ON管理－客户物料'])
        return CustomerMaterialPage(self.driver)

    def go_RestrictPage(self):
        """ON管理－交易受限型号"""
        self.is_click(sekorm['ON管理－交易受限型号'])
        return RestrictPage(self.driver)

    def go_DeliveryAddrPage(self):
        """ON管理－发货地管理"""
        self.is_click(sekorm['ON管理－发货地管理'])
        return DeliveryAddrPage(self.driver)

    def go_OnFirstConsumePage(self):
        """ON管理－第一次消费ON清单"""
        self.is_click(sekorm['ON管理－第一次消费ON清单'])
        return OnFirstConsumePage(self.driver)

    def go_OnFirstConsumeToDoPage(self):
        """ON管理－第一次消费ON待办池"""
        self.is_click(sekorm['ON管理－第一次消费ON待办池'])
        return OnFirstConsumeToDoPage(self.driver)

    def go_MyFilePage(self):
        """ON管理－我的文件库"""
        self.is_click(sekorm['ON管理－我的文件库'])
        return MyFilePage(self.driver)

    def go_OnWorkPage(self):
        """ON管理－ON工作台"""
        self.is_click(sekorm['ON管理－ON工作台'])
        return OnWorkPage(self.driver)

    def go_PreScreeningPage(self):
        """ON管理－新增数据查询"""
        self.is_click(sekorm['ON管理－新增数据查询'])
        return PreScreeningPage(self.driver)
