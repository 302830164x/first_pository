from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.BaseData.BdmLabelList import BdmLabelList
from page_object.ECM.BaseData.BdmPosition import BdmPosition
from page_object.ECM.BaseData.CommodityKeyword.CmsKeywordAnalysisLog import CmsKeywordAnalysisLog
from page_object.ECM.BaseData.CommodityKeyword.CmsKeywordManage import CmsKeywordManage
from page_object.ECM.BaseData.CommodityKeyword.CmsSEOManage import CmsSEOManage
from page_object.ECM.BaseData.CommodityManage.EcdmPartnumber import EcdmPartnumber
from page_object.ECM.BaseData.CommodityManage.EcdmSeries import EcdmSeries
from page_object.ECM.BaseData.CommodityManage.EcdmSeriesType import EcdmSeriesType
from page_object.ECM.BaseData.CommodityType.EcdmGoodscategory import EcdmGoodscategory
from page_object.ECM.BaseData.CommodityType.EcdmGoodscategory1 import EcdmGoodscategory1
from page_object.ECM.BaseData.DdmEcNewSysCode import DdmEcNewSysCode
from page_object.ECM.BaseData.DdmEcdocType import DdmEcdocType
from page_object.ECM.BaseData.DdmVideoType import DdmVideoType
from page_object.ECM.BaseData.EcdmEleccategory import EcdmEleccategory
from page_object.ECM.BaseData.KeywordGoodsRack import KeywordGoodsRack
from page_object.ECM.BaseData.KeywordNewGoodsRack import KeywordNewGoodsRack
from page_object.ECM.BaseData.KeywordNewShelvesContent import KeywordNewShelvesContent
from page_object.ECM.BaseData.NewBrandManage.BrandApprovedList import BrandApprovedList
from page_object.ECM.BaseData.NewBrandManage.BrandChangeAuditList import BrandChangeAuditList
from page_object.ECM.BaseData.NewBrandManage.BrandUnapprovedList import BrandUnapprovedList
from page_object.ECM.BaseData.NewBrandManage.BrandWaitingApprovalList import BrandWaitingApprovalList
from page_object.ECM.BaseData.OnManage.OnManageList import OnManageList
from page_object.ECM.BaseData.OnManage.OnTranslationReview import OnTranslationReview
from page_object.ECM.BaseData.OnManage.OnVerify import OnVerify
from page_object.ECM.BaseData.PartnershipList import PartnershipList
from page_object.ECM.BaseData.SensitiveWords.SensitiveWordsList import SensitiveWordsList
from page_object.ECM.BaseData.SensitiveWords.SensitiveWordsLogList import SensitiveWordsLogList
from page_object.ECM.BaseData.ShelfCenterList import ShelfCenterList
from page_object.ECM.BaseData.ShelfConfigFormList import ShelfConfigFormList
from page_object.ECM.BaseData.SpmDrProjectSet import SpmDrProjectSet
from page_object.ECM.BaseData.WmsNavigationBarMenu import WmsNavigationBarMenu

sekorm = Element('EcmElement')


