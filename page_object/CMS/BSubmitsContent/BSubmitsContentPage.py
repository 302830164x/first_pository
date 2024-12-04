from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.BSubmitsContent.EcnewbPage import EcnewbPage
from page_object.CMS.BSubmitsContent.SelectionPage import SelectionPage
from page_object.CMS.BSubmitsContent.SpmsEcdocPage import SpmsEcdocPage

sekorm = Element('CmsElement')


class BSubmitsContentPage(BasePage):
    """B台提交内容"""

    def go_EcnewbPage(self):
        """B台提交内容-文章"""
        self.is_click(sekorm['B台提交内容-文章'])
        return EcnewbPage(self.driver)

    def go_SpmsEcdocPage(self):
        """B台提交内容-资料"""
        self.is_click(sekorm['B台提交内容-资料'])
        return SpmsEcdocPage(self.driver)

    def go_SelectionPage(self):
        """B台提交内容-选型表"""
        self.is_click(sekorm['B台提交内容-选型表'])
        return SelectionPage(self.driver)
