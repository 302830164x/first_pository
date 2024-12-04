import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("现货市场")
class Test_Mall:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story("现货市场-检查门楣是否高亮、文案")
    def test_go_MallPage(self):
        text = self.sekorm.go_MallPage().get_tips_text()
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('现货市场', 'class'), 'index nav-active')
        assertUtils.assert_contains(text, '''1. 市场所售物料由第三方企业销售并提供售后服务。''')

    @allure.story("现货市场-检查图片是否加载成功")
    @pytest.mark.parametrize('elm, size', [('轮播图', (2400, 200)), ('授权代理品牌', (240, 144)), ('生态合作伙伴', (240, 120))])
    def test_MallPage_check_img(self, elm, size):
        img_size = self.sekorm.go_MallPage().check_img(elm)
        assertUtils.assert_equals(img_size, size)

    @allure.story("现货市场-点击型号名称、技术资料")
    @pytest.mark.parametrize('elm', ['ON名称', '技术资料'])
    def test_MallPage_go_OnPage(self, elm):
        text = self.sekorm.go_MallPage().go_OnPage(elm).check_layout()
        assertUtils.assert_equals(text, '规格参数')

    @allure.story("现货市场-点击厂牌名称")
    def test_MallPage_go_brand_search(self):
        url = self.sekorm.go_MallPage().go_brand_search().driver.current_url
        assertUtils.assert_contains(url, 'https://www.sekorm.com/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("现货市场-点击授权代理品牌、生态合作伙伴")
    @pytest.mark.parametrize('elm', ['授权代理品牌', '生态合作伙伴'])
    def test_MallPage_go_brand_search(self, elm):
        url = self.sekorm.go_MallPage().click_img(elm).driver.current_url
        assertUtils.assert_contains(url, 'https://www.sekorm.com/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("现货市场-检查描述内容")
    def test_MallPage_check_description(self):
        text = self.sekorm.go_MallPage().check_description()
        assertUtils.assert_contains(text, '最小包装量：')

    @allure.story("现货市场-检查供应商/品质保证")
    def test_MallPage_check_supplier(self):
        num = self.sekorm.go_MallPage().check_mall_supplier()
        assertUtils.assert_greater_equal(num, 20)

    @allure.story("现货市场-检查单价（含增值税）")
    def test_MallPage_check_information(self):
        text = self.sekorm.go_MallPage().check_ON_information()
        assertUtils.assert_contains(text, ('约', '工作日'))

    @allure.story("现货市场-未登录点击下单购买")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_unlogin_click_MallPage_service(self, elm, text):
        text1, self.UnLoginPage = self.sekorm.go_MallPage().unlogin_click_service(elm)
        text2 = self.UnLoginPage.close_login()
        assertUtils.assert_contains(text1, text)
        assertUtils.assert_equals(text2, '所属国家/地区')

    @allure.story("现货市场-翻页检查")
    def test_next_MallPage(self):
        text = self.sekorm.go_MallPage().next_page(next_action=False)
        assertUtils.assert_equals(text, 'active')

    @allure.story("现货市场-翻页后点击型号名称、技术资料")
    @pytest.mark.parametrize('elm', ['ON名称', '技术资料'])
    def test_MallPage_next_go_OnPage(self, elm):
        text = self.sekorm.go_MallPage().next_page(next_action=True).go_OnPage(elm).check_layout()
        assertUtils.assert_equals(text, '规格参数')

    @allure.story("现货市场-翻页后点击厂牌名称")
    def test_MallPage_next_go_brand_search(self):
        url = self.sekorm.go_MallPage().next_page(next_action=True).go_brand_search().driver.current_url
        assertUtils.assert_contains(url, 'https://www.sekorm.com/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("现货市场-翻页后点击授权代理品牌、生态合作伙伴")
    @pytest.mark.parametrize('elm', ['授权代理品牌', '生态合作伙伴'])
    def test_MallPage_next_go_brand_search(self, elm):
        url = self.sekorm.go_MallPage().next_page(next_action=True).click_img(elm).driver.current_url
        assertUtils.assert_contains(url, 'https://www.sekorm.com/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("现货市场-翻页后检查描述内容")
    def test_MallPage_next_check_description(self):
        text = self.sekorm.go_MallPage().next_page(next_action=True).check_description()
        assertUtils.assert_contains(text, '最小包装量：')

    @allure.story("现货市场-翻页后检查供应商/品质保证")
    def test_MallPage_next_check_supplier(self):
        num = self.sekorm.go_MallPage().next_page(next_action=True).check_mall_supplier()
        assertUtils.assert_greater_equal(num, 20)

    @allure.story("现货市场-翻页后检查单价（含增值税）")
    def test_MallPage_next_check_information(self):
        text = self.sekorm.go_MallPage().next_page(next_action=True).check_ON_information()
        assertUtils.assert_contains(text, ('约', '工作日'))

    @allure.story("现货市场-翻页后未登录点击下单购买")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_unlogin_next_click_MallPage_service(self, elm, text):
        text1, self.UnLoginPage = self.sekorm.go_MallPage().next_page(next_action=True).unlogin_click_service(elm)
        text2 = self.UnLoginPage.close_login()
        assertUtils.assert_contains(text1, (elm, text))
        assertUtils.assert_equals(text2, '所属国家/地区')
