from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.NewDocsManage.DuplicateFilePage import DuplicateFilePage
from page_object.CMS.NewDocsManage.NewDocPage import NewDocPage

sekorm = Element('CmsElement')


class NewDocsManagePage(BasePage):
    """新增资料管理"""

    def go_NewDocPage(self):
        """新增资料管理-资料管理"""
        self.is_click(sekorm['新增资料管理-资料管理'])
        return NewDocPage(self.driver)

    def go_DuplicateFilePage(self):
        """新增资料管理-疑似重复资料管理"""
        self.is_click(sekorm['新增资料管理-疑似重复资料管理'])
        return DuplicateFilePage(self.driver)
