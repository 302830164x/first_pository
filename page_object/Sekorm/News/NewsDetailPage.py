from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.times import sleep

Locator = {
    '资讯标题': ('xpath', "//span[@class='item-title5 ']"),
    '发布时间': ('xpath', "//span[@class='servcie-top-block-time']//span[1]"),
    '来源': ('xpath', "//span[@class='servcie-top-block-time']//span[2]"),
    '资讯内容': ('xpath', "//div[@class='cd-content']"),
    '视频iframe': ('xpath', "//div[@class='cd-iframe-video']//iframe"),
    '视频': ('xpath', "//div[@id='video-cover-layer']"),
    '视频播放': ('xpath', "//div[@class='outter']"),
    '视频时间': ('xpath', "//span[@class='current-time']"),
    '发送到邮箱': ('xpath', "//li[@class='email_share cd-email']"),
    '点赞': ('xpath', "//ul[@class='last clearfix']//li[2]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect']"),
    '评论': ('xpath', "//li[@class='cd-comment']"),
    '转发-微信': ('xpath', "//a[@class='bds_weixin']"),
    '转发-QQ': ('xpath', "//a[@class='bds_qzone']"),
    '转发-微博': ('xpath', "//a[@class='bds_tsina']"),
    '相关服务': ('xpath', "//div[@id='service_enter_list_content']"),
    '相关推荐': ('xpath', "//div[@class='search-content']"),
    '关键字': ('xpath', "//div[@class='cp1040']//a"),
    '登录': ('xpath', "//a[@class='login_comment'][1]"),
    '立即注册': ('xpath', "//a[@class='login_comment'][2]"),
    '全部评论': ('xpath', "//ul[@class='comment-list']"),
    '评论列表': ('xpath', "//ul[@class='comment-list']/li"),
    '头像': ('xpath', "//img[@class='userIcon']"),
    '姓名': ('xpath', "//div[contains(@class,'answerDetail')]/span[1]"),
    '等级': ('xpath', "//div[contains(@class,'answerDetail')]/span[2]"),
    '头衔': ('xpath', "//div[contains(@class,'answerDetail')]/span[3]"),
    '评论时间': ('xpath', "//div[contains(@class,'answerDetail')]/span[4]"),
    '评论内容': ('xpath', "//div[contains(@class,'comment-content')]"),
    '更多评论': ('xpath', "//a[@id='loadMore']"),
}


class NewsDetailPage(SekormCommon):
    """资讯详情页"""

    def check_news_detail_layout(self):
        """检查资讯详情页模块"""
        title = self.element_text(Locator['资讯标题'])
        time = self.element_text(Locator['发布时间'])
        self.move_to_element(Locator['来源'])
        self.move_to_element(Locator['资讯内容'])
        self.move_to_element(Locator['相关服务'])
        self.move_to_element(Locator['相关推荐'])
        self.move_to_element(Locator['关键字'])
        self.move_to_element(Locator['全部评论'])
        return title, time

    def check_unlogin_bottom(self, elm):
        """检查未登录点击按钮"""
        self.is_click(Locator[elm])
        return UnLoginPage(self.driver)

    def check_like(self):
        """检查点赞按钮"""
        self.element_move_to_center(Locator['点赞'])
        text1 = self.get_attribute_value(Locator['点赞'], 'class')
        self.is_click(Locator['点赞'])
        text2 = self.get_attribute_value(Locator['点赞'], 'class')
        return text1, text2

    def check_comment_button(self):
        """检查评论按钮"""
        self.element_move_to_center(Locator['评论'])
        display1 = self.get_position()
        self.is_click(Locator['评论'])
        display2 = self.get_position()
        return display1, display2

    def check_keyword(self):
        """检查关键词"""
        from page_object.Sekorm.Search.SearchPage import SearchPage
        self.element_move_to_center(Locator['关键字'])
        keyword = self.element_text(Locator['关键字'])
        self.is_click(Locator['关键字'])
        self.switch_window()
        return keyword, SearchPage(self.driver)

    def check_comment(self):
        """检查评论"""
        num1 = self.elements_num(Locator['评论列表'])
        self.move_to_element(Locator['头像'])
        self.move_to_element(Locator['姓名'])
        self.move_to_element(Locator['等级'])
        self.move_to_element(Locator['头衔'])
        self.move_to_element(Locator['评论时间'])
        self.move_to_element(Locator['评论内容'])
        self.is_click(Locator['更多评论'])
        num2 = self.elements_num(Locator['评论列表'])
        return num1, num2

    def check_video(self):
        """检查视频"""
        self.switch_to_iframe(Locator['视频iframe'])
        self.is_click(Locator['视频播放'])
        play = self.get_attribute_value(Locator['视频'], 'style')
        sleep(10)
        close = self.get_attribute_value(Locator['视频'], 'style')
        stop_time = self.element_text(Locator['视频时间'])
        self.switch_to_content()
        return play, close, stop_time

    def close_login(self):
        """关闭登录弹窗阻拦"""
        sleep()
        self.go_to_element(Locator['相关推荐'])
        sleep()
        page = UnLoginPage(self.driver)
        page.close_login()
