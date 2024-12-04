from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Provider.CommodityLable.WmsLabelManage import WmsLabelManage
from page_object.ECM.Provider.CommodityLable.WmsLabelManageSpManage import WmsLabelManageSpManage
from page_object.ECM.Provider.CommodityManage.AuthorizationManageList import AuthorizationManageList
from page_object.ECM.Provider.CommodityManage.CommodityManageList import CommodityManageList
from page_object.ECM.Provider.CommodityManage.CommodityVerify import CommodityVerify
from page_object.ECM.Provider.CommodityManage.PnOnManageOnSaleCategory import PnOnManageOnSaleCategory
from page_object.ECM.Provider.Consignment.HsMaterialsInfoList import HsMaterialsInfoList
from page_object.ECM.Provider.Consignment.OfflineRemainderList import OfflineRemainderList
from page_object.ECM.Provider.Consignment.SaleProxyList import SaleProxyList
from page_object.ECM.Provider.NewCommodityLable.LabelAuthcList import LabelAuthcList
from page_object.ECM.Provider.NewCommodityLable.LabelList import LabelList
from page_object.ECM.Provider.ProviderManage.CustomerMain import CustomerMain
from page_object.ECM.Provider.ProviderManage.SpmFunction import SpmFunction
from page_object.ECM.Provider.ProviderManage.SpmIncubator import SpmIncubator
from page_object.ECM.Provider.ProviderManage.SpmSpManager import SpmSpManager
from page_object.ECM.Provider.SpmChargingMod import SpmChargingMod
from page_object.ECM.Provider.SpmEnt import SpmEnt
from page_object.ECM.Provider.SpmEnterprise import SpmEnterprise
from page_object.ECM.Provider.SpmEpServiceTeam import SpmEpServiceTeam

sekorm = Element('EcmElement')


class ProviderPage(BasePage):
    """服务商页"""

    # 服务商管理
    def go_SpmSpManager(self):
        self.is_click(sekorm['服务商-服务商-服务商管理'])
        return SpmSpManager(self.driver)

    # 服务商客户管理
    def go_CustomerMain(self):
        self.is_click(sekorm['服务商-服务商-服务商客户管理'])
        return CustomerMain(self.driver)

    # 服务商功能管理
    def go_SpmFunction(self):
        self.is_click(sekorm['服务商-服务商-服务商功能管理'])
        return SpmFunction(self.driver)

    # 投资孵化申请
    def go_SpmIncubator(self):
        self.is_click(sekorm['服务商-服务商-投资孵化申请'])
        return SpmIncubator(self.driver)

    # 服务费管理
    def go_SpmChargingMod(self):
        self.is_click(sekorm['服务商-服务费管理'])
        return SpmChargingMod(self.driver)

    # 商品审核
    def go_CommodityVerify(self):
        self.is_click(sekorm['服务商-商品管理'])
        self.is_click(sekorm['服务商-商品管理-商品审核'])
        return CommodityVerify(self.driver)

    # 商品管理
    def go_CommodityManageList(self):
        self.is_click(sekorm['服务商-商品管理'])
        self.is_click(sekorm['服务商-商品管理-商品管理'])
        return CommodityManageList(self.driver)

    # 上架类别
    def go_PnOnManageOnSaleCategory(self):
        self.is_click(sekorm['服务商-商品管理'])
        self.is_click(sekorm['服务商-商品管理-上架类别'])
        return PnOnManageOnSaleCategory(self.driver)

    # ON授权管理
    def go_AuthorizationManageList(self):
        self.is_click(sekorm['服务商-商品管理'])
        self.is_click(sekorm['服务商-商品管理-ON授权管理'])
        return AuthorizationManageList(self.driver)

    # B端企业信息
    def go_SpmEnt(self):
        self.is_click(sekorm['服务商-B端企业信息'])
        return SpmEnt(self.driver)

    # 未上线提醒
    def go_OfflineRemainderList(self):
        self.is_click(sekorm['服务商-代销商品'])
        self.is_click(sekorm['服务商-代销商品-未上线提醒'])
        return OfflineRemainderList(self.driver)

    # 代销商品管理
    def go_SaleProxyList(self):
        self.is_click(sekorm['服务商-代销商品'])
        self.is_click(sekorm['服务商-代销商品-代销商品管理'])
        return SaleProxyList(self.driver)

    # 厚声物料表
    def go_HsMaterialsInfoList(self):
        self.is_click(sekorm['服务商-代销商品'])
        self.is_click(sekorm['服务商-代销商品-厚声物料表'])
        return HsMaterialsInfoList(self.driver)

    # 服务商授权管理
    def go_WmsLabelManageSpManage(self):
        self.is_click(sekorm['服务商-商品标签管理'])
        self.is_click(sekorm['服务商-商品标签管理-服务商授权管理'])
        return WmsLabelManageSpManage(self.driver)

    # 标签库
    def go_WmsLabelManage(self):
        self.is_click(sekorm['服务商-商品标签管理'])
        self.is_click(sekorm['服务商-商品标签管理-标签库'])
        return WmsLabelManage(self.driver)

    # 商品标签管理(新)-标签库
    def go_LabelList(self):
        self.is_click(sekorm['服务商-商品标签管理(新)'])
        self.is_click(sekorm['服务商-商品标签管理(新)-标签库'])
        return LabelList(self.driver)

    # 商品标签管理(新)-店铺标签授权管理
    def go_LabelAuthcList(self):
        self.is_click(sekorm['服务商-商品标签管理(新)'])
        self.is_click(sekorm['服务商-商品标签管理(新)-店铺标签授权管理'])
        return LabelAuthcList(self.driver)

    # 团队管理
    def go_SpmEpServiceTeam(self):
        self.is_click(sekorm['服务商-团队管理'])
        return SpmEpServiceTeam(self.driver)

    # 公有企业数据库
    def go_SpmEnterprise(self):
        self.is_click(sekorm['服务商-公有企业数据库'])
        return SpmEnterprise(self.driver)
