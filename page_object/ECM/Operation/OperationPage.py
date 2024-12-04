from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Operation.ActivityManage.ActiActivity import ActiActivity
from page_object.ECM.Operation.ActivityManage.ActiEnroll import ActiEnroll
from page_object.ECM.Operation.ActivityManage.ActiFormv import ActiFormv
from page_object.ECM.Operation.ActivityManage.ActiLabOrder import ActiLabOrder
from page_object.ECM.Operation.ActivityManage.ActiLotteryList import ActiLotteryList
from page_object.ECM.Operation.ActivityManage.ActiMouseReceive import ActiMouseReceive
from page_object.ECM.Operation.ActivityManage.ActiScoreStat import ActiScoreStat
from page_object.ECM.Operation.ActivityManage.AtatActiStatToActiDataCount import AtatActiStatToActiDataCount
from page_object.ECM.Operation.ActivityManage.SemiNarSignList import SemiNarSignList
from page_object.ECM.Operation.ActivityManage.SemiNarSignListSeminarlist import SemiNarSignListSeminarlist
from page_object.ECM.Operation.ActivityManage.StatMunichShowStat import StatMunichShowStat
from page_object.ECM.Operation.CommentManage.WmsCommentNopass import WmsCommentNopass
from page_object.ECM.Operation.CommentManage.WmsCommentPass import WmsCommentPass
from page_object.ECM.Operation.CommunicationChannel import CommunicationChannel
from page_object.ECM.Operation.ContentOperation.MarkList import MarkList
from page_object.ECM.Operation.ContentOperation.OperateList import OperateList
from page_object.ECM.Operation.ContentOperation.PendingList import PendingList
from page_object.ECM.Operation.CouponManage.WmsCoupon import WmsCoupon
from page_object.ECM.Operation.CouponManage.WmsCouponDetail import WmsCouponDetail
from page_object.ECM.Operation.EsTest.SelfInspection import SelfInspection
from page_object.ECM.Operation.HomeContent.WmsEnHomebanner import WmsEnHomebanner
from page_object.ECM.Operation.HomeContent.WmsGoodsBrand import WmsGoodsBrand
from page_object.ECM.Operation.HomeContent.WmsHomebanner import WmsHomebanner
from page_object.ECM.Operation.HomeContent.WmsHomerecomHomeFloor import WmsHomerecomHomeFloor
from page_object.ECM.Operation.HomeContent.WmsHomerecomPartnumber import WmsHomerecomPartnumber
from page_object.ECM.Operation.HomeContent.WmsHomerecomVip import WmsHomerecomVip
from page_object.ECM.Operation.MallManage.MallManageMallConfiguration import MallManageMallConfiguration
from page_object.ECM.Operation.MallManage.MallManageOrderFlow import MallManageOrderFlow
from page_object.ECM.Operation.McomServiceReminder import McomServiceReminder
from page_object.ECM.Operation.NewMember.EmailSharing import EmailSharing
from page_object.ECM.Operation.QuickPrhPay.QuickPrhCheckAccount import QuickPrhCheckAccount
from page_object.ECM.Operation.QuickPrhPay.QuickPrhPaidManage import QuickPrhPaidManage
from page_object.ECM.Operation.QuickPrhPay.QuickPrhPayManage import QuickPrhPayManage
from page_object.ECM.Operation.QuickPurchase.QuickPrhProgram import QuickPrhProgram
from page_object.ECM.Operation.RecomConfig.KeywordGraphRelationList import KeywordGraphRelationList
from page_object.ECM.Operation.RecomConfig.RecomAreaRule import RecomAreaRule
from page_object.ECM.Operation.RecomConfig.RecomCustom import RecomCustom
from page_object.ECM.Operation.RecomConfig.RecomHelp import RecomHelp
from page_object.ECM.Operation.RecomConfig.RecomLogin import RecomLogin
from page_object.ECM.Operation.RecomConfig.RecomOpera import RecomOpera
from page_object.ECM.Operation.RecomConfig.RecomRecomRuleUnloginNew import RecomRecomRuleUnloginNew
from page_object.ECM.Operation.RecomConfig.RecomScene import RecomScene
from page_object.ECM.Operation.RecomConfig.RecomTaskManage import RecomTaskManage
from page_object.ECM.Operation.RecomConfig.RecomUnlogin import RecomUnlogin
from page_object.ECM.Operation.RedisTest.RedisSelfInspection import RedisSelfInspection
from page_object.ECM.Operation.Restrict.PartnumberNewCustomerRestrictPool import PartnumberNewCustomerRestrictPool
from page_object.ECM.Operation.Restrict.PartnumberNewRestrictPool import PartnumberNewRestrictPool
from page_object.ECM.Operation.Restrict.PartnumberNewRestrictSetting import PartnumberNewRestrictSetting
from page_object.ECM.Operation.RestrictEnSitemap import RestrictEnSitemap
from page_object.ECM.Operation.RestrictLapseSitemapMain import RestrictLapseSitemapMain
from page_object.ECM.Operation.RestrictSiteMapImport import RestrictSiteMapImport
from page_object.ECM.Operation.SearchAnalysis.SearchAnalyzer import SearchAnalyzer
from page_object.ECM.Operation.SearchAnalysis.SearchClicks import SearchClicks
from page_object.ECM.Operation.SearchAnalysis.SearchConversion import SearchConversion
from page_object.ECM.Operation.SearchAnalysis.SearchDocManage import SearchDocManage
from page_object.ECM.Operation.SearchAnalysis.SearchDocManages import SearchDocManages
from page_object.ECM.Operation.SearchAnalysis.SearchIndexManager import SearchIndexManager
from page_object.ECM.Operation.SearchAnalysis.SekRgcKeyword import SekRgcKeyword
from page_object.ECM.Operation.SearchAnalysis.SekWordKeywordSource import SekWordKeywordSource
from page_object.ECM.Operation.SearchAnalysis.SekWordSignalSource import SekWordSignalSource
from page_object.ECM.Operation.SearchConfig.CompressString import CompressString
from page_object.ECM.Operation.SearchConfig.SearchRule import SearchRule
from page_object.ECM.Operation.SearchConfig.SearchWeight import SearchWeight
from page_object.ECM.Operation.SearchConfig.SearchWordType import SearchWordType
from page_object.ECM.Operation.SearchConfig.SekWordKeyword import SekWordKeyword
from page_object.ECM.Operation.SearchConfig.SekWordServiceResource import SekWordServiceResource
from page_object.ECM.Operation.SearchConfig.SekWordSynonym import SekWordSynonym
from page_object.ECM.Operation.StaticRefresh import StaticRefresh
from page_object.ECM.Operation.Supply.QuickPrhSupplySort import QuickPrhSupplySort
from page_object.ECM.Operation.Supply.SupplyChannelConfig import SupplyChannelConfig
from page_object.ECM.Operation.Supply.SupplyPartnumberSupply import SupplyPartnumberSupply
from page_object.ECM.Operation.WmsBrandLogo import WmsBrandLogo
from page_object.ECM.Operation.WmsEmailTool import WmsEmailTool
from page_object.ECM.Operation.WmsHotWord import WmsHotWord
from page_object.ECM.Operation.WmsMessage import WmsMessage
from page_object.ECM.Operation.WmsShortUrlToPage import WmsShortUrlToPage

