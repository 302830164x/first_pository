from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage
from utils.times import sleep

Locator = {
    '资讯标题': ('xpath', "//span[@class='item-title5 ']"),
    '发布时间': ('xpath', "//div[@class='sub-time']//span[1]"),
    '来源': ('xpath', "//span[@class='smart-font-shuxian']"),
    '资讯内容': ('xpath', "//div[@class='cd-content']"),
    '点赞': ('xpath', "//div[@class='last-content']//li[1]"),
    '收藏': ('xpath', "//li[@class='cd-collect cd-uncollect']"),
    '相关推荐': ('xpath', "//div[@class='mt15']"),
    '相关推荐-资料': ('xpath', "//div[@id='relatedRecom']//div[@class='module-tit-list']//a"),
    '相关推荐-资讯': ('xpath', "//div[@class='cd-left']//div[2]//div[2]//a"),
    '相关推荐-查看更多': ('xpath', "//div[@id='relatedRecom']//a[@class='read-more'][normalize-space()='More>']"),
    '关键字': ('xpath', "//div[@class='cd-tag-wrap pull-left']/a"),
    '品牌墙': ('xpath', "//div[@id='content']//a[1]//img[1]"),
    '视频iframe': ('xpath', "//div[@class='cd-iframe-video']//iframe"),
    '视频': ('xpath', "//div[@id='video-cover-layer']"),
    '视频播放': ('xpath', "//div[@class='outter']"),
    '视频时间': ('xpath', "//span[@class='current-time']"),
}


class EnNewsDetailPage(BasePage):
    """英文站资讯详情页"""

    def check_en_news_detail_layout(self):
        """检查资讯详情页模块"""
        self.move_to_element(Locator['资讯标题'])
        self.move_to_element(Locator['发布时间'])
        self.move_to_element(Locator['来源'])
        self.move_to_element(Locator['资讯内容'])
        self.move_to_element(Locator['点赞'])
        self.move_to_element(Locator['收藏'])
        self.move_to_element(Locator['相关推荐'])
        self.move_to_element(Locator['关键字'])
        self.move_to_element(Locator['品牌墙'])

    def click_news_detail_right_brand(self):
        """点击右侧品牌墙"""
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_news_detail_keyword(self):
        """点击关键字"""
        self.is_click(Locator['关键字'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_en_news_recommend(self):
        """点击资讯推荐"""
        self.is_click(Locator['相关推荐-资讯'])
        self.switch_window()
        return EnNewsDetailPage(self.driver)

    def click_en_doc_recommend(self):
        """点击资讯推荐"""
        from page_object.Sekorm.EnSekrom.EnDocDetailPage import EnDocDetailPage
        self.is_click(Locator['相关推荐-资料'])
        self.switch_window()
        return EnDocDetailPage(self.driver)

    def click_news_detail_read_more(self):
        """点击相关推荐-查看更多"""
        self.is_click(Locator['相关推荐-查看更多'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def check_en_news_like(self):
        """检查点赞按钮"""
        self.element_move_to_center(Locator['点赞'])
        text1 = self.get_attribute_value(Locator['点赞'], 'class')
        self.is_click(Locator['点赞'])
        text2 = self.get_attribute_value(Locator['点赞'], 'class')
        return text1, text2

    def check_en_video(self):
        """检查视频"""
        self.switch_to_iframe(Locator['视频iframe'])
        self.is_click(Locator['视频播放'])
        play = self.get_attribute_value(Locator['视频'], 'style')
        sleep(15)
        close = self.get_attribute_value(Locator['视频'], 'style')
        stop_time = self.element_text(Locator['视频时间'])
        self.switch_to_content()
        return play, close, stop_time
