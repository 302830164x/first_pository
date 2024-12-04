from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.ContentSettlement.BillRuleAuditPage import BillRuleAuditPage
from page_object.CMS.ContentSettlement.DocsKeyinSettlement.KeyinBillCountPage import KeyinBillCountPage
from page_object.CMS.ContentSettlement.DocsKeyinSettlement.KeyinBillRulePage import KeyinBillRulePage
from page_object.CMS.ContentSettlement.DocsKeyinSettlement.KeyinBillSourcePage import KeyinBillSourcePage
from page_object.CMS.ContentSettlement.DocsTranslationSettlement.TransBillCountPage import TransBillCountPage
from page_object.CMS.ContentSettlement.DocsTranslationSettlement.TransBillRulePage import TransBillRulePage
from page_object.CMS.ContentSettlement.DocsTranslationSettlement.TransBillSourcePage import TransBillSourcePage
from page_object.CMS.ContentSettlement.NewsSettlement.BillCountPage import BillCountPage
from page_object.CMS.ContentSettlement.NewsSettlement.BillRulePage import BillRulePage
from page_object.CMS.ContentSettlement.NewsSettlement.BillSourcePage import BillSourcePage

sekorm = Element('CmsElement')


class ContentSettlementPage(BasePage):
    """内容结算"""

    def go_BillCountPage(self):
        """内容结算-资讯结算-资讯结算报表"""
        self.is_click(sekorm['内容结算-资讯结算'])
        self.is_click(sekorm['内容结算-资讯结算-资讯结算报表'])
        return BillCountPage(self.driver)

    def go_BillRulePage(self):
        """内容结算-资讯结算-资讯计费规则配置"""
        self.is_click(sekorm['内容结算-资讯结算'])
        self.is_click(sekorm['内容结算-资讯结算-资讯计费规则配置'])
        return BillRulePage(self.driver)

    def go_BillSourcePage(self):
        """内容结算-资讯结算-资讯计费原始报表"""
        self.is_click(sekorm['内容结算-资讯结算'])
        self.is_click(sekorm['内容结算-资讯结算-资讯计费原始报表'])
        return BillSourcePage(self.driver)

    def go_KeyinBillCountPage(self):
        """内容结算-资料KEYIN结算-KEYIN结算报表"""
        self.is_click(sekorm['内容结算-资料KEYIN结算'])
        self.is_click(sekorm['内容结算-资料KEYIN结算-KEYIN结算报表'])
        return KeyinBillCountPage(self.driver)

    def go_KeyinBillRulePage(self):
        """内容结算-资料KEYIN结算-KEYIN规则配置"""
        self.is_click(sekorm['内容结算-资料KEYIN结算'])
        self.is_click(sekorm['内容结算-资料KEYIN结算-KEYIN规则配置'])
        return KeyinBillRulePage(self.driver)

    def go_KeyinBillSourcePage(self):
        """内容结算-资料KEYIN结算-KEYIN原始报表"""
        self.is_click(sekorm['内容结算-资料KEYIN结算'])
        self.is_click(sekorm['内容结算-资料KEYIN结算-KEYIN原始报表'])
        return KeyinBillSourcePage(self.driver)

    def go_TransBillCountPage(self):
        """内容结算-资料翻译结算-翻译结算报表"""
        self.is_click(sekorm['内容结算-资料翻译结算'])
        self.is_click(sekorm['内容结算-资料翻译结算-翻译结算报表'])
        return TransBillCountPage(self.driver)

    def go_TransBillRulePage(self):
        """内容结算-资料翻译结算-翻译规则配置"""
        self.is_click(sekorm['内容结算-资料翻译结算'])
        self.is_click(sekorm['内容结算-资料翻译结算-翻译规则配置'])
        return TransBillRulePage(self.driver)

    def go_TransBillSourcePage(self):
        """内容结算-资料翻译结算-翻译原始报表"""
        self.is_click(sekorm['内容结算-资料翻译结算'])
        self.is_click(sekorm['内容结算-资料翻译结算-翻译原始报表'])
        return TransBillSourcePage(self.driver)

    def go_BillRuleAuditPage(self):
        """内容结算-内容计费规则审核"""
        self.is_click(sekorm['内容结算-内容计费规则审核'])
        return BillRuleAuditPage(self.driver)
