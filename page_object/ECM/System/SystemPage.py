from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.System.BdmAppv import BdmAppv
from page_object.ECM.System.BdmCountry import BdmCountry
from page_object.ECM.System.BdmRemind import BdmRemind
from page_object.ECM.System.DataDictionary.EcpParam import EcpParam
from page_object.ECM.System.DataDictionary.EcpParamterType import EcpParamterType
from page_object.ECM.System.EcpFunc import EcpFunc
from page_object.ECM.System.EcpOrgan import EcpOrgan
from page_object.ECM.System.EcpRole import EcpRole
from page_object.ECM.System.EcpTask import EcpTask
from page_object.ECM.System.EcpUser import EcpUser
from page_object.ECM.System.LimitingConfig.LimitMethodList import LimitMethodList
from page_object.ECM.System.LimitingConfig.LimitParentList import LimitParentList
from page_object.ECM.System.LimitingConfig.LimitUserList import LimitUserList
from page_object.ECM.System.LimitingConfig.LimitUserMethodList import LimitUserMethodList
from page_object.ECM.System.LogManage.BdmOperateLog import BdmOperateLog
from page_object.ECM.System.LogManage.BdmSendLog import BdmSendLog
from page_object.ECM.System.LogManage.BdmSysDown import BdmSysDown
from page_object.ECM.System.LogManage.BdmTaskLog import BdmTaskLog
from page_object.ECM.System.LogManage.StatSensitiveData import StatSensitiveData
from page_object.ECM.System.TaskManage.EcpTaskJobTrigger import EcpTaskJobTrigger
from page_object.ECM.System.TaskManage.EcpTaskSchedulerJob import EcpTaskSchedulerJob

sekorm = Element('EcmElement')


class SystemPage(BasePage):
    """系统管理页"""

    # 用户管理
    def go_EcpUser(self):
        self.is_click(sekorm['系统管理-用户管理'])
        return EcpUser(self.driver)

    # 角色管理
    def go_EcpRole(self):
        self.is_click(sekorm['系统管理-角色管理'])
        return EcpRole(self.driver)

    # 功能管理
    def go_EcpFunc(self):
        self.is_click(sekorm['系统管理-功能管理'])
        return EcpFunc(self.driver)

    # 机构管理
    def go_EcpOrgan(self):
        self.is_click(sekorm['系统管理-机构管理'])
        return EcpOrgan(self.driver)

    # 内部内容访问日志
    def go_StatSensitiveData(self):
        self.is_click(sekorm['系统管理-日志管理'])
        self.is_click(sekorm['系统管理-日志管理-内部内容访问日志'])
        return StatSensitiveData(self.driver)

    # 定时任务日志
    def go_BdmTaskLog(self):
        self.is_click(sekorm['系统管理-日志管理'])
        self.is_click(sekorm['系统管理-日志管理-定时任务日志'])
        return BdmTaskLog(self.driver)

    # App崩溃日志
    def go_BdmSysDown(self):
        self.is_click(sekorm['系统管理-日志管理'])
        self.is_click(sekorm['系统管理-日志管理-App崩溃日志'])
        return BdmSysDown(self.driver)

    # 发送日志
    def go_BdmSendLog(self):
        self.is_click(sekorm['系统管理-日志管理'])
        self.is_click(sekorm['系统管理-日志管理-发送日志'])
        return BdmSendLog(self.driver)

    # 操作日志
    def go_BdmOperateLog(self):
        self.is_click(sekorm['系统管理-日志管理'])
        self.is_click(sekorm['系统管理-日志管理-操作日志'])
        return BdmOperateLog(self.driver)

    # 省市区
    def go_BdmCountry(self):
        self.is_click(sekorm['系统管理-省市区'])
        return BdmCountry(self.driver)

    # APP版本管理
    def go_BdmAppv(self):
        self.is_click(sekorm['系统管理-APP版本管理'])
        return BdmAppv(self.driver)

    # 字典类型
    def go_EcpParamterType(self):
        self.is_click(sekorm['系统管理-数据字典管理'])
        self.is_click(sekorm['系统管理-数据字典管理-字典类型'])
        return EcpParamterType(self.driver)

    # 字典数据
    def go_EcpParam(self):
        self.is_click(sekorm['系统管理-数据字典管理'])
        self.is_click(sekorm['系统管理-数据字典管理-字典数据'])
        return EcpParam(self.driver)

    # 任务管理
    def go_EcpTask(self):
        self.is_click(sekorm['系统管理-任务管理'])
        return EcpTask(self.driver)

    # 邮件提醒
    def go_BdmRemind(self):
        self.is_click(sekorm['系统管理-邮件提醒'])
        return BdmRemind(self.driver)

    # 任务调度管理
    def go_EcpTaskSchedulerJob(self):
        self.is_click(sekorm['系统管理-调度中心'])
        self.is_click(sekorm['系统管理-调度中心-任务调度管理'])
        return EcpTaskSchedulerJob(self.driver)

    # 任务调度日志
    def go_EcpTaskJobTrigger(self):
        self.is_click(sekorm['系统管理-调度中心'])
        self.is_click(sekorm['系统管理-调度中心-任务调度日志'])
        return EcpTaskJobTrigger(self.driver)

    # 父类限流配置
    def go_LimitParentList(self):
        self.is_click(sekorm['系统管理-WEB端限流配置'])
        self.is_click(sekorm['系统管理-WEB端限流配置-父类限流配置'])
        return LimitParentList(self.driver)

    # WEB方法限流配置
    def go_LimitMethodList(self):
        self.is_click(sekorm['系统管理-WEB端限流配置'])
        self.is_click(sekorm['系统管理-WEB端限流配置-WEB方法限流配置'])
        return LimitMethodList(self.driver)

    # WEB登陆用户限流策略
    def go_LimitUserList(self):
        self.is_click(sekorm['系统管理-WEB端限流配置'])
        self.is_click(sekorm['系统管理-WEB端限流配置-WEB登陆用户限流策略'])
        return LimitUserList(self.driver)

    # WEB登陆用户的方法限流配置
    def go_LimitUserMethodList(self):
        self.is_click(sekorm['系统管理-WEB端限流配置'])
        self.is_click(sekorm['系统管理-WEB端限流配置-WEB登陆用户的方法限流配置'])
        return LimitUserMethodList(self.driver)
