import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站资讯")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-门楣高亮")
    def test_go_EnNewsPage(self):
        self.en_sekorm.go_EnNewsPage()
        assert_text = 'Shopping Cart'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('a', assert_text), assert_text)
        assertUtils.assert_contains(self.en_sekorm.get_elm_attribute('英文站新产品页', 'class'), ('new-nav', 'nav-active'))

    @allure.story("英文站-检查列表资讯显示格式、点击")
    def test_check_en_news_list(self):
        self.en_sekorm.go_EnNewsPage().check_en_news_list()

    @allure.story("英文站-检查列表条数")
    def test_check_en_news_list_num(self):
        num1, num2, num3 = self.en_sekorm.go_EnNewsPage().check_news_list_num()
        assertUtils.assert_equals(num1, 50)
        assertUtils.assert_equals(num2, 70)
        assertUtils.assert_greater_equal(num3, 90)

    @allure.story("英文站-点击右侧厂牌墙")
    def test_click_news_right_brand(self):
        EnSearchPage = self.en_sekorm.go_EnNewsPage().click_news_right_brand()
        text = EnSearchPage.get_search_text()
        assertUtils.assert_equals(text, 'ROHM')

    @allure.story("英文站-资讯详情页-检查布局")
    def test_check_en_news_detail_layout(self):
        self.en_sekorm.go_EnNewsDetailPage_by_id().check_en_news_detail_layout()

    @allure.story("英文站-资讯详情页-点击右侧厂牌墙")
    def test_click_news_detail_right_brand(self):
        EnSearchPage = self.en_sekorm.go_EnNewsDetailPage_by_id().click_news_detail_right_brand()
        text = EnSearchPage.get_search_text()
        assertUtils.assert_equals(text, 'ROHM')

    @allure.story("英文站-资讯详情页-点击推荐资讯")
    def test_click_en_news_recommend(self):
        self.en_sekorm.go_EnNewsDetailPage_by_id().click_en_news_recommend()
        assert_text = 'PublishTime：'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("英文站-资讯详情页-点击推荐资料")
    def test_click_en_doc_recommend(self):
        self.en_sekorm.go_EnNewsDetailPage_by_id().click_en_doc_recommend()
        assert_text = 'PublishTime：'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("英文站-资讯详情页-点击关键词")
    def test_click_news_detail_keyword(self):
        EnSearchPage = self.en_sekorm.go_EnNewsDetailPage_by_id().click_news_detail_keyword()
        text = EnSearchPage.get_search_text()
        assert text

    @allure.story("英文站-资讯详情页-检查点赞按钮")
    def test_check_en_news_like(self):
        text1, text2 = self.en_sekorm.go_EnNewsDetailPage_by_id().check_en_news_like()
        assertUtils.assert_contains(text1, 'unpraise')
        assertUtils.assert_contains(text2, 'praised')

    @allure.story("英文站-资讯详情页-相关推荐-查看更多")
    def test_click_news_detail_read_more(self):
        EnSearchPage = self.en_sekorm.go_EnNewsDetailPage_by_id().click_news_detail_read_more()
        text = EnSearchPage.get_search_text()
        assert text

    @allure.story("英文站-资讯详情页-检查视频")
    def test_check_en_video(self):
        play, close, stop_time = self.en_sekorm.go_EnNewsDetailPage_by_id().check_en_video()
        assertUtils.assert_contains(play, 'display: none')
        assertUtils.assert_contains(close, 'display: block')
        assertUtils.assert_equals('00:10', stop_time)