class BaseDataPage(BasePage):
    """基础资料页"""

    # ON待审核
    def go_OnVerify(self):
        self.is_click(sekorm['基础资料-ON管理-ON待审核'])
        return OnVerify(self.driver)

    # ON管理
    def go_OnManageList(self):
        self.is_click(sekorm['基础资料-ON管理-ON管理'])
        return OnManageList(self.driver)

    # ON参数校对审核
    def go_OnTranslationReview(self):
        self.is_click(sekorm['基础资料-ON管理-ON参数校对审核'])
        return OnTranslationReview(self.driver)

    # 型号管理
    def go_EcdmPartnumber(self):
        self.is_click(sekorm['基础资料-商品管理'])
        self.is_click(sekorm['基础资料-商品管理-型号管理'])
        return EcdmPartnumber(self.driver)

    # 系列型号管理
    def go_EcdmSeriesType(self):
        self.is_click(sekorm['基础资料-商品管理'])
        self.is_click(sekorm['基础资料-商品管理-系列型号管理'])
        return EcdmSeriesType(self.driver)

    # 系列管理
    def go_EcdmSeries(self):
        self.is_click(sekorm['基础资料-商品管理'])
        self.is_click(sekorm['基础资料-商品管理-系列管理'])
        return EcdmSeries(self.driver)

    # 旧分类
    def go_EcdmGoodscategory1(self):
        self.is_click(sekorm['基础资料-商品分类'])
        self.is_click(sekorm['基础资料-商品分类-旧分类'])
        return EcdmGoodscategory1(self.driver)

    # 新分类
    def go_EcdmGoodscategory(self):
        self.is_click(sekorm['基础资料-商品分类'])
        self.is_click(sekorm['基础资料-商品分类-新分类'])
        return EcdmGoodscategory(self.driver)

    # 市场应用
    def go_EcdmEleccategory(self):
        self.is_click(sekorm['基础资料-市场应用'])
        return EcdmEleccategory(self.driver)

    # 资讯类型管理
    def go_DdmEcNewSysCode(self):
        self.is_click(sekorm['基础资料-资讯类型管理'])
        return DdmEcNewSysCode(self.driver)

    # 资料类型管理
    def go_DdmEcdocType(self):
        self.is_click(sekorm['基础资料-资料类型管理'])
        return DdmEcdocType(self.driver)

    # 视频类型管理
    def go_DdmVideoType(self):
        self.is_click(sekorm['基础资料-视频类型管理'])
        return DdmVideoType(self.driver)

    # 敏感词库
    def go_SensitiveWordsList(self):
        self.is_click(sekorm['基础资料-敏感词管理'])
        self.is_click(sekorm['基础资料-敏感词管理-敏感词库'])
        return SensitiveWordsList(self.driver)

    # 敏感词日志
    def go_SensitiveWordsLogList(self):
        self.is_click(sekorm['基础资料-敏感词管理'])
        self.is_click(sekorm['基础资料-敏感词管理-敏感词日志'])
        return SensitiveWordsLogList(self.driver)

    # 职位
    def go_BdmPosition(self):
        self.is_click(sekorm['基础资料-职位'])
        return BdmPosition(self.driver)

    # 关键词管理
    def go_CmsKeywordManage(self):
        self.is_click(sekorm['基础资料-商品关键词管理'])
        self.is_click(sekorm['基础资料-商品关键词管理-关键词管理'])
        return CmsKeywordManage(self.driver)

    # SEO管理
    def go_CmsSEOManage(self):
        self.is_click(sekorm['基础资料-商品关键词管理'])
        self.is_click(sekorm['基础资料-商品关键词管理-SEO管理'])
        return CmsSEOManage(self.driver)

    # 关键词分解
    def go_CmsKeywordAnalysisLog(self):
        self.is_click(sekorm['基础资料-商品关键词管理'])
        self.is_click(sekorm['基础资料-商品关键词管理-关键词分解'])
        return CmsKeywordAnalysisLog(self.driver)

    # 品类货架
    def go_KeywordGoodsRack(self):
        self.is_click(sekorm['基础资料-品类货架'])
        return KeywordGoodsRack(self.driver)

    # 新品类货架
    def go_KeywordNewGoodsRack(self):
        self.is_click(sekorm['基础资料-新品类货架'])
        return KeywordNewGoodsRack(self.driver)

    # DR表单管理
    def go_SpmDrProjectSet(self):
        self.is_click(sekorm['基础资料-DR表单管理'])
        return SpmDrProjectSet(self.driver)

    # 货架内容查看
    def go_KeywordNewShelvesContent(self):
        self.is_click(sekorm['基础资料-货架内容查看'])
        return KeywordNewShelvesContent(self.driver)

    # 展示货架
    def go_WmsNavigationBarMenu(self):
        self.is_click(sekorm['基础资料-展示货架'])
        return WmsNavigationBarMenu(self.driver)

    # 平台标签维护
    def go_BdmLabelList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-平台标签维护'])
        return BdmLabelList(self.driver)

    # 货架表单管理
    def go_ShelfConfigFormList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-货架表单管理'])
        return ShelfConfigFormList(self.driver)

    # 货架配置管理
    def go_ShelfCenterList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-货架配置管理'])
        return ShelfCenterList(self.driver)

    # 待审核厂牌
    def go_BrandWaitingApprovalList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-新厂牌管理'])
        self.is_click(sekorm['基础资料-新厂牌管理-待审核厂牌'])
        return BrandWaitingApprovalList(self.driver)

    # 品牌变更审核
    def go_BrandChangeAuditList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-新厂牌管理'])
        self.is_click(sekorm['基础资料-新厂牌管理-品牌变更审核'])
        return BrandChangeAuditList(self.driver)

    # 审核未通过
    def go_BrandUnapprovedList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-新厂牌管理'])
        self.is_click(sekorm['基础资料-新厂牌管理-审核未通过'])
        return BrandUnapprovedList(self.driver)

    # 品牌数据库
    def go_BrandApprovedList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-新厂牌管理'])
        self.is_click(sekorm['基础资料-新厂牌管理-品牌数据库'])
        return BrandApprovedList(self.driver)

    # 合作关系
    def go_PartnershipList(self):
        self.go_to_element(sekorm['基础资料-展示货架'])
        self.is_click(sekorm['基础资料-合作关系'])
        return PartnershipList(self.driver)


