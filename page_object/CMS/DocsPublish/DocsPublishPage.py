
from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.DocsPublish.EcdocPublishPage import EcdocPublishPage
from page_object.CMS.DocsPublish.WrongWordPage import WrongWordPage

sekorm = Element('CmsElement')


class DocsPublishPage(BasePage):
    """资料发布"""

    def go_EcdocPublishPage(self):
        """资料发布-资料发布"""
        self.is_click(sekorm['资料发布-资料发布'])
        return EcdocPublishPage(self.driver)

    def go_WrongWordPage(self):
        """资料发布-原词有误处理"""
        self.is_click(sekorm['资料发布-原词有误处理'])
        return WrongWordPage(self.driver)
