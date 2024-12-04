from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.DocsCollect.GeneralFilterPage import GeneralFilterPage
from page_object.CMS.DocsCollect.ImportFileurlPage import ImportFileurlPage
from page_object.CMS.DocsCollect.LinkMonitorPage import LinkMonitorPage
from page_object.CMS.DocsCollect.LinkValidatePage import LinkValidatePage
from page_object.CMS.DocsCollect.TaskDispatchPage import TaskDispatchPage
from page_object.CMS.DocsCollect.TaskMonitorPage import TaskMonitorPage
from page_object.CMS.DocsCollect.TitleSourcePage import TitleSourcePage
from page_object.CMS.DocsCollect.WebsitePage import WebsitePage

sekorm = Element('CmsElement')


class DocsCollectPage(BasePage):
    """资料采集"""

    def go_WebsitePage(self):
        """资料采集-地址管理"""
        self.is_click(sekorm['资料采集-地址管理'])
        return WebsitePage(self.driver)

    def go_TitleSourcePage(self):
        """资料采集-标题来源管理"""
        self.is_click(sekorm['资料采集-标题来源管理'])
        return TitleSourcePage(self.driver)

    def go_TaskDispatchPage(self):
        """资料采集-任务调度管理"""
        self.is_click(sekorm['资料采集-任务调度管理'])
        return TaskDispatchPage(self.driver)

    def go_TaskMonitorPage(self):
        """资料采集-采集情况管理"""
        self.is_click(sekorm['资料采集-采集情况管理'])
        return TaskMonitorPage(self.driver)

    def go_LinkMonitorPage(self):
        """资料采集-链接采集校验"""
        self.is_click(sekorm['资料采集-链接采集校验'])
        return LinkMonitorPage(self.driver)

    def go_LinkValidatePage(self):
        """资料采集-链接过滤校验"""
        self.is_click(sekorm['资料采集-链接过滤校验'])
        return LinkValidatePage(self.driver)

    def go_ImportFileurlPage(self):
        """资料采集-导入链接管理"""
        self.is_click(sekorm['资料采集-导入链接管理'])
        return ImportFileurlPage(self.driver)

    def go_GeneralFilterPage(self):
        """资料采集-通过过滤字符管理"""
        self.is_click(sekorm['资料采集-通用过滤字符管理'])
        return GeneralFilterPage(self.driver)
