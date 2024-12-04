from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.NewsProduce.Checker.MyAuditPage import MyAuditPage
from page_object.CMS.NewsProduce.Checker.WaitAuditPage import WaitAuditPage
from page_object.CMS.NewsProduce.Checker.WaitReceivePage import WaitReceivePage
from page_object.CMS.NewsProduce.NewsManager.DisabledEcnewPage import DisabledEcnewPage
from page_object.CMS.NewsProduce.NewsManager.EcnewKeywordCheckPage import EcnewKeywordCheckPage
from page_object.CMS.NewsProduce.NewsManager.ImportSubjectPage import ImportSubjectPage
from page_object.CMS.NewsProduce.NewsManager.ManageSettingsPage import ManageSettingsPage
from page_object.CMS.NewsProduce.NewsManager.NotPassEcnewPage import NotPassEcnewPage
from page_object.CMS.NewsProduce.NewsManager.NotPassedSubjectPage import NotPassedSubjectPage
from page_object.CMS.NewsProduce.NewsManager.PassedSubjectPage import PassedSubjectPage
from page_object.CMS.NewsProduce.NewsManager.PublishEcnewPage import PublishEcnewPage
from page_object.CMS.NewsProduce.NewsManager.WaitAuditSubjectPage import WaitAuditSubjectPage
from page_object.CMS.NewsProduce.NewsManager.WaitPublishEcnewPage import WaitPublishEcnewPage
from page_object.CMS.NewsProduce.Writer.AuthorEcnewPage import AuthorEcnewPage
from page_object.CMS.NewsProduce.Writer.PendingSubjectPage import PendingSubjectPage
from page_object.CMS.NewsProduce.Writer.ReceiveSubjectPage import ReceiveSubjectPage
from page_object.CMS.NewsProduce.Writer.SelfSubjectPage import SelfSubjectPage

sekorm = Element('CmsElement')


class NewsProducePage(BasePage):
    """资讯生产"""

    def go_SelfSubjectPage(self):
        """资讯生产-作者-提主题"""
        self.is_click(sekorm['资讯生产-作者'])
        self.is_click(sekorm['资讯生产-作者-提主题'])
        return SelfSubjectPage(self.driver)

    def go_ReceiveSubjectPage(self):
        """资讯生产-作者-提主题"""
        self.is_click(sekorm['资讯生产-作者'])
        self.is_click(sekorm['资讯生产-作者-待认领主题'])
        return ReceiveSubjectPage(self.driver)

    def go_PendingSubjectPage(self):
        """资讯生产-作者-已认领主题"""
        self.is_click(sekorm['资讯生产-作者'])
        self.is_click(sekorm['资讯生产-作者-已认领主题'])
        return PendingSubjectPage(self.driver)

    def go_AuthorEcnewPage(self):
        """资讯生产-作者-我的文章"""
        self.is_click(sekorm['资讯生产-作者'])
        self.is_click(sekorm['资讯生产-作者-我的文章'])
        return AuthorEcnewPage(self.driver)

    def go_WaitReceivePage(self):
        """资讯生产-审核专家-待认领文章"""
        self.is_click(sekorm['资讯生产-审核专家'])
        self.is_click(sekorm['资讯生产-审核专家-待认领文章'])
        return WaitReceivePage(self.driver)

    def go_WaitAuditPage(self):
        """资讯生产-审核专家-已认领文章"""
        self.is_click(sekorm['资讯生产-审核专家'])
        self.is_click(sekorm['资讯生产-审核专家-已认领文章'])
        return WaitAuditPage(self.driver)

    def go_MyAuditPage(self):
        """资讯生产-审核专家-我审核的文章"""
        self.is_click(sekorm['资讯生产-审核专家'])
        self.is_click(sekorm['资讯生产-审核专家-我审核的文章'])
        return MyAuditPage(self.driver)

    def go_WaitAuditSubjectPage(self):
        """资讯生产-资讯管理员-待审核主题"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-待审核主题'])
        return WaitAuditSubjectPage(self.driver)

    def go_PassedSubjectPage(self):
        """资讯生产-资讯管理员-已通过主题"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-已通过主题'])
        return PassedSubjectPage(self.driver)

    def go_NotPassedSubjectPage(self):
        """资讯生产-资讯管理员-未通过主题"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-未通过主题'])
        return NotPassedSubjectPage(self.driver)

    def go_WaitPublishEcnewPage(self):
        """资讯生产-资讯管理员-待发布文章"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-待发布文章'])
        return WaitPublishEcnewPage(self.driver)

    def go_PublishEcnewPage(self):
        """资讯生产-资讯管理员-已发布文章"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-已发布文章'])
        return PublishEcnewPage(self.driver)

    def go_NotPassEcnewPage(self):
        """资讯生产-资讯管理员-未通过文章"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-未通过文章'])
        return NotPassEcnewPage(self.driver)

    def go_DisabledEcnewPage(self):
        """资讯生产-资讯管理员-已失效文章"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-已失效文章'])
        return DisabledEcnewPage(self.driver)

    def go_ManageSettingsPage(self):
        """资讯生产-资讯管理员-管理设置"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-管理设置'])
        return ManageSettingsPage(self.driver)

    def go_ImportSubjectPage(self):
        """资讯生产-资讯管理员-导入主题"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-导入主题'])
        return ImportSubjectPage(self.driver)

    def go_EcnewKeywordCheckPage(self):
        """资讯生产-资讯管理员-关键词检查"""
        self.is_click(sekorm['资讯生产-资讯管理员'])
        self.is_click(sekorm['资讯生产-资讯管理员-关键词检查'])
        return EcnewKeywordCheckPage(self.driver)
