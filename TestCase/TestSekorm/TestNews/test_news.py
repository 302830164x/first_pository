import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("新技术")
class Test_News:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story("进入新技术,检查门楣是否高亮")
    def test_click_news_highlight(self):
        self.sekorm.go_NewsPage()
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('新技术', 'class'), 'index nav-active')

    @allure.story("新技术-检查列表资讯显示格式、点击")
    def test_check_news_list(self):
        self.sekorm.go_NewsPage().check_news_list()
        assert_text = '时间：', '来源：'
        for text in assert_text:
            assertUtils.assert_equals(self.sekorm.get_assert_text('label', text), text)

    @allure.story("新技术-检查列表条数")
    def test_check_news_list_num(self):
        num1, num2 = self.sekorm.go_NewsPage().check_news_list_num()
        assertUtils.assert_greater_equal(num1, 12)
        assertUtils.assert_greater_equal(num2, 12)

    @allure.story("新技术-检查左侧广告")
    @pytest.mark.parametrize('elm', ['左侧广告1', '左侧广告2'])
    def test_click_advertising(self, elm):
        url = self.sekorm.go_NewsPage().check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webLeft', 'adPack=webNews', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("新技术-检查右侧LOGO墙")
    def test_check_news_logo(self):
        BrandSearchPage = self.sekorm.go_NewsPage().check_logo()
        text1 = BrandSearchPage.get_search_text()
        assertUtils.assert_equals(text1, 'ROHM')

    # @allure.story("新技术-点击我要提问")
    # def test_check_news_ask(self):
    #     text, AskServicePage = self.sekorm.go_NewsPage().check_ask()
    #     AskServicePage.get_login().check_AskServicePage()
    #     assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
    #     assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
    #     AskServicePage.quit_login()
