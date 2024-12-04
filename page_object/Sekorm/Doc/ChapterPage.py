from page.basepage import BasePage
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage

Locator = {
    '章节标题': ('xpath', "//h1[@id='article_title']"),
    '下载整本': ('xpath', "(//a[@class='btn-dlBox-opBorder'][contains(text(),'下载整本选型指南')])[1]"),
    'PDF预览': ('xpath', "//div[@id='viewer']"),
    '章节目录': ('xpath', "//div[@id='pageContainer3']//section[2]//a[1]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect select-collect']"),
    '邮箱分享': ('xpath', "//li[@class='email_share cd-email']"),
    '转发-微信': ('xpath', "//a[@class='bds_weixin']"),
    '转发-QQ': ('xpath', "//a[@class='bds_qzone']"),
    '转发-微博': ('xpath', "//a[@class='bds_tsina']"),
}


class ChapterPage(BasePage):
    """章节详情页"""

    def check_chapter_layout(self):
        """检查章节详情页模块"""
        title = self.element_text(Locator['章节标题'])
        self.move_to_element(Locator['下载整本'])
        self.move_to_element(Locator['PDF预览'])
        self.move_to_element(Locator['章节目录'])
        self.move_to_element(Locator['收藏'])
        self.move_to_element(Locator['邮箱分享'])
        self.move_to_element(Locator['转发-微信'])
        self.move_to_element(Locator['转发-QQ'])
        self.move_to_element(Locator['转发-微博'])
        return title

    def check_unlogin_bottom(self, elm):
        """检查未登录点击按钮"""
        self.is_click(Locator[elm])
        return UnLoginPage(self.driver)

    def check_menu(self):
        """检查章节详情页目录"""
        self.is_click(Locator['章节目录'])
        return self
