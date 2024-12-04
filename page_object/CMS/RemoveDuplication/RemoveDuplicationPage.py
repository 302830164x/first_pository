from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.RemoveDuplication.EcdocRepeatPage import EcdocRepeatPage
from page_object.CMS.RemoveDuplication.EdocSuspectPage import EdocSuspectPage

sekorm = Element('CmsElement')


class RemoveDuplicationPage(BasePage):
    """发布资料去重"""

    def go_EcdocRepeatPage(self):
        """发布资料去重-重复资料"""
        self.is_click(sekorm['发布资料去重-重复资料'])
        return EcdocRepeatPage(self.driver)

    def go_EdocSuspectPage(self):
        """发布资料去重-疑似重复资料"""
        self.is_click(sekorm['发布资料去重-疑似重复资料'])
        return EdocSuspectPage(self.driver)
