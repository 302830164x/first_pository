import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站商城")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-商城门楣高亮")
    def test_go_EnSupplyPage(self):
        self.en_sekorm.go_EnSupplyPage()
        assert_text = 'Shopping Cart'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('a', assert_text), assert_text)
        assertUtils.assert_contains(self.en_sekorm.get_elm_attribute('英文站商城页', 'class'), ('new-nav', 'nav-active'))

    @allure.story("英文站-商城页-检查布局")
    def test_check_en_supply_layout(self):
        text = self.en_sekorm.go_EnSupplyPage().check_en_supply_layout()
        assertUtils.assert_contains(text, 'Sekorm is an authorized distributor')

    @allure.story("英文站-商城页-检查图片显示")
    def test_check_en_supply_img(self):
        size1, size2 = self.en_sekorm.go_EnSupplyPage().check_en_supply_img()
        assertUtils.assert_equals(size1, (240, 144))
        assertUtils.assert_equals(size2, (240, 120))

    @allure.story("英文站-商城页-点击ON型号")
    @pytest.mark.parametrize('elm', ['型号', 'Documents'])
    def test_click_en_supply_on(self, elm):
        text = self.en_sekorm.go_EnSupplyPage().click_en_supply_on(elm).check_en_on_layout()
        assertUtils.assert_contains(text, 'Sekorm is an authorized distributor')

    @allure.story("英文站-商城页-点击ON厂牌、合作厂牌")
    @pytest.mark.parametrize('elm', ['厂牌', '授权品牌', '生态伙伴'])
    def test_click_en_supply_brand(self, elm):
        text = self.en_sekorm.go_EnSupplyPage().click_en_supply_brand(elm).get_search_text()
        assert text, '搜索词不为空'

    @allure.story("英文站-商城页-点击RFQ")
    def test_check_en_supply_RFQ(self):
        text, EnServiceCommPage = self.en_sekorm.go_EnSupplyPage().next_page(True).next_page(True).next_page(True).check_en_supply_RFQ()
        text1, text2 = EnServiceCommPage.check_RFQ_layout()
        assertUtils.assert_contains(text, 'For the best price and delivery time')
        assertUtils.assert_equals(text1, 'RFQ')
        assertUtils.assert_equals(text2, 'Please Fill In Company Name')

    @allure.story("英文站-商城页-未登录点击Buy")
    def test_unlogin_click_en_supply_buy(self):
        text = self.en_sekorm.go_EnSupplyPage().next_page(True).next_page(True).next_page(True).unlogin_click_en_supply_buy()
        assertUtils.assert_equals(text, 'Please choose email')

    @allure.story("英文站-商城页-翻页")
    def test_next_page_en_supply(self):
        text = self.en_sekorm.go_EnSupplyPage().next_page(False)
        assertUtils.assert_equals(text, 'active')

    @allure.story("英文站-商城页-翻页-点击ON型号")
    @pytest.mark.parametrize('elm', ['型号', 'Documents'])
    def test_next_page_click_en_supply_on(self, elm):
        text = self.en_sekorm.go_EnSupplyPage().next_page(True).click_en_supply_on(elm).check_en_on_layout()
        assertUtils.assert_contains(text, 'Sekorm is an authorized distributor')

    @allure.story("英文站-ON详情页-检查布局")
    def test_check_en_on_layout(self):
        text = self.en_sekorm.go_EnOnPage_by_id().check_en_on_layout()
        assertUtils.assert_contains(text, 'Sekorm is an authorized distributor')

    @allure.story("英文站-ON详情页-检查ON信息")
    def test_check_en_on_info(self):
        text = self.en_sekorm.go_EnOnPage_by_id().check_en_on_info()
        assertUtils.assert_contains(text, 'TS32F401CBU7')

    @allure.story("英文站-未登录-ON详情页点击按钮")
    @pytest.mark.parametrize('elm', ['发送到邮箱', 'Buy', '预览按钮', '下载按钮'])
    def test_unlogin_click_en_on(self, elm):
        text = self.en_sekorm.go_EnOnPage_by_id().unlogin_click_en_on(elm)
        assertUtils.assert_equals(text, 'Please choose email')

    @allure.story("英文站-未登录-ON详情页点击RFQ")
    def test_check_on_RFQ(self):
        text, EnServiceCommPage = self.en_sekorm.go_EnOnPage_by_id().check_on_RFQ()
        text1, text2 = EnServiceCommPage.check_RFQ_layout()
        assertUtils.assert_contains(text, 'For the best price and delivery time')
        assertUtils.assert_equals(text1, 'RFQ')
        assertUtils.assert_equals(text2, 'Please Fill In Company Name')

    @allure.story("英文站-已登录-ON详情页点击分享")
    def test_check_on_Share(self):
        text1, text2 = self.en_sekorm.get_en_login().go_EnOnPage_by_id().login_click_Share()
        assertUtils.assert_equals(text1, 'Send to email')
        assertUtils.assert_equals(text2, 'peter_fang@sekorm.com')

    @allure.story("英文站-已登录-ON详情页点击预览")
    def test_login_click_Preview(self):
        self.en_sekorm.get_en_login().go_EnOnPage_by_id().login_click_Preview()

    @allure.story("英文站-已登录-ON详情页点击Buy")
    def test_login_click_Buy(self):
        text, EnUserListPage = self.en_sekorm.get_en_login().go_EnOnPage_by_id().login_click_Buy().check_join_cart()
        text2 = EnUserListPage.check_en_user_list_layout()
        assertUtils.assert_equals(text, 'Added successfully!')
        assertUtils.assert_equals(text2, 'Check Out')

    @allure.story("英文站-已登录-检查购物车")
    def test_check_en_user_list_layout(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().check_en_user_list_layout()
        assertUtils.assert_equals(text, 'Check Out')

    @allure.story("英文站-已登录-检查购物车移除按钮")
    @pytest.mark.parametrize('elm', ['删除按钮', 'Remove Selected'])
    def test_click_en_list_delete(self, elm):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_list_delete(elm)
        assertUtils.assert_equals(text, 'Do you confirm to delete this product ?')

    @allure.story("英文站-已登录-订单审核页")
    def test_check_order_filling(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().check_order_filling()
        assertUtils.assert_equals(text, 'Order Filling and Checking')

    @allure.story("英文站-已登录-订单审核页-地址编辑")
    def test_check_en_order_address(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().check_en_order_address()
        assertUtils.assert_equals(text, 'Please fill in Recipient')

    @allure.story("英文站-已登录-订单审核页-买卖合同")
    def test_check_en_sales_agreement(self):
        self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().check_en_sales_agreement()
        text = 'Goods (Services) Sales Agreement of Sekorm Platform'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('h3', text), text)

    @allure.story("英文站-已登录-订单审核页-ON信息检查")
    def test_check_en_order_on_info(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().check_en_order_on_info()
        assertUtils.assert_equals(text, 'Sekorm Advanced Technology (Shenzhen) Co., Ltd')

    @allure.story("英文站-已登录-订单审核页-点击ON型号")
    def test_click_en_order_on(self):
        self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().click_en_order_on().check_en_on_layout()

    @allure.story("英文站-已登录-订单审核页-点击ON厂牌")
    def test_click_en_order_brand(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out() \
            .click_en_order_brand().get_search_text()
        assert text, '搜索词不为空'

    @allure.story("英文站-已登录-订单审核页-点击提交订单")
    def test_click_en_order_submit(self):
        text = self.en_sekorm.get_en_login().go_EnUserListPage().click_en_check_out().click_en_order_submit()
        assertUtils.assert_equals(text, 'Please enter company name.')

    @allure.story("英文站-已登录-我的订单")
    def test_check_empty_order_list(self):
        num = self.en_sekorm.get_en_login().go_EnUserOrderPage().check_en_order_list()
        text = 'Order Details'
        assertUtils.assert_greater_equal(num, 7)
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('p', text), text)

    @allure.story("英文站-已登录-商城页-点击Buy")
    def test_login_click_en_on(self):
        text, EnUserListPage = self.en_sekorm.get_en_login().go_EnSupplyPage().next_page(True).next_page(True).next_page(True).login_click_en_supply_buy() \
            .check_join_cart()
        text = EnUserListPage.click_en_check_out().click_en_order_submit()
        assertUtils.assert_equals(text, 'Please enter company name.')
