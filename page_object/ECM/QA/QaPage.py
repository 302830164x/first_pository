from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.QA.Business.PgcEmployeeRelation3 import PgcEmployeeRelation3
from page_object.ECM.QA.Business.PgcMyreceived3 import PgcMyreceived3
from page_object.ECM.QA.Business.PgcMytreated3 import PgcMytreated3
from page_object.ECM.QA.Business.PgcSubtreated3 import PgcSubtreated3
from page_object.ECM.QA.Business.PgcUnreceive3 import PgcUnreceive3
from page_object.ECM.QA.Operation.PgcOperationPool import PgcOperationPool
from page_object.ECM.QA.PgcInviteAnswer import PgcInviteAnswer
from page_object.ECM.QA.PgcPgcAuditAnsAudit import PgcPgcAuditAnsAudit
from page_object.ECM.QA.PgcPgcAuditQueAudit import PgcPgcAuditQueAudit
from page_object.ECM.QA.PgcPgcServiceList import PgcPgcServiceList
from page_object.ECM.QA.PgcPubPrepareAuditNotPass import PgcPubPrepareAuditNotPass
from page_object.ECM.QA.PgcPubPreparePublished import PgcPubPreparePublished
from page_object.ECM.QA.PgcPubPrepareQueAnsPub import PgcPubPrepareQueAnsPub
from page_object.ECM.QA.Technical.PgcEmployeeRelation2 import PgcEmployeeRelation2
from page_object.ECM.QA.Technical.PgcMyreceived2 import PgcMyreceived2
from page_object.ECM.QA.Technical.PgcMytreated2 import PgcMytreated2
from page_object.ECM.QA.Technical.PgcSubtreated2 import PgcSubtreated2
from page_object.ECM.QA.Technical.PgcUnreceive2 import PgcUnreceive2

sekorm = Element('EcmElement')


class QaPage(BasePage):
    """Q&A管理页"""

    # 新增提问
    def go_PgcPgcAuditQueAudit(self):
        self.is_click(sekorm['Q&A管理-新增提问'])
        return PgcPgcAuditQueAudit(self.driver)

    # 新增回答
    def go_PgcPgcAuditAnsAudit(self):
        self.is_click(sekorm['Q&A管理-新增回答'])
        return PgcPgcAuditAnsAudit(self.driver)

    # 待处理问题
    def go_PgcOperationPool(self):
        self.is_click(sekorm['Q&A管理-运营类池'])
        self.is_click(sekorm['Q&A管理-运营类池-待处理问题'])
        return PgcOperationPool(self.driver)

    # 技术类池 待认领问题
    def go_PgcUnreceive2(self):
        self.is_click(sekorm['Q&A管理-技术类池'])
        self.is_click(sekorm['Q&A管理-技术类池-待认领问题'])
        return PgcUnreceive2(self.driver)

    # 技术类池 我的认领
    def go_PgcMyreceived2(self):
        self.is_click(sekorm['Q&A管理-技术类池'])
        self.is_click(sekorm['Q&A管理-技术类池-我的认领'])
        return PgcMyreceived2(self.driver)

    # 技术类池 我处理的PGC
    def go_PgcMytreated2(self):
        self.is_click(sekorm['Q&A管理-技术类池'])
        self.is_click(sekorm['Q&A管理-技术类池-我处理的PGC'])
        return PgcMytreated2(self.driver)

    # 技术类池 我下属处理的PGC
    def go_PgcSubtreated2(self):
        self.is_click(sekorm['Q&A管理-技术类池'])
        self.is_click(sekorm['Q&A管理-技术类池-我下属处理的PGC'])
        return PgcSubtreated2(self.driver)

    # 技术类池 我的下属管理
    def go_PgcEmployeeRelation2(self):
        self.is_click(sekorm['Q&A管理-技术类池'])
        self.is_click(sekorm['Q&A管理-技术类池-我的下属管理'])
        return PgcEmployeeRelation2(self.driver)

    # 商务类池 待认领问题
    def go_PgcUnreceive3(self):
        self.is_click(sekorm['Q&A管理-商务类池'])
        self.is_click(sekorm['Q&A管理-商务类池-待认领问题'])
        return PgcUnreceive3(self.driver)

    # 商务类池 我的认领
    def go_PgcMyreceived3(self):
        self.is_click(sekorm['Q&A管理-商务类池'])
        self.is_click(sekorm['Q&A管理-商务类池-我的认领'])
        return PgcMyreceived3(self.driver)

    # 商务类池 我处理的PGC
    def go_PgcMytreated3(self):
        self.is_click(sekorm['Q&A管理-商务类池'])
        self.is_click(sekorm['Q&A管理-商务类池-我处理的PGC'])
        return PgcMytreated3(self.driver)

    # 商务类池 我下属处理的PGC
    def go_PgcSubtreated3(self):
        self.is_click(sekorm['Q&A管理-商务类池'])
        self.is_click(sekorm['Q&A管理-商务类池-我下属处理的PGC'])
        return PgcSubtreated3(self.driver)

    # 商务类池 我的下属管理
    def go_PgcEmployeeRelation3(self):
        self.is_click(sekorm['Q&A管理-商务类池'])
        self.is_click(sekorm['Q&A管理-商务类池-我的下属管理'])
        return PgcEmployeeRelation3(self.driver)

    # Q&A内容管理
    def go_PgcPubPrepareQueAnsPub(self):
        self.is_click(sekorm['Q&A管理-Q&A内容管理'])
        return PgcPubPrepareQueAnsPub(self.driver)

    # Q&A服务管理
    def go_PgcPgcServiceList(self):
        self.is_click(sekorm['Q&A管理-Q&A服务管理'])
        return PgcPgcServiceList(self.driver)

    # 通过的问答
    def go_PgcPubPreparePublished(self):
        self.is_click(sekorm['Q&A管理-通过的问答'])
        return PgcPubPreparePublished(self.driver)

    # 不通过的问答
    def go_PgcPubPrepareAuditNotPass(self):
        self.is_click(sekorm['Q&A管理-不通过的问答'])
        return PgcPubPrepareAuditNotPass(self.driver)

    # 邀请解答记录
    def go_PgcInviteAnswer(self):
        self.is_click(sekorm['Q&A管理-邀请解答记录'])
        return PgcInviteAnswer(self.driver)