sekorm = Element('EcmElement')


class OperationPage(BasePage):
    """运营管理页"""

    # 审核通过列表
    def go_WmsCommentPass(self):
        self.is_click(sekorm['运营管理-评论管理-审核通过列表'])
        return WmsCommentPass(self.driver)

    # 审核不通过列表
    def go_WmsCommentNopass(self):
        self.is_click(sekorm['运营管理-评论管理-审核不通过列表'])
        return WmsCommentNopass(self.driver)

    # 发布活动
    def go_ActiActivity(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-发布活动'])
        return ActiActivity(self.driver)

    # 表单管理
    def go_ActiFormv(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-表单管理'])
        return ActiFormv(self.driver)

    # 活动报名管理
    def go_ActiEnroll(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-活动报名管理'])
        return ActiEnroll(self.driver)

    # 活动数据统计
    def go_AtatActiStatToActiDataCount(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-活动数据统计'])
        return AtatActiStatToActiDataCount(self.driver)

    # 会员积分明细
    def go_ActiScoreStat(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-会员积分明细'])
        return ActiScoreStat(self.driver)

    # 送鼠标报名统计
    def go_ActiMouseReceive(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-送鼠标报名统计'])
        return ActiMouseReceive(self.driver)

    # 展会数据统计
    def go_StatMunichShowStat(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-展会数据统计'])
        return StatMunichShowStat(self.driver)

    # 实验室预约管理
    def go_ActiLabOrder(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-实验室预订管理'])
        return ActiLabOrder(self.driver)

    # 研讨会管理
    def go_SemiNarSignListSeminarlist(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-研讨会管理'])
        return SemiNarSignListSeminarlist(self.driver)

    # 研讨会签到
    def go_SemiNarSignList(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-研讨会签到'])
        return SemiNarSignList(self.driver)

    # 抽奖管理
    def go_ActiLotteryList(self):
        self.is_click(sekorm['运营管理-活动管理'])
        self.is_click(sekorm['运营管理-活动管理-抽奖管理'])
        return ActiLotteryList(self.driver)

    # 订单管制
    def go_PartnumberNewRestrictPool(self):
        self.is_click(sekorm['运营管理-出口管制'])
        self.is_click(sekorm['运营管理-出口管制-订单管制'])
        return PartnumberNewRestrictPool(self.driver)

    # 客户管制
    def go_PartnumberNewCustomerRestrictPool(self):
        self.is_click(sekorm['运营管理-出口管制'])
        self.is_click(sekorm['运营管理-出口管制-客户管制'])
        return PartnumberNewCustomerRestrictPool(self.driver)

    # 管制设置
    def go_PartnumberNewRestrictSetting(self):
        self.is_click(sekorm['运营管理-出口管制'])
        self.is_click(sekorm['运营管理-出口管制-管制设置'])
        return PartnumberNewRestrictSetting(self.driver)

    # 元件供应
    def go_SupplyPartnumberSupply(self):
        self.is_click(sekorm['运营管理-元件供应'])
        self.is_click(sekorm['运营管理-元件供应-元件供应'])
        return SupplyPartnumberSupply(self.driver)

    # 频道页排序
    def go_QuickPrhSupplySort(self):
        self.is_click(sekorm['运营管理-元件供应'])
        self.is_click(sekorm['运营管理-元件供应-频道页排序'])
        return QuickPrhSupplySort(self.driver)

    # APP频道页配置
    def go_SupplyChannelConfig(self):
        self.is_click(sekorm['运营管理-元件供应'])
        self.is_click(sekorm['运营管理-元件供应-APP频道页配置'])
        return SupplyChannelConfig(self.driver)

    # 商城设置
    def go_MallManageMallConfiguration(self):
        self.is_click(sekorm['运营管理-商城管理'])
        self.is_click(sekorm['运营管理-商城管理-商城设置'])
        return MallManageMallConfiguration(self.driver)

    # 平台交易流水
    def go_MallManageOrderFlow(self):
        self.is_click(sekorm['运营管理-商城管理'])
        self.is_click(sekorm['运营管理-商城管理-平台交易流水'])
        return MallManageOrderFlow(self.driver)

    # 奖券管理
    def go_WmsCoupon(self):
        self.is_click(sekorm['运营管理-奖券管理'])
        self.is_click(sekorm['运营管理-奖券管理-奖券管理'])
        return WmsCoupon(self.driver)

    # 奖券统计
    def go_WmsCouponDetail(self):
        self.is_click(sekorm['运营管理-奖券管理'])
        self.is_click(sekorm['运营管理-奖券管理-奖券统计'])
        return WmsCouponDetail(self.driver)

    # 品牌管理
    def go_WmsBrandLogo(self):
        self.is_click(sekorm['运营管理-品牌管理'])
        return WmsBrandLogo(self.driver)

    # 搜索热词设置
    def go_WmsHotWord(self):
        self.is_click(sekorm['运营管理-搜索热词设置'])
        return WmsHotWord(self.driver)

    # 系统消息
    def go_WmsMessage(self):
        self.is_click(sekorm['运营管理-系统消息'])
        return WmsMessage(self.driver)

    # VIP福利专区管理
    def go_WmsHomerecomVip(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-VIP福利专区管理'])
        return WmsHomerecomVip(self.driver)

    # 首页轮播图管理
    def go_WmsHomebanner(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-首页轮播图管理'])
        return WmsHomebanner(self.driver)

    # 首页楼层广告管理
    def go_WmsHomerecomHomeFloor(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-首页楼层广告管理'])
        return WmsHomerecomHomeFloor(self.driver)

    # 元件供应管理
    def go_WmsHomerecomPartnumber(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-元件供应管理'])
        return WmsHomerecomPartnumber(self.driver)

    # 英文版首页轮播图管理
    def go_WmsEnHomebanner(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-英文版首页轮播图管理'])
        return WmsEnHomebanner(self.driver)

    # 首页商城厂牌
    def go_WmsGoodsBrand(self):
        self.is_click(sekorm['运营管理-首页内容管理'])
        self.is_click(sekorm['运营管理-首页内容管理-首页商城厂牌'])
        return WmsGoodsBrand(self.driver)

    # 快购管理
    def go_QuickPrhProgram(self):
        self.is_click(sekorm['运营管理-小量快购'])
        self.is_click(sekorm['运营管理-小量快购-快购管理'])
        return QuickPrhProgram(self.driver)

    # 待确认收款
    def go_QuickPrhPayManage(self):
        self.is_click(sekorm['运营管理-快购对账'])
        self.is_click(sekorm['运营管理-快购对账-待确认收款'])
        return QuickPrhPayManage(self.driver)

    # 已确认收款
    def go_QuickPrhPaidManage(self):
        self.is_click(sekorm['运营管理-快购对账'])
        self.is_click(sekorm['运营管理-快购对账-已确认收款'])
        return QuickPrhPaidManage(self.driver)

    # 财务对账
    def go_QuickPrhCheckAccount(self):
        self.is_click(sekorm['运营管理-快购对账'])
        self.is_click(sekorm['运营管理-快购对账-财务对账'])
        return QuickPrhCheckAccount(self.driver)

    # 溯源记录查询工具
    def go_CompressString(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-溯源记录查询工具'])
        return CompressString(self.driver)

    # 服务资源词库管理
    def go_SekWordServiceResource(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-服务资源词库管理'])
        return SekWordServiceResource(self.driver)

    # 关键词管理工具
    def go_SekWordKeyword(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-关键词管理工具'])
        return SekWordKeyword(self.driver)

    # 索引查询设置
    def go_SearchWeight(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-索引查询设置'])
        return SearchWeight(self.driver)

    # 同义词管理
    def go_SekWordSynonym(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-同义词管理'])
        return SekWordSynonym(self.driver)

    # 词性管理
    def go_SearchWordType(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.is_click(sekorm['运营管理-搜索配置-词性管理'])
        return SearchWordType(self.driver)

    # 自定义规则管理
    def go_SearchRule(self):
        self.is_click(sekorm['运营管理-搜索配置'])
        self.go_to_element(sekorm['运营管理-搜索配置-词性管理'])
        self.is_click(sekorm['运营管理-搜索配置-自定义规则管理'])
        return SearchRule(self.driver)

    # 服务提醒管理
    def go_McomServiceReminder(self):
        self.is_click(sekorm['运营管理-服务提醒管理'])
        return McomServiceReminder(self.driver)

    # 分词分析
    def go_SearchAnalyzer(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-分词分析'])
        return SearchAnalyzer(self.driver)

    # 搜索分析
    def go_SearchDocManage(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-搜索分析'])
        return SearchDocManage(self.driver)

    # 权重分析
    def go_SearchIndexManager(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-权重分析'])
        return SearchIndexManager(self.driver)

    # 评分对比
    def go_SearchDocManages(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-评分对比'])
        return SearchDocManages(self.driver)

    # RGC分析
    def go_SekRgcKeyword(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-RGC分析'])
        return SekRgcKeyword(self.driver)

    # 点击统计
    def go_SearchClicks(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-点击统计'])
        return SearchClicks(self.driver)

    # 搜索转化分析
    def go_SearchConversion(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-搜索转化分析'])
        return SearchConversion(self.driver)

    # 关键词朔源查询
    def go_SekWordKeywordSource(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-关键词朔源查询'])
        return SekWordKeywordSource(self.driver)

    # 短型号词朔源查询
    def go_SekWordSignalSource(self):
        self.is_click(sekorm['运营管理-搜索分析'])
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-搜索分析-短型号词朔源查询'])
        return SekWordSignalSource(self.driver)

    # ES自检-配置查询
    def go_SelfInspection(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-ES自检'])
        self.is_click(sekorm['运营管理-ES自检-配置查询'])
        return SelfInspection(self.driver)

    # Redis自检-配置查询
    def go_RedisSelfInspection(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-Redis自检'])
        self.is_click(sekorm['运营管理-Redis自检-配置查询'])
        return RedisSelfInspection(self.driver)

    # 推荐场景配置
    def go_RecomScene(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-推荐场景配置'])
        return RecomScene(self.driver)

    # 未登录配置
    def go_RecomUnlogin(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-未登录配置'])
        return RecomUnlogin(self.driver)

    # 已登录配置
    def go_RecomLogin(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-已登录配置'])
        return RecomLogin(self.driver)

    # 未登录配置（新）
    def go_RecomRecomRuleUnloginNew(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-未登录配置（新）'])
        return RecomRecomRuleUnloginNew(self.driver)

    # 区域规则配置
    def go_RecomAreaRule(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-区域规则配置'])
        return RecomAreaRule(self.driver)

    # 运营规则配置
    def go_RecomOpera(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-运营规则配置'])
        return RecomOpera(self.driver)

    # 自定义内容管理
    def go_RecomCustom(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-自定义内容管理'])
        return RecomCustom(self.driver)

    # 推荐帮助信息
    def go_RecomHelp(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-推荐帮助信息'])
        return RecomHelp(self.driver)

    # 任务管理
    def go_RecomTaskManage(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-任务管理'])
        return RecomTaskManage(self.driver)

    # 二元关系图谱分析
    def go_KeywordGraphRelationList(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-推荐配置'])
        self.go_to_element(sekorm['运营管理-推荐配置'])
        self.is_click(sekorm['运营管理-推荐配置-二元关系图谱分析'])
        return KeywordGraphRelationList(self.driver)

    # SEO文件生成
    def go_RestrictSiteMapImport(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-SEO文件生成'])
        return RestrictSiteMapImport(self.driver)

    # 英文站SEO链接
    def go_RestrictEnSitemap(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-英文站SEO链接'])
        return RestrictEnSitemap(self.driver)

    # 标识管理
    def go_MarkList(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-内容运营功能'])
        self.is_click(sekorm['运营管理-内容运营功能-标识管理'])
        return MarkList(self.driver)

    # 待处理内容
    def go_PendingList(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-内容运营功能'])
        self.is_click(sekorm['运营管理-内容运营功能-待处理内容'])
        return PendingList(self.driver)

    # 运营内容管理
    def go_OperateList(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-内容运营功能'])
        self.is_click(sekorm['运营管理-内容运营功能-运营内容管理'])
        return OperateList(self.driver)

    # 短链生成工具
    def go_WmsShortUrlToPage(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-短链生成工具'])
        return WmsShortUrlToPage(self.driver)

    # 404链接生成
    def go_RestrictLapseSitemapMain(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-404链接生成'])
        return RestrictLapseSitemapMain(self.driver)

    # 公用通讯通道
    def go_CommunicationChannel(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-公用通讯通道'])
        return CommunicationChannel(self.driver)

    # 静态页刷新工具
    def go_StaticRefresh(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-静态页刷新工具'])
        return StaticRefresh(self.driver)

    # 批量邮件发送工具
    def go_WmsEmailTool(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-批量邮件发送工具'])
        return WmsEmailTool(self.driver)

    # 邮件导出
    def go_EmailSharing(self):
        self.go_to_element(sekorm['运营管理-搜索分析'])
        self.is_click(sekorm['运营管理-会员拉新'])
        self.go_to_element(sekorm['运营管理-会员拉新'])
        self.is_click(sekorm['运营管理-会员拉新-邮件导出'])
        return EmailSharing(self.driver)


