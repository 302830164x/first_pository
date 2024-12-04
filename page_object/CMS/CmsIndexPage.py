from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.BSubmitsContent.BSubmitsContentPage import BSubmitsContentPage
from page_object.CMS.ContentSettlement.ContentSettlementPage import ContentSettlementPage
from page_object.CMS.DocsCollect.DocsCollectPage import DocsCollectPage
from page_object.CMS.DocsProduce.DocsProducePage import DocsProducePage
from page_object.CMS.DocsPublish.DocsPublishPage import DocsPublishPage
from page_object.CMS.KeywordTranslation.KeywordTranslationPage import KeywordTranslationPage
from page_object.CMS.NewDocsManage.NewDocsManagePage import NewDocsManagePage
from page_object.CMS.NewsProduce.NewsProducePage import NewsProducePage
from page_object.CMS.NoticePage import NoticePage
from page_object.CMS.RemoveDuplication.RemoveDuplicationPage import RemoveDuplicationPage
from page_object.CMS.Settings.UsersManagePage import UsersManagePage
from page_object.CMS.UserCenterPage import UserCenterPage
from page_object.CMS.VideoManage.VideoManagePage import VideoManagePage

sekorm = Element('CmsElement')


class CmsIndexPage(BasePage):
    """首页类"""

    def get_cms_index_text(self):
        """获取登录后头部文本"""
        return self.element_text(sekorm['登录成功'])

    def get_cms_index_list_num(self):
        """获取列表数据总量"""
        return self.elements_num(sekorm['首页-数据'])

    def quit_cms_login(self):
        """退出登录"""
        self.is_click(sekorm['退出登录'])
        self.is_click(sekorm['确认退出'])
        return self

    def go_cms_login(self):
        """返回未登录页面对象"""
        from page_object.CMS.CmsLoginPage import CmsLoginPage
        return CmsLoginPage(self.driver)

    def go_CmsIndexPage(self):
        """首页"""
        self.is_click(sekorm['首页'])
        return CmsIndexPage(self.driver)

    def go_UserCenterPage(self):
        """个人中心"""
        self.is_click(sekorm['个人中心'])
        return UserCenterPage(self.driver)

    def go_NoticePage(self):
        """公告发布"""
        self.is_click(sekorm['公告发布'])
        return NoticePage(self.driver)

    def go_NewsProducePage(self):
        """资讯生产"""
        self.is_click(sekorm['资讯生产'])
        return NewsProducePage(self.driver)

    def go_DocsProducePage(self):
        """资料生产"""
        self.is_click(sekorm['资料生产'])
        return DocsProducePage(self.driver)

    def go_DocsCollectPage(self):
        """资料采集"""
        self.is_click(sekorm['资料采集'])
        return DocsCollectPage(self.driver)

    def go_NewDocsManagePage(self):
        """新增资料管理"""
        self.is_click(sekorm['新增资料管理'])
        return NewDocsManagePage(self.driver)

    def go_BSubmitsContentPage(self):
        """B台提交内容"""
        self.is_click(sekorm['B台提交内容'])
        return BSubmitsContentPage(self.driver)

    def go_KeywordTranslationPage(self):
        """关键词翻译"""
        self.is_click(sekorm['关键词翻译'])
        return KeywordTranslationPage(self.driver)

    def go_DocsPublishPage(self):
        """资料发布"""
        self.is_click(sekorm['资料发布'])
        return DocsPublishPage(self.driver)

    def go_RemoveDuplicationPage(self):
        """发布资料去重"""
        self.is_click(sekorm['发布资料去重'])
        return RemoveDuplicationPage(self.driver)

    def go_ContentSettlementPage(self):
        """内容结算"""
        self.is_click(sekorm['内容结算'])
        return ContentSettlementPage(self.driver)

    def go_VideoManagePage(self):
        """视频管理"""
        self.is_click(sekorm['视频管理'])
        return VideoManagePage(self.driver)

    def go_UsersManagePage(self):
        """设置-用户管理"""
        self.is_click(sekorm['设置'])
        self.is_click(sekorm['设置-用户管理'])
        return UsersManagePage(self.driver)
