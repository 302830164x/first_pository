from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnNewsDetailPage import EnNewsDetailPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage

Locator = {
    '资料标题': ('xpath', "//span[@class='item-title5 ']"),
    '发布时间': ('xpath', "//div[@class='sub-time']//span[1]"),
    '文件名称': ('xpath', "//div[@class='toolbar-detail-wrap']//li[1]/a"),
    '预览按钮': ('xpath', "//a[@id='line-view']"),
    'PDF预览组件': ('xpath', "//div[@id='viewer']"),
    '预览页下载按钮': ('xpath', "//a[normalize-space()='Download']"),
    '下载按钮': ('xpath', "//li[contains(@class,'last')]/a"),
    '资料内容': ('xpath', "//div[contains(@class,'cd-item-list mt10')]"),
    '文件预览': ('xpath', "//iframe[@id='doc_iframe']"),
    '底部下载按钮': ('xpath', "//div[contains(@class,'getdoc-box')]//a[normalize-space()='Download']"),
    '点赞': ('xpath', "//div[@class='last-content']//li[1]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect']"),
    '相关推荐': ('xpath', "//div[@class='mt15']"),
    '相关推荐-资料': ('xpath', "//div[@id='relatedRecom']//div[@class='module-tit-list']//a"),
    '相关推荐-资讯': ('xpath', "//div[@class='doc-detail']//div[1]//div[2]//a"),
    '相关推荐-查看更多': ('xpath', "//div[@id='relatedRecom']//a[@class='read-more'][normalize-space()='More>']"),
    '品牌墙': ('xpath', "//div[@id='content']//a[1]//img[1]"),
    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '登录提示': ('xpath', "//p[@class='form-error-msg']"),
    '登录弹窗关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),
}


class EnDocDetailPage(BasePage):
    """英文站资料详情页"""

    def check_en_doc_detail_layout(self):
        """检查资料详情页模块"""
        self.move_to_element(Locator['资料标题'])
        self.move_to_element(Locator['发布时间'])
        self.move_to_element(Locator['文件名称'])
        self.move_to_element(Locator['预览按钮'])
        self.move_to_element(Locator['下载按钮'])
        self.move_to_element(Locator['资料内容'])
        self.move_to_element(Locator['文件预览'])
        self.move_to_element(Locator['点赞'])
        self.move_to_element(Locator['收藏'])
        self.move_to_element(Locator['相关推荐'])
        self.move_to_element(Locator['品牌墙'])

    def click_doc_detail_right_brand(self):
        """点击右侧品牌墙"""
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_doc_detail_read_more(self):
        """点击相关推荐-查看更多"""
        self.is_click(Locator['相关推荐-查看更多'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_en_news_recommend(self):
        """点击资讯推荐"""
        self.is_click(Locator['相关推荐-资讯'])
        self.switch_window()
        return EnNewsDetailPage(self.driver)

    def click_en_doc_recommend(self):
        """点击资讯推荐"""
        self.is_click(Locator['相关推荐-资料'])
        self.switch_window()
        return EnDocDetailPage(self.driver)

    def unlogin_click_en_doc(self, elm):
        """资料详情页未登录点击"""
        self.is_click(Locator[elm])
        self.is_click(Locator['登录按钮'])
        text = self.element_text(Locator['登录提示'])
        self.is_click(Locator['登录弹窗关闭按钮'])
        return text

    def check_en_doc_like(self):
        """检查点赞按钮"""
        self.element_move_to_center(Locator['点赞'])
        text1 = self.get_attribute_value(Locator['点赞'], 'class')
        self.is_click(Locator['点赞'])
        text2 = self.get_attribute_value(Locator['点赞'], 'class')
        return text1, text2

    def login_click_preview(self):
        """资料详情页-登录后-点击预览"""
        self.is_click(Locator['预览按钮'])
        self.switch_window()
        self.move_to_element(Locator['PDF预览组件'])
        self.move_to_element(Locator['预览页下载按钮'])
        return self

    def login_click_favorites(self):
        """资料详情页-登录后-点击收藏"""
        self.is_click(Locator['收藏'])
