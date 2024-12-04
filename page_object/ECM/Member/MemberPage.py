from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Member.AutoReg.AutoRegCompleted import AutoRegCompleted
from page_object.ECM.Member.AutoReg.AutoRegPending import AutoRegPending
from page_object.ECM.Member.MemberChangeInfo import MemberChangeInfo
from page_object.ECM.Member.MemberEmailMain import MemberEmailMain
from page_object.ECM.Member.MemberEnterpriseEpinfo import MemberEnterpriseEpinfo
from page_object.ECM.Member.MemberExperience.ExpExpManage import ExpExpManage
from page_object.ECM.Member.MemberExperience.ExpGradeLabel import ExpGradeLabel
from page_object.ECM.Member.MemberExperience.ExpGradeRule import ExpGradeRule
from page_object.ECM.Member.MemberGroup.ExpCredMem import ExpCredMem
from page_object.ECM.Member.MemberList.BlackListList import BlackListList
from page_object.ECM.Member.MemberList.MemberMemRegMemMain import MemberMemRegMemMain
from page_object.ECM.Member.MemberList.MemberMemSpMemMain import MemberMemSpMemMain
from page_object.ECM.Member.MemberList.MemberMemVipMemMain import MemberMemVipMemMain
from page_object.ECM.Member.MemberList.PotentialMember import PotentialMember
from page_object.ECM.Member.MemberOpinionMain import MemberOpinionMain
from page_object.ECM.Member.MemberProduct.MemberConcernCheckMain import MemberConcernCheckMain
from page_object.ECM.Member.MemberProduct.MemberConcernConcernMain import MemberConcernConcernMain
from page_object.ECM.Member.MemberProduct.MemberConcernDefMarkMain import MemberConcernDefMarkMain
from page_object.ECM.Member.MemberProduct.MemberConcernLogMain import MemberConcernLogMain
from page_object.ECM.Member.MemberReview.MemberWorkAbnormalList import MemberWorkAbnormalList
from page_object.ECM.Member.MemberReview.MemberWorkNotPassMember import MemberWorkNotPassMember
from page_object.ECM.Member.MemberReview.MemberWorkPass import MemberWorkPass
from page_object.ECM.Member.MemberReview.MemberWorkWaitAssessVerify import MemberWorkWaitAssessVerify
from page_object.ECM.Member.MemberVerifyHead import MemberVerifyHead
from page_object.ECM.Member.MemberVipMemberFilter import MemberVipMemberFilter
from page_object.ECM.Member.MemberVipMemberFilter_Email import MemberVipMemberFilter_Email
from page_object.ECM.Member.VerifyVerifyHelp import VerifyVerifyHelp
from page_object.ECM.Member.WhiteListMain import WhiteListMain

sekorm = Element('EcmElement')


