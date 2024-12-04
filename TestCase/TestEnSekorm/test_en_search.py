import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站搜索")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-搜索结果页-检查布局")
    def test_check_en_search_layout(self):
        self.en_sekorm.go_EnSearchPage('MCU').check_en_search_layout()

    @allure.story("英文站-搜索结果页-结果条数")
    def test_check_en_search_num(self):
        num = self.en_sekorm.go_EnSearchPage('MCU').check_en_search_num()
        assertUtils.assert_greater(num, 50)

    @allure.story("英文站-搜索结果页-点击文章标题")
    def test_click_search_title(self):
        self.en_sekorm.go_EnSearchPage('MCU').click_en_search_title().check_en_doc_detail_layout()

    @allure.story("英文站-搜索结果页-点击品牌墙")
    def test_click_search_right_brand(self):
        text = self.en_sekorm.go_EnSearchPage('MCU').click_en_search_right_brand().get_search_text()
        assertUtils.assert_equals(text, 'ROHM')

    @allure.story("英文站-搜索结果页-检查商城模块信息")
    def test_check_en_search_on(self):
        self.en_sekorm.go_EnSearchPage('MCU').check_en_search_on()

    @allure.story("英文站-搜索结果页-点击商城模块")
    @pytest.mark.parametrize('elm', ['商城模块-型号', '商城模块-厂牌', '商城模块-Buy', '商城模块-RFQ', '商城模块-More'])
    def test_click_en_search_on(self, elm):
        text = self.en_sekorm.go_EnSearchPage('MCU').click_en_search_on(elm).get_search_text()
        assertUtils.assert_equals(text, 'mcu')

    @allure.story("英文站-搜索结果页-翻页")
    def test_check_en_search_next_page(self):
        text = self.en_sekorm.go_EnSearchPage('MCU').next_page(next_action=False)
        assertUtils.assert_equals(text, 'active')

    @allure.story("英文站-搜索结果页-翻页点击文章标题")
    def test_next_page_click_search_title(self):
        self.en_sekorm.go_EnSearchPage('MCU').next_page(True).click_en_search_title().check_en_doc_detail_layout()

    @allure.story("英文站-商城垂直搜索结果页-检查布局")
    def test_check_en_supply_search_layout(self):
        self.en_sekorm.go_EnSupplySearchPage('MCU').check_en_supply_search_layout()

    @allure.story("英文站-商城垂直搜索结果页-检查每页ON数量")
    def test_check_en_supply_search_num(self):
        num = self.en_sekorm.go_EnSupplySearchPage('MCU').check_en_supply_search_num()
        assertUtils.assert_equals(num, 50)

    @allure.story("英文站-商城垂直搜索结果页-点击品牌墙")
    def test_click_supply_search_right_brand(self):
        text = self.en_sekorm.go_EnSupplySearchPage('MCU').click_en_supply_search_right_brand().get_search_text()
        assertUtils.assert_equals(text, 'ROHM')

    @allure.story("英文站-商城垂直搜索结果页-点击型号")
    @pytest.mark.parametrize('elm', ['型号', 'Documents'])
    def test_click_en_supply_search_on(self, elm):
        text = self.en_sekorm.go_EnSupplySearchPage('MCU').click_en_supply_search_on(elm).check_en_on_layout()
        assertUtils.assert_contains(text, 'Sekorm is an authorized distributor')

    @allure.story("英文站-商城垂直搜索结果页-点击品牌墙")
    def test_click_en_supply_search_on_brand(self):
        text = self.en_sekorm.go_EnSupplySearchPage('MCU').click_en_supply_search_on_brand().get_search_text()
        assert text, '搜索词不为空'

    @allure.story("英文站-商城垂直搜索结果页-点击RFQ")
    def test_check_en_supply_search_RFQ(self):
        text, EnServiceCommPage = self.en_sekorm.go_EnSupplySearchPage('MCU').check_en_supply_search_RFQ()
        text1, text2 = EnServiceCommPage.check_RFQ_layout()
        assertUtils.assert_contains(text, 'For the best price and delivery time')
        assertUtils.assert_equals(text1, 'RFQ')
        assertUtils.assert_equals(text2, 'Please Fill In Company Name')

    @allure.story("英文站-未登录-商城垂直搜索结果页-点击Buy")
    def test_unlogin_click_en_on(self):
        text = self.en_sekorm.go_EnSupplySearchPage('MCU').unlogin_click_en_on_buy()
        assertUtils.assert_equals(text, 'Please choose email')

    @allure.story("英文站-商城垂直搜索结果页-翻页")
    def test_check_en_supply_earch_next_page(self):
        text = self.en_sekorm.go_EnSupplySearchPage('MCU').next_page(next_action=False)
        assertUtils.assert_equals(text, 'active')

    @allure.story("英文站-商城垂直搜索结果页-获取条数")
    def test_next_page_check_en_supply_search_num(self):
        num = self.en_sekorm.go_EnSupplySearchPage('MCU').next_page(True).check_en_supply_search_num()
        assertUtils.assert_equals(num, 50)

    @allure.story("英文站-已登录-商城垂直搜索结果页-点击Buy")
    def test_login_click_en_on(self):
        text, EnUserListPage = self.en_sekorm.get_en_login().go_EnSupplySearchPage('INS5699S'). \
            login_click_en_on_buy().check_join_cart()
        text = EnUserListPage.click_en_check_out().click_en_order_submit()
        assertUtils.assert_equals(text, 'Please enter company name.')
