from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Delivery.DeliveryManage.GiftSend import GiftSend
from page_object.ECM.Delivery.GiftDeliver.GiftPrizeGroupManagement import GiftPrizeGroupManagement
from page_object.ECM.Delivery.GiftDeliver.GiftSubject import GiftSubject
from page_object.ECM.Delivery.MallStock.GiftExpStock import GiftExpStock
from page_object.ECM.Delivery.MallStock.GiftStock import GiftStock
from page_object.ECM.Delivery.MallStock.WmsCouponGiftMain import WmsCouponGiftMain

sekorm = Element('EcmElement')


class DeliveryPage(BasePage):
    """交付管理页"""

    # 实物仓库
    def go_GiftStock(self):
        self.is_click(sekorm['交付管理-电商仓库-实物仓库'])
        return GiftStock(self.driver)

    # 奖券仓库
    def go_WmsCouponGiftMain(self):
        self.is_click(sekorm['交付管理-电商仓库-奖券仓库'])
        return WmsCouponGiftMain(self.driver)

    # 经验值仓库
    def go_GiftExpStock(self):
        self.is_click(sekorm['交付管理-电商仓库-经验值仓库'])
        return GiftExpStock(self.driver)

    # 礼品发放需求管理
    def go_GiftSubject(self):
        self.is_click(sekorm['交付管理-礼品发放'])
        self.is_click(sekorm['交付管理-礼品发放-礼品发放需求管理'])
        return GiftSubject(self.driver)

    # 奖品分组管理
    def go_GiftPrizeGroupManagement(self):
        self.is_click(sekorm['交付管理-礼品发放'])
        self.is_click(sekorm['交付管理-礼品发放-奖品分组管理'])
        return GiftPrizeGroupManagement(self.driver)

    # 电商发货管理
    def go_GiftSend(self):
        self.is_click(sekorm['交付管理-电商交付平台'])
        self.is_click(sekorm['交付管理-电商交付平台-电商发货管理'])
        return GiftSend(self.driver)


