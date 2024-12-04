import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("电子商城")
class Test_Supply:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story("电子商城-检查门楣是否高亮")
    def test_go_SupplyPage(self):
        self.sekorm.go_SupplyPage()
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('电子商城', 'class'), 'index nav-active')

    @allure.story("电子商城-检查图片是否加载成功")
    @pytest.mark.parametrize('elm, size', [('轮播图', (2400, 200)), ('授权代理品牌', (240, 144)), ('生态合作伙伴', (240, 120))])
    def test_check_img(self, elm, size):
        img_size = self.sekorm.go_SupplyPage().check_img(elm)
        assertUtils.assert_equals(img_size, size)

    @allure.story("电子商城-点击型号名称、技术资料")
    @pytest.mark.parametrize('elm', ['ON名称', '技术资料'])
    def test_go_OnPage(self, elm):
        text = self.sekorm.go_SupplyPage().go_OnPage(elm).check_layout()
        assertUtils.assert_equals(text, '规格参数')

    @allure.story("电子商城-点击厂牌名称")
    def test_go_brand_search(self):
        url = self.sekorm.go_SupplyPage().go_brand_search().driver.current_url
        assertUtils.assert_contains(url, f'{ini.SekormUrl}/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("电子商城-点击授权代理品牌、生态合作伙伴")
    @pytest.mark.parametrize('elm', ['授权代理品牌', '生态合作伙伴'])
    def test_go_brand_search(self, elm):
        url = self.sekorm.go_SupplyPage().click_img(elm).driver.current_url
        assertUtils.assert_contains(url, f'{ini.SekormUrl}/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("电子商城-检查描述内容")
    def test_check_description(self):
        text = self.sekorm.go_SupplyPage().check_description()
        assertUtils.assert_contains(text, '最小包装量：')

    @allure.story("电子商城-检查供应商/品质保证")
    def test_check_supplier(self):
        text = self.sekorm.go_SupplyPage().check_supply_supplier()
        assertUtils.assert_equals(text, '世强先进（深圳）科技股份有限公司')

    @allure.story("电子商城-检查单价（含增值税）")
    def test_check_ON_information(self):
        text = self.sekorm.go_SupplyPage().check_ON_information()
        assertUtils.assert_contains(text, '(当天发货)')

    @allure.story("电子商城-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息')])
    def test_unlogin_click_service(self, elm, text):
        text1, self.UnLoginPage = self.sekorm.refresh().go_SupplyPage().unlogin_click_service(elm)
        text2 = self.UnLoginPage.close_login()
        assertUtils.assert_contains(text1, (elm, text))
        assertUtils.assert_equals(text2, '所属国家/地区')

    @allure.story("电子商城-翻页检查")
    def test_next_page(self):
        active = self.sekorm.go_SupplyPage().next_page(next_action=False)
        assert active, "第二页选中高亮"

    @allure.story("电子商城-翻页后点击型号名称、技术资料")
    @pytest.mark.parametrize('elm', ['ON名称', '技术资料'])
    def test_next_go_OnPage(self, elm):
        text = self.sekorm.go_SupplyPage().next_page(next_action=True).go_OnPage(elm).check_layout()
        assertUtils.assert_equals(text, '规格参数')

    @allure.story("电子商城-翻页后点击厂牌名称")
    def test_next_go_brand_search(self):
        url = self.sekorm.go_SupplyPage().next_page(next_action=True).go_brand_search().driver.current_url
        assertUtils.assert_contains(url, f'{ini.SekormUrl}/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("电子商城-点击授权代理品牌、生态合作伙伴")
    @pytest.mark.parametrize('elm', ['授权代理品牌', '生态合作伙伴'])
    def test_next_go_brand_search(self, elm):
        url = self.sekorm.go_SupplyPage().next_page(next_action=True).click_img(elm).driver.current_url
        assertUtils.assert_contains(url, f'{ini.SekormUrl}/brand/')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("电子商城-翻页后检查描述内容")
    def test_next_check_description(self):
        text = self.sekorm.go_SupplyPage().next_page(next_action=True).check_description()
        assertUtils.assert_contains(text, '最小包装量：')

    @allure.story("电子商城-翻页后检查供应商/品质保证")
    def test_next_check_supplier(self):
        text = self.sekorm.go_SupplyPage().next_page(next_action=True).check_supply_supplier()
        assertUtils.assert_equals(text, '世强先进（深圳）科技股份有限公司')

    @allure.story("电子商城-翻页后检查单价（含增值税）")
    def test_next_check_ON_information(self):
        text = self.sekorm.go_SupplyPage().next_page(next_action=True).check_ON_information()
        assertUtils.assert_contains(text, '(当天发货)')

    @allure.story("电子商城-翻页后未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批'),
                                          ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息')])
    def test_unlogin_next_page_click_service(self, elm, text):
        text1, self.UnLoginPage = self.sekorm.go_SupplyPage().next_page(next_action=True).unlogin_click_service(elm)
        text2 = self.UnLoginPage.close_login()
        assertUtils.assert_contains(text1, (elm, text))
        assertUtils.assert_equals(text2, '所属国家/地区')