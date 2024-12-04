
from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.KeywordTranslation.TransReplaceManagePage import TransReplaceManagePage
from page_object.CMS.KeywordTranslation.TranslationManagePage import TranslationManagePage

sekorm = Element('CmsElement')


class KeywordTranslationPage(BasePage):
    """关键词翻译"""

    def go_TranslationManagePage(self):
        """关键词翻译-已翻译管理"""
        self.is_click(sekorm['关键词翻译-已翻译管理'])
        return TranslationManagePage(self.driver)

    def go_TransReplaceManagePage(self):
        """关键词翻译-翻译替换管理"""
        self.is_click(sekorm['关键词翻译-翻译替换管理'])
        return TransReplaceManagePage(self.driver)