class MemberPage(BasePage):
    """会员管理页"""

    # 跳转注册会员列表
    def go_MemberMemRegMemMain(self):
        self.is_click(sekorm['会员管理-会员列表-注册会员列表'])
        return MemberMemRegMemMain(self.driver)

    # 跳转VIP认证会员列表
    def go_MemberMemVipMemMain(self):
        self.is_click(sekorm['会员管理-会员列表-VIP认证会员列表'])
        return MemberMemVipMemMain(self.driver)

    # 跳转服务商会员列表
    def go_MemberMemSpMemMain(self):
        self.is_click(sekorm['会员管理-会员列表-服务商会员列表'])
        return MemberMemSpMemMain(self.driver)

    # 跳转手机黑名单
    def go_BlackListList(self):
        self.is_click(sekorm['会员管理-会员列表-手机黑名单'])
        return BlackListList(self.driver)

    # 跳转潜在会员
    def go_PotentialMember(self):
        self.is_click(sekorm['会员管理-会员列表-潜在会员'])
        return PotentialMember(self.driver)

    # 跳转VIP认证会员分组
    def go_ExpCredMem(self):
        self.is_click(sekorm['会员管理-会员分组'])
        self.is_click(sekorm['会员管理-会员分组-VIP认证会员分组'])
        return ExpCredMem(self.driver)

    # 跳转经验值管理
    def go_ExpExpManage(self):
        self.is_click(sekorm['会员管理-经验值等级头衔'])
        self.is_click(sekorm['会员管理-经验值等级头衔-经验值管理'])
        return ExpExpManage(self.driver)

    # 跳转等级规则
    def go_ExpGradeRule(self):
        self.is_click(sekorm['会员管理-经验值等级头衔'])
        self.is_click(sekorm['会员管理-经验值等级头衔-等级规则'])
        return ExpGradeRule(self.driver)

    # 跳转等级头衔
    def go_ExpGradeLabel(self):
        self.is_click(sekorm['会员管理-经验值等级头衔'])
        self.is_click(sekorm['会员管理-经验值等级头衔-等级头衔'])
        return ExpGradeLabel(self.driver)

    # 跳转产品匹配
    def go_MemberConcernConcernMain(self):
        self.is_click(sekorm['会员管理-会员产品'])
        self.is_click(sekorm['会员管理-会员产品-产品匹配'])
        return MemberConcernConcernMain(self.driver)

    # 跳转产品校正
    def go_MemberConcernCheckMain(self):
        self.is_click(sekorm['会员管理-会员产品'])
        self.is_click(sekorm['会员管理-会员产品-产品校正'])
        return MemberConcernCheckMain(self.driver)

    # 跳转默认市场
    def go_MemberConcernDefMarkMain(self):
        self.is_click(sekorm['会员管理-会员产品'])
        self.is_click(sekorm['会员管理-会员产品-默认市场'])
        return MemberConcernDefMarkMain(self.driver)

    # 跳转匹配日志
    def go_MemberConcernLogMain(self):
        self.is_click(sekorm['会员管理-会员产品'])
        self.is_click(sekorm['会员管理-会员产品-匹配日志'])
        return MemberConcernLogMain(self.driver)

    # 跳转会员信息审核
    def go_MemberWorkWaitAssessVerify(self):
        self.is_click(sekorm['会员管理-会员审核'])
        self.is_click(sekorm['会员管理-会员审核-会员信息审核'])
        return MemberWorkWaitAssessVerify(self.driver)

    # 跳转异常客户关联
    def go_MemberWorkAbnormalList(self):
        self.is_click(sekorm['会员管理-会员审核'])
        self.is_click(sekorm['会员管理-会员审核-异常客户关联'])
        return MemberWorkAbnormalList(self.driver)

    # 跳转通过审核的会员
    def go_MemberWorkPass(self):
        self.is_click(sekorm['会员管理-会员审核'])
        self.is_click(sekorm['会员管理-会员审核-通过审核的会员'])
        return MemberWorkPass(self.driver)

    # 跳转不通过审核的会员
    def go_MemberWorkNotPassMember(self):
        self.is_click(sekorm['会员管理-会员审核'])
        self.is_click(sekorm['会员管理-会员审核-不通过审核的会员'])
        return MemberWorkNotPassMember(self.driver)

    # 跳转发现工作变更
    def go_MemberChangeInfo(self):
        self.is_click(sekorm['会员管理-发现工作变更'])
        return MemberChangeInfo(self.driver)

    # 跳转头像审核
    def go_MemberVerifyHead(self):
        self.is_click(sekorm['会员管理-头像审核'])
        return MemberVerifyHead(self.driver)

    # 跳转电商客户管理
    def go_MemberEnterpriseEpinfo(self):
        self.is_click(sekorm['会员管理-电商客户管理'])
        return MemberEnterpriseEpinfo(self.driver)

    # 跳转电商客户白名单
    def go_WhiteListMain(self):
        self.is_click(sekorm['会员管理-电商客户白名单'])
        return WhiteListMain(self.driver)

    # 跳转手机过滤VIP会员
    def go_MemberVipMemberFilter(self):
        self.is_click(sekorm['会员管理-手机过滤VIP会员'])
        return MemberVipMemberFilter(self.driver)

    # 跳转邮箱过滤VIP会员
    def go_MemberVipMemberFilter_Email(self):
        self.is_click(sekorm['会员管理-邮箱过滤VIP会员'])
        return MemberVipMemberFilter_Email(self.driver)

    # 跳转意见反馈
    def go_MemberOpinionMain(self):
        self.is_click(sekorm['会员管理-意见反馈'])
        return MemberOpinionMain(self.driver)

    # 跳转邮箱域名管理
    def go_MemberEmailMain(self):
        self.is_click(sekorm['会员管理-邮箱域名管理'])
        return MemberEmailMain(self.driver)

    # 跳转验证工作邮箱
    def go_VerifyVerifyHelp(self):
        self.is_click(sekorm['会员管理-验证工作邮箱'])
        return VerifyVerifyHelp(self.driver)

    # 跳转待注册记录
    def go_AutoRegPending(self):
        self.go_to_element(sekorm['会员管理-验证工作邮箱'])
        self.is_click(sekorm['会员管理-自动注册会员'])
        self.is_click(sekorm['会员管理-自动注册会员-待注册记录'])
        return AutoRegPending(self.driver)

    # 跳转完成注册记录
    def go_AutoRegCompleted(self):
        self.go_to_element(sekorm['会员管理-验证工作邮箱'])
        self.is_click(sekorm['会员管理-自动注册会员'])
        self.is_click(sekorm['会员管理-自动注册会员-完成注册记录'])
        return AutoRegCompleted(self.driver)
