import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站首页")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-检查登录、退出登录")
    def test_check_EnSekorm(self):
        self.en_sekorm.get_en_login().quit_login()
        assert_text = 'Sign in / Register'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('a', assert_text), assert_text)

    @allure.story("英文站-检查title、热门是否高亮")
    def test_go_EnSekormIndexPage(self):
        assert_text = 'Shopping Cart'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('a', assert_text), assert_text)
        assertUtils.assert_contains(self.en_sekorm.get_title(), 'Services Platform – Sekorm')
        assertUtils.assert_contains(self.en_sekorm.get_elm_attribute('英文站首页', 'class'), ('index', 'nav-active'))

    @allure.story("英文站-轮播图切换")
    def test_switch_banner(self):
        size1, size2, size3, size4 = self.en_sekorm.banner_change()
        assertUtils.assert_equals(size1, (600, 340))
        assertUtils.assert_equals(size2, (600, 340))
        assertUtils.assert_equals(size3, (600, 340))
        assertUtils.assert_equals(size4, (600, 340))

    @allure.story("英文站-轮播图点击")
    def test_click_banner(self):
        self.en_sekorm.click_banner().check_en_news_detail_layout()

    @allure.story("英文站-品牌墙点击")
    def test_click_brand(self):
        num, EnSearchPage = self.en_sekorm.click_brand()
        text = EnSearchPage.get_search_text()
        assertUtils.assert_equals(num, 2)
        assert text

    @allure.story("英文站-点击首页楼层")
    def test_click_index_showcase(self):
        self.en_sekorm.click_index_showcase().check_en_news_list()

    @allure.story("英文站-点击首页资讯")
    def test_click_index_news(self):
        self.en_sekorm.click_index_news().check_en_news_detail_layout()

    @allure.story("英文站-检查首页资讯图片")
    def test_check_index_news_img(self):
        size, EnNewsDetailPage = self.en_sekorm.check_index_news_img()
        EnNewsDetailPage.check_en_news_detail_layout()
        assertUtils.assert_equals(size, (180, 130))

    @allure.story("英文站-点击About Us")
    def test_click_about_us(self):
        self.en_sekorm.click_about_us()
        assert_text = 'Our strengths', 'Company Profile'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('p', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story("英文站-点击Contact Us")
    def test_click_contact_us(self):
        self.en_sekorm.click_contact_us()
        assert_text = 'Headquartered in Shenzhen', 'Company Profile'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('span', assert_text[0]), assert_text[0])

    @allure.story("英文站-点击Supplier Cooperation")
    def test_click_supplier_cooperation(self):
        text = self.en_sekorm.click_supplier_cooperation().check_en_cooperation_layout()
        assertUtils.assert_equals(text, 'Hardware Innovation')

    @allure.story("英文站-未登录-点击顶部")
    @pytest.mark.parametrize('elm', ['英文站购物车', '英文站我的订单', '登录'])
    def test_Unlogin_click_en_top(self, elm):
        text = self.en_sekorm.un_login_click_en_top(elm)
        assertUtils.assert_equals(text, 'Please choose email')

    @allure.story("英文站-未登录-点击Chinese,跳转中文站")
    def test_click_Chinese(self):
        self.en_sekorm.click_Chinese()
        assert_text = '热门'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('span', assert_text), assert_text)
