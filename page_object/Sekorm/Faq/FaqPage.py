from page_object.Sekorm.Faq.FaqDetailPage import FaqDetailPage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.Service.AskServicePage import AskServicePage
from utils.times import sleep

Locator = {
    '我要提问-顶部': ('xpath', "//a[@class='js-ask sekorm-user-ask question-ask color-white pull-left']"),
    '顶部提问文案': ('xpath', "//em[@class='ml10 pull-left']"),
    '问答列表': ('xpath', "//div[@class='faq-mul-list-qustion']"),
    '相关服务': ('xpath', "//div[@class='search-service-module clearfix']"),
    '等你来答': ('xpath', "//div[@class='tit-list-item']"),
    '问答标题': ('xpath', "//div[@class='faq-mul-list-qustion']//h2"),
    '问答描述': ('xpath', "//div[@class='faq-mul-list-qustion']//p"),
    '问答发布时间': ('xpath', "//div[@class='ecnew-list-info clearfix']//span"),
    '问答logo图': ('xpath', "//div[@class='faq-channel']//img"),
    '第10条问答': ('xpath', "(//div[@class='faq-mul-list-qustion']//h2//a)[10]"),
    '第20条问答': ('xpath', "(//div[@class='faq-mul-list-qustion']//h2//a)[20]"),
    '第10条等你来答': ('xpath', "(//div[@class='tit-list-item']//h2//a)[10]"),
    '第20条等你来答': ('xpath', "(//div[@class='tit-list-item']//h2//a)[20]"),
}


class FaqPage(SekormCommon):
    """技术问答"""

    def check_top_ask(self):
        """检查顶部技术问答按钮"""
        text = self.element_text(Locator['顶部提问文案'])
        self.is_click(Locator['我要提问-顶部'])
        self.switch_window()
        sleep()
        return text, AskServicePage(self.driver)

    def check_list_num(self):
        """检查列表问答数据"""
        num1 = self.elements_num(Locator['问答列表'])
        num2 = self.elements_num(Locator['等你来答'])
        # num3 = self.elements_num(Locator['相关服务'])
        return num1, num2

    def check_list(self):
        """检查列表问答内容格式"""
        self.move_to_element(Locator['问答标题'])
        self.move_to_element(Locator['问答描述'])
        self.scroll_to_bottom()
        size = self.img_show(Locator['问答logo图'])
        text = self.element_text(Locator['问答发布时间'])
        return size, text

    def click_ask_list(self, elm):
        """点击列表问答内容"""
        self.move_to_element(Locator[elm])
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return FaqDetailPage(self.driver)

