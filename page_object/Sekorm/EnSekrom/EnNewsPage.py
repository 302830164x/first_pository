from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnNewsDetailPage import EnNewsDetailPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage
from utils.times import sleep

Locator = {
    '资讯标题': ('xpath', "//div[contains(@class,'mul-list')]/h2"),
    '资讯简介': ('xpath', "//div[contains(@class,'mul-list')]/p"),
    '资讯类型': ('xpath', "//div[contains(@class,'mul-list')]/div/span[1]"),
    '资讯发布时间': ('xpath', "//div[contains(@class,'mul-list')]/div/span[2]"),
    '品牌墙': ('xpath', "//div[@class='list-cont-right']//a"),
}


class EnNewsPage(BasePage):
    """英文站新产品页"""

    def check_en_news_list(self):
        """检查列表资讯格式和点击"""
        self.move_to_element(Locator['资讯标题'])
        self.move_to_element(Locator['资讯简介'])
        self.move_to_element(Locator['资讯类型'])
        self.move_to_element(Locator['资讯发布时间'])
        self.is_click(Locator['资讯标题'])
        self.switch_window()
        return EnNewsDetailPage(self.driver)

    def check_news_list_num(self):
        """获取列表初始状态资讯条数、加载一次后资讯条数"""
        num1 = self.elements_num(Locator['资讯标题'])
        self.scroll_to_bottom()
        sleep(2)
        num2 = self.elements_num(Locator['资讯标题'])
        self.scroll_to_top()
        sleep(2)
        self.scroll_to_bottom()
        sleep(2)
        num3 = self.elements_num(Locator['资讯标题'])
        return num1, num2, num3

    def click_news_right_brand(self):
        """点击首页品牌墙"""
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return EnSearchPage(self.driver)
