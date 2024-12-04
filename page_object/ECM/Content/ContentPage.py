from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Content.AdvertisingManage.WmsAdvertLeftManageMain import WmsAdvertLeftManageMain
from page_object.ECM.Content.AdvertisingManage.WmsAdvertList import WmsAdvertList
from page_object.ECM.Content.AdvertisingManage.WmsH5AdvertMain import WmsH5AdvertMain
from page_object.ECM.Content.AdvertisingManage.WmsLoadimgList import WmsLoadimgList
from page_object.ECM.Content.AdvertisingManage.WmsTextadsList import WmsTextadsList
from page_object.ECM.Content.BdmQrCodeMain import BdmQrCodeMain
from page_object.ECM.Content.CmsEcdocShow import CmsEcdocShow
from page_object.ECM.Content.CmsEcnewMain import CmsEcnewMain
from page_object.ECM.Content.EcdocImpt import EcdocImpt
from page_object.ECM.Content.MessageManage.WmsMobileMessageList import WmsMobileMessageList
from page_object.ECM.Content.SeleDocManageList import SeleDocManageList
from page_object.ECM.Content.SelectionEcdoc import SelectionEcdoc
from page_object.ECM.Content.SpreadManage.WmsEcDataAdvert import WmsEcDataAdvert
from page_object.ECM.Content.SpreadManage.WmsVideo import WmsVideo

sekorm = Element('EcmElement')


class ContentPage(BasePage):
    """内容管理页"""

    # 内容管理-广告管理-App启动广告
    def go_WmsLoadimgList(self):
        self.is_click(sekorm['内容管理-广告管理-App启动广告'])
        return WmsLoadimgList(self.driver)

    # 内容管理-广告管理-Web右侧广告
    def go_WmsAdvertList(self):
        self.is_click(sekorm['内容管理-广告管理-Web右侧广告'])
        return WmsAdvertList(self.driver)

    # 内容管理-广告管理-Web左侧广告
    def go_WmsAdvertLeftManageMain(self):
        self.is_click(sekorm['内容管理-广告管理-Web左侧广告'])
        return WmsAdvertLeftManageMain(self.driver)

    # 跳转H5分享页广告图
    def go_WmsH5AdvertMain(self):
        self.is_click(sekorm['内容管理-广告管理-H5分享页广告图'])
        return WmsH5AdvertMain(self.driver)

    # 跳转文字广告管理
    def go_WmsTextadsList(self):
        self.is_click(sekorm['内容管理-广告管理-文字广告管理'])
        return WmsTextadsList(self.driver)

    # 跳转展会管理
    def go_WmsEcDataAdvert(self):
        self.is_click(sekorm['内容管理-内容推广管理'])
        self.is_click(sekorm['内容管理-内容推广管理-展会管理'])
        return WmsEcDataAdvert(self.driver)

    # 跳转视频管理
    def go_WmsVideo(self):
        self.is_click(sekorm['内容管理-内容推广管理'])
        self.is_click(sekorm['内容管理-内容推广管理-视频管理'])
        return WmsVideo(self.driver)

    # 跳转资讯发布
    def go_CmsEcnewMain(self):
        self.is_click(sekorm['内容管理-资讯发布'])
        return CmsEcnewMain(self.driver)

    # 跳转产品选型列表
    def go_SeleDocManageList(self):
        self.is_click(sekorm['内容管理-产品选型列表'])
        return SeleDocManageList(self.driver)

    # 跳转资料导入
    def go_EcdocImpt(self):
        self.is_click(sekorm['内容管理-资料导入'])
        return EcdocImpt(self.driver)

    # 跳转产品选型管理
    def go_SelectionEcdoc(self):
        self.is_click(sekorm['内容管理-产品选型管理'])
        return SelectionEcdoc(self.driver)

    # 跳转资料预览配置
    def go_CmsEcdocShow(self):
        self.is_click(sekorm['内容管理-资料预览配置'])
        return CmsEcdocShow(self.driver)

    # 跳转 消息管理-APP消息推送
    def go_WmsMobileMessageList(self):
        self.is_click(sekorm['内容管理-消息管理'])
        self.is_click(sekorm['内容管理-消息管理-APP消息推送'])
        return WmsMobileMessageList(self.driver)

    # 跳转二维码管理
    def go_BdmQrCodeMain(self):
        self.is_click(sekorm['内容管理-二维码管理'])
        return BdmQrCodeMain(self.driver)
