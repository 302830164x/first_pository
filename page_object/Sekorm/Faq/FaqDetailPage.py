from page.basepage import BasePage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage

Locator = {
    '问答标题': ('xpath', "//h1[@id='queTitle']"),
    '问答创建时间': ('xpath', "//span[@class='servcie-top-block-time']"),
    '回答创建时间': ('xpath', "//dd[@class='answerDetail-subDesc']//a"),
    '写回答': ('xpath', "//a[@id='do_answer']"),
    '参与回答': ('xpath', "//a[@id='login_answer']"),
    '回答列表': ('xpath', "//div[@class='answer-list']"),
    '相关服务': ('xpath', "//div[@id='service_enter_list_content']"),
    '相关服务-展开': ('xpath', "//div[contains(@class,'service-brand-collapse')]"),
    '相关推荐': ('xpath', "//div[@class='search-content']"),
    '未登录提示': ('xpath', "//div[@class='opacity-cover-text']/p"),
    '发送到邮箱': ('xpath', "//li[@class='email_share cd-email']"),
    '点赞': ('xpath', "//ul[@class='last clearfix']//li[2]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect']"),
    '转发-微信': ('xpath', "//a[@class='bds_weixin']"),
    '转发-QQ': ('xpath', "//a[@class='bds_qzone']"),
    '转发-微博': ('xpath', "//a[@class='bds_tsina']"),
}


class FaqDetailPage(SekormCommon):
    """问答详情页"""

    def check_unlogin(self):
        """检查未登录状态"""
        self.move_to_element(Locator['问答标题'])
        text = self.element_text(Locator['未登录提示'])
        return text

    def check_layout(self):
        """检查页面布局"""
        title = self.element_text(Locator['问答标题'])
        time = self.element_text(Locator['问答创建时间'])
        self.element_move_to_center(Locator['写回答'])
        self.element_move_to_center(Locator['回答列表'])
        self.element_move_to_center(Locator['相关服务'])
        self.element_move_to_center(Locator['相关推荐'])
        return title, time

    def check_service_open(self):
        """检查相关服务展开和关闭"""
        close1 = self.get_attribute_value(Locator['相关服务-展开'], 'class')
        self.is_click(Locator['相关服务-展开'])
        open2 = self.get_attribute_value(Locator['相关服务-展开'], 'class')
        self.is_click(Locator['相关服务-展开'])
        close3 = self.get_attribute_value(Locator['相关服务-展开'], 'class')
        return close1, open2, close3

    def check_unlogin_answer_open(self):
        """检查未登录写回答展开和关闭"""
        answer_close = self.get_attribute_value(Locator['写回答'], 'class')
        self.is_click(Locator['写回答'])
        answer_open = self.get_attribute_value(Locator['写回答'], 'class')
        self.is_click(Locator['参与回答'])
        return UnLoginPage(self.driver), answer_close, answer_open

    def check_unlogin_bottom(self, elm):
        """检查未登录点击按钮"""
        self.move_to_element(Locator[elm])
        self.is_click(Locator[elm])
        return UnLoginPage(self.driver)

    def check_like(self):
        """检查点赞按钮"""
        self.element_move_to_center(Locator['点赞'])
        text1 = self.get_attribute_value(Locator['点赞'], 'class')
        self.is_click(Locator['点赞'])
        text2 = self.get_attribute_value(Locator['点赞'], 'class')
        return text1, text2

    def check_answer_detail(self):
        """点击回答时间，跳转问答详情页"""
        self.is_click(Locator['回答创建时间'])
        self.switch_window()
        self.element_move_to_center(Locator['问答标题'])
        self.element_move_to_center(Locator['相关推荐'])
        return self.driver.current_url
