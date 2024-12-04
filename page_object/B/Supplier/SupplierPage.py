from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Supplier.BrandManagePage import BrandManagePage
from page_object.B.Supplier.MailTemplateManagementPage import MailTemplateManagementPage
from page_object.B.Supplier.MySupplierBenchPage import MySupplierBenchPage
from page_object.B.Supplier.SupplierBenchPage import SupplierBenchPage
from page_object.B.Supplier.SupplierEvaluteBenchPoolPage import SupplierEvaluteBenchPoolPage

sekorm = Element('B_Element')


class SupplierPage(BasePage):
    """供应商工作台"""

    def go_SupplierBenchPage(self):
        """供应商工作台-全部供应商"""
        self.is_click(sekorm['供应商工作台-全部供应商'])
        return SupplierBenchPage(self.driver)

    def go_MySupplierBenchPage(self):
        """供应商工作台-我的供应商"""
        self.is_click(sekorm['供应商工作台-我的供应商'])
        return MySupplierBenchPage(self.driver)

    def go_SupplierEvaluteBenchPoolPage(self):
        """供应商工作台-供应商评价体系"""
        self.is_click(sekorm['供应商工作台-供应商评价体系'])
        return SupplierEvaluteBenchPoolPage(self.driver)

    def go_MailTemplateManagementPage(self):
        """供应商工作台-邮件模板管理"""
        self.is_click(sekorm['供应商工作台-邮件模板管理'])
        return MailTemplateManagementPage(self.driver)

    def go_BrandManagePage(self):
        """供应商工作台-品牌管理"""
        self.is_click(sekorm['供应商工作台-品牌管理'])
        return BrandManagePage(self.driver)
