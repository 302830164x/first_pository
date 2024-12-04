
from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Tag.ProductLabelPage import ProductLabelPage
from page_object.B.Tag.TagDatasetPage import TagDatasetPage
from page_object.B.Tag.TagManagePage import TagManagePage
from page_object.B.Tag.TagPrintPage import TagPrintPage
from page_object.B.Tag.TemplateManagePage import TemplateManagePage

sekorm = Element('B_Element')


class TagPage(BasePage):
    """标签管理"""

    def go_TagManagePage(self):
        """标签管理－标签模板"""
        self.is_click(sekorm['标签管理－标签模板'])
        return TagManagePage(self.driver)

    def go_TemplateManagePage(self):
        """标签管理－模板管理"""
        self.is_click(sekorm['标签管理－模板管理'])
        return TemplateManagePage(self.driver)

    def go_TagDatasetPage(self):
        """标签管理－API数据集"""
        self.is_click(sekorm['标签管理－API数据集'])
        return TagDatasetPage(self.driver)

    def go_ProductLabelPage(self):
        """标签管理－商品标签管理"""
        self.is_click(sekorm['标签管理－商品标签管理'])
        return ProductLabelPage(self.driver)

    def go_TagPrintPage(self):
        """标签管理－标签打印"""
        self.is_click(sekorm['标签管理－标签打印'])
        return TagPrintPage(self.driver)