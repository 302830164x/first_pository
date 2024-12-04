import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站资料")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-资料详情页-检查布局")
    def test_check_en_doc_detail_layout(self):
        self.en_sekorm.go_EnDocDetailPage_by_id().check_en_doc_detail_layout()

    @allure.story("英文站-未登录-资料详情页")
    @pytest.mark.parametrize('elm', ['文件名称', '预览按钮', '下载按钮', '底部下载按钮', '收藏'])
    def test_unlogin_click_en_doc(self, elm):
        text = self.en_sekorm.go_EnDocDetailPage_by_id().unlogin_click_en_doc(elm)
        assertUtils.assert_equals(text, 'Please choose email')

    @allure.story("英文站-资料详情页-点击右侧厂牌墙")
    def test_click_doc_detail_right_brand(self):
        EnSearchPage = self.en_sekorm.go_EnDocDetailPage_by_id().click_doc_detail_right_brand()
        text = EnSearchPage.get_search_text()
        assertUtils.assert_equals(text, 'ROHM')

    @allure.story("英文站-资料详情页-点击推荐资讯")
    def test_click_en_news_recommend(self):
        self.en_sekorm.go_EnDocDetailPage_by_id().click_en_news_recommend()
        assert_text = 'PublishTime：'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("英文站-资料详情页-点击推荐资料")
    def test_click_en_doc_recommend(self):
        self.en_sekorm.go_EnDocDetailPage_by_id().click_en_doc_recommend()
        assert_text = 'PublishTime：'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("英文站-资料详情页-相关推荐-查看更多")
    def test_click_doc_detail_read_more(self):
        EnSearchPage = self.en_sekorm.go_EnDocDetailPage_by_id().click_doc_detail_read_more()
        text = EnSearchPage.get_search_text()
        assert text

    @allure.story("英文站-资料详情页-检查点赞按钮")
    def test_check_doc_like(self):
        text1, text2 = self.en_sekorm.go_EnDocDetailPage_by_id().check_en_doc_like()
        assertUtils.assert_contains(text1, 'unpraise')
        assertUtils.assert_contains(text2, 'praised')

    @allure.story("英文站-资料详情页-登录后-点击预览")
    def test_login_click_preview(self):
        self.en_sekorm.get_en_login().go_EnDocDetailPage_by_id().login_click_preview()
