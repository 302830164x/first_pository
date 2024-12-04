from page_object.Sekorm.Doc.ChapterPage import ChapterPage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.times import sleep

Locator = {
    '资料标题': ('xpath', "//span[@class='item-title5 ']"),
    '发布时间': ('xpath', "//span[@class='servcie-top-block-time']"),
    'PDF': ('xpath', "(//div[@class='toolbar-list clearfix']//a)[1]"),
    '文件大小': ('xpath', "//li[@class='doc-size en-size']/span"),
    '预览': ('xpath', "(//div[@class='toolbar-list clearfix']//a)[3]"),
    '预览页PDF组件': ('xpath', "//div[@class='textLayer']"),
    '预览页下载按钮': ('xpath', "//a[contains(text(),'下载资料')]"),
    '我要下载': ('xpath', "(//div[@class='toolbar-list clearfix']//a)[2]"),
    '资料内容': ('xpath', "//div[@class='cd-content']"),
    '资料信息': ('xpath', "//div[@class='cd-item-list mt10']//label"),
    '资料部分预览': ('xpath', "//div[@class='doc-pdfView-wrap']"),
    '选型目录': ('xpath', "//div[@class='select-list']"),
    '目录章节': ('xpath', "//div[@class='select-list']//a"),
    '资料-厂牌': ('xpath', "//td[@id='brands']//a"),
    '资料-型号': ('xpath', "//tr[@class='doc-pn-list']//p[@class='cd-item-content cd-item-maxhide']//a"),
    '资料-品类': ('xpath', "//tr[@class='doc-goods-list']//p[@class='cd-item-content cd-item-maxhide']//a"),
    '资料-应用': ('xpath', "//tr[@class='doc-elec-list']//p[@class='cd-item-content cd-item-maxhide']//a"),
    '资料-登录': ('xpath', "//a[@class='header_user_unlogin']"),
    '资料-注册': ('xpath', "//a[@class='user-menu-last header_user_unlogin']"),
    '立即下载完整资料': ('xpath', "//a[contains(text(),'立即下载完整资料')]"),
    '发送到邮箱': ('xpath', "//li[@class='email_share cd-email']"),
    '点赞': ('xpath', "//ul[@class='last clearfix']//li[2]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect']"),
    '评论': ('xpath', "//li[@class='cd-comment']"),
    '转发-微信': ('xpath', "//a[@class='bds_weixin']"),
    '转发-QQ': ('xpath', "//a[@class='bds_qzone']"),
    '转发-微博': ('xpath', "//a[@class='bds_tsina']"),
    '相关服务': ('xpath', "//div[@id='service_enter_list_content']"),
    '相关推荐': ('xpath', "//div[@class='search-content']"),
    '登录': ('xpath', "//a[@class='login_comment'][1]"),
    '立即注册': ('xpath', "//a[@class='login_comment'][2]"),
    '全部评论': ('xpath', "//li[@class='answerDetail-desc clearfix']"),
    '头像': ('xpath', "//img[@class='userIcon']"),
    '姓名': ('xpath', "//div[contains(@class,'answerDetail')]/span[1]"),
    '等级': ('xpath', "//div[contains(@class,'answerDetail')]/span[2]"),
    '头衔': ('xpath', "//div[contains(@class,'answerDetail')]/span[3]"),
    '评论时间': ('xpath', "//div[contains(@class,'answerDetail')]/span[4]"),
    '评论内容': ('xpath', "//div[contains(@class,'comment-content')]"),
    '更多评论': ('xpath', "//a[@id='loadMore']"),
}


class DocDetailPage(SekormCommon):
    """资料详情页"""

    def check_doc_detail_layout(self):
        """检查资讯详情页模块"""
        title = self.element_text(Locator['资料标题'])
        time = self.element_text(Locator['发布时间'])
        self.move_to_element(Locator['PDF'])
        self.move_to_element(Locator['文件大小'])
        self.move_to_element(Locator['我要下载'])
        self.move_to_element(Locator['资料内容'])
        num = self.elements_num(Locator['资料信息'])
        # self.move_to_element(Locator['资料部分预览'])
        self.move_to_element(Locator['相关服务'])
        self.move_to_element(Locator['相关推荐'])
        return title, time, num

    def check_unlogin_bottom(self, elm):
        """检查未登录点击按钮"""
        self.js_click(Locator[elm])
        return UnLoginPage(self.driver)

    def check_doc_keyword(self, elm):
        """检查点击资料厂牌、型号、品类、应用"""
        from page_object.Sekorm.Search.SearchPage import SearchPage
        keyword = self.element_text(Locator[elm])
        self.is_click(Locator[elm])
        self.switch_window()
        return keyword, SearchPage(self.driver)

    def check_doc_like(self):
        """检查点赞按钮"""
        self.element_move_to_center(Locator['点赞'])
        text1 = self.get_attribute_value(Locator['点赞'], 'class')
        self.is_click(Locator['点赞'])
        text2 = self.get_attribute_value(Locator['点赞'], 'class')
        return text1, text2

    def check_doc_comment_button(self):
        """检查评论按钮"""
        self.element_move_to_center(Locator['评论'])
        display1 = self.get_position()
        self.is_click(Locator['评论'])
        display2 = self.get_position()
        return display1, display2

    def check_doc_comment(self):
        """检查评论"""
        self.move_to_element(Locator['头像'])
        self.move_to_element(Locator['姓名'])
        self.move_to_element(Locator['等级'])
        self.move_to_element(Locator['头衔'])
        self.move_to_element(Locator['评论时间'])
        self.move_to_element(Locator['评论内容'])
        num1 = self.elements_num(Locator['全部评论'])
        return num1

    def go_ChapterPage(self):
        """检查跳转章节详情页"""
        self.is_click(Locator['目录章节'])
        self.switch_window()
        return ChapterPage(self.driver)

    def check_pdf_preview(self):
        """检查PDF预览页"""
        self.is_click(Locator['预览'])
        sleep()
        self.switch_window()
        self.move_to_element(Locator['预览页PDF组件'])
        return self.element_text(Locator['预览页下载按钮'])
