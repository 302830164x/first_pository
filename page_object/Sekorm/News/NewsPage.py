from common.readelement import Element
from page_object.Sekorm.News.NewsDetailPage import NewsDetailPage
from page_object.Sekorm.SekormCommon import SekormCommon
from utils.times import sleep

sekorm = Element('SekormElement')
Locator = {
    '资讯列表': ('xpath', "//div[@class='multiple-search']/div[contains(@class,'clearfix')]"),
    '资讯缩略图': ('xpath', "//div[@class='multiple-search']//div[1]//div[1]//a[1]//img[1]"),
    '资讯标题': ('xpath', "//div[@class='search-item-main']//h2"),
    '资讯简介': ('xpath', "//div[@class='search-item-main']//p"),
    '资讯类型': ('xpath', "//div[@class='search-item-main']//p[@class='search-item-info search-weak']/span[1]"),
    '资讯发布时间': ('xpath', "//div[@class='search-item-main']//p[@class='search-item-info search-weak']/span[2]"),
}


class NewsPage(SekormCommon):
    """新技术频道页"""

    def check_news_list(self):
        """检查列表资讯格式和点击"""
        self.move_to_element(Locator['资讯缩略图'])
        self.move_to_element(Locator['资讯标题'])
        self.move_to_element(Locator['资讯简介'])
        self.move_to_element(Locator['资讯类型'])
        self.move_to_element(Locator['资讯发布时间'])
        self.is_click(Locator['资讯缩略图'])
        self.switch_window()
        sleep()
        return NewsDetailPage(self.driver)

    def check_news_list_num(self):
        """获取列表初始状态资讯条数、加载一次后资讯条数"""
        num1 = self.elements_num(Locator['资讯列表'])
        self.scroll_to_bottom()
        sleep(5)
        num2 = self.elements_num(Locator['资讯列表'])
        return num1, num2
