import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature('前台提交订单')
class Test_Submit:

    # 首页登录
    @pytest.fixture(scope='class', autouse=True)
    def set_sekorm_login(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.get_login()

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()
        self.sekorm.refresh()

    @allure.story("跳转电子商城，提交订单")
    def test_go_supply_submit(self):
        text1, ShopServicePage = self.sekorm.go_SupplyPage().supply_submit_order()
        text2 = ShopServicePage.check_join_cart()
        text3 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text1, ('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'))
        assertUtils.assert_equals(text2, '购买')
        assertUtils.assert_equals(text3, '订单填写及核对')

    @allure.story("跳转电子商城垂搜，提交订单")
    def test_go_supply_search_submit(self):
        text1, ShopServicePage = self.sekorm.go_SupplySearchPage('MCU').supply_search_submit_order()
        text2 = ShopServicePage.check_join_cart()
        text3 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text1, ('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'))
        assertUtils.assert_equals(text2, '购买')
        assertUtils.assert_equals(text3, '订单填写及核对')

    @allure.story("跳转现货市场，提交订单")
    def test_go_mall_submit(self):
        text1, ShopServicePage = self.sekorm.go_MallPage().mall_submit_order()
        text2 = ShopServicePage.check_join_cart()
        text3 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text1, ('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'))
        assertUtils.assert_equals(text2, '购买')
        assertUtils.assert_equals(text3, '订单填写及核对')

    @allure.story("跳转现货市场垂搜，提交订单")
    def test_go_mall_search_submit(self):
        text1, ShopServicePage = self.sekorm.go_MallSearchPage('MCU').mall_search_submit_order()
        text2 = ShopServicePage.check_join_cart()
        text3 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text1, ('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'))
        assertUtils.assert_equals(text2, '购买')
        assertUtils.assert_equals(text3, '订单填写及核对')

    @allure.story("跳转ON详情页，提交订单")
    @pytest.mark.parametrize('elm,text', [('ON详情页-商城-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('ON详情页-市场-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_go_on_submit(self, elm, text):
        text1, ShopServicePage = self.sekorm.go_OnPage_byID(23056365).on_submit_order(elm)
        text2 = ShopServicePage.check_join_cart()
        text3 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text1, text)
        assertUtils.assert_equals(text2, '购买')
        assertUtils.assert_equals(text3, '订单填写及核对')

    @allure.story("跳转电子商城，提交样品申请")
    def test_check_supply_sample(self):
        text, SampleApplicationPage = self.sekorm.go_SupplyPage().check_supply_sample()
        text1, text2 = SampleApplicationPage.check_sample_join_cart()
        text3, text4 = SampleApplicationPage.check_SampleApplicationPage()
        assertUtils.assert_contains(text, ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息'))
        assertUtils.assert_equals(text1, '样品申请')
        assertUtils.assert_contains(text2, '只对VIP和平台认证的最终用户开放')
        assertUtils.assert_equals(text3, '样品申请')
        assertUtils.assert_equals(text4, '请输入项目名称')

    @allure.story("跳转电子商城垂搜，提交样品申请")
    def test_check_supply_search_sample(self):
        text, SampleApplicationPage = self.sekorm.go_SupplySearchPage('MCU').check_supply_search_sample()
        text1, text2 = SampleApplicationPage.check_sample_join_cart()
        text3, text4 = SampleApplicationPage.check_SampleApplicationPage()
        assertUtils.assert_contains(text, ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息'))
        assertUtils.assert_equals(text1, '样品申请')
        assertUtils.assert_contains(text2, '只对VIP和平台认证的最终用户开放')
        assertUtils.assert_equals(text3, '样品申请')
        assertUtils.assert_equals(text4, '请输入项目名称')

    @allure.story("跳转ON详情页，提交样品申请")
    def test_check_on_sample(self):
        text, SampleApplicationPage = self.sekorm.go_OnPage_byID(15115).check_on_sample()
        text1, text2 = SampleApplicationPage.check_sample_join_cart()
        text3, text4 = SampleApplicationPage.check_SampleApplicationPage()
        assertUtils.assert_contains(text, ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息'))
        assertUtils.assert_equals(text1, '样品申请')
        assertUtils.assert_contains(text2, '只对VIP和平台认证的最终用户开放')
        assertUtils.assert_equals(text3, '样品申请')
        assertUtils.assert_equals(text4, '请输入项目名称')

    @allure.story("跳转电子商城，提交批量询价")
    def test_check_supply_ask_price(self):
        text, AskPricePage = self.sekorm.go_SupplyPage().check_supply_ask_price()
        text1 = AskPricePage.check_ask_price_join_cart()
        text2, text3 = AskPricePage.check_AskPricePage()
        assertUtils.assert_contains(text, ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'))
        assertUtils.assert_equals(text1, '批量询价')
        assertUtils.assert_equals(text2, '价格及供货查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转电子商城垂直搜索结果页，提交批量询价")
    def test_check_supply_search_ask_price(self):
        text, AskPricePage = self.sekorm.go_SupplySearchPage('MCU').check_supply_search_ask_price()
        text1 = AskPricePage.check_ask_price_join_cart()
        text2, text3 = AskPricePage.check_AskPricePage()
        assertUtils.assert_contains(text, ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'))
        assertUtils.assert_equals(text1, '批量询价')
        assertUtils.assert_equals(text2, '价格及供货查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转ON详情页，提交批量询价")
    def test_check_on_ask_price(self):
        text, AskPricePage = self.sekorm.go_OnPage_byID(15115).check_on_ask_price()
        text1 = AskPricePage.check_ask_price_join_cart()
        text2, text3 = AskPricePage.check_AskPricePage()
        assertUtils.assert_contains(text, ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'))
        assertUtils.assert_equals(text1, '批量询价')
        assertUtils.assert_equals(text2, '价格及供货查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转电子商城，提交 交期查询")
    def test_check_supply_ask_time(self):
        text, AskTimePage = self.sekorm.go_SupplyPage().check_supply_ask_time()
        text1 = AskTimePage.check_ask_price_join_cart()
        text2, text3 = AskTimePage.check_AskTimePage()
        assertUtils.assert_contains(text, ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应'))
        assertUtils.assert_equals(text1, '交期查询')
        assertUtils.assert_equals(text2, '交期查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转电子商城垂直搜索结果页，提交 交期查询")
    def test_check_supply_search_ask_time(self):
        text, AskTimePage = self.sekorm.go_SupplySearchPage('MCU').check_supply_search_ask_time()
        text1 = AskTimePage.check_ask_price_join_cart()
        text2, text3 = AskTimePage.check_AskTimePage()
        assertUtils.assert_contains(text, ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应'))
        assertUtils.assert_equals(text1, '交期查询')
        assertUtils.assert_equals(text2, '交期查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转ON详情页，提交 交期查询")
    def test_check_on_ask_time(self):
        text, AskTimePage = self.sekorm.go_OnPage_byID(15115).check_on_ask_time()
        text1 = AskTimePage.check_ask_price_join_cart()
        text2, text3 = AskTimePage.check_AskTimePage()
        assertUtils.assert_contains(text, ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应'))
        assertUtils.assert_equals(text1, '交期查询')
        assertUtils.assert_equals(text2, '交期查询')
        assertUtils.assert_equals(text3, '请输入公司名称')

    @allure.story("跳转电子商城，提交 期货订购")
    def test_check_supply_futures(self):
        text, FuturesPage = self.sekorm.go_SupplyPage().check_supply_futures()
        text1 = FuturesPage.check_futures_join_cart()
        text2, text3 = FuturesPage.check_FuturesPage()
        assertUtils.assert_contains(text, ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息'))
        assertUtils.assert_equals(text1, '期货订购')
        assertUtils.assert_equals(text2, '期货订购')
        assertUtils.assert_equals(text3, '请选择期望交期')

    @allure.story("跳转电子商城垂直搜索结果页，提交 期货订购")
    def test_check_supply_search_futures(self):
        text, FuturesPage = self.sekorm.go_SupplySearchPage('MCU').check_supply_search_futures()
        text1 = FuturesPage.check_futures_join_cart()
        text2, text3 = FuturesPage.check_FuturesPage()
        assertUtils.assert_contains(text, ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息'))
        assertUtils.assert_equals(text1, '期货订购')
        assertUtils.assert_equals(text2, '期货订购')
        assertUtils.assert_equals(text3, '请选择期望交期')

    @allure.story("跳转ON详情页，提交 期货订购")
    def test_check_on_futures(self):
        text, FuturesPage = self.sekorm.go_OnPage_byID(15115).check_on_futures()
        text1 = FuturesPage.check_futures_join_cart()
        text2, text3 = FuturesPage.check_FuturesPage()
        assertUtils.assert_contains(text, ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息'))
        assertUtils.assert_equals(text1, '期货订购')
        assertUtils.assert_equals(text2, '期货订购')
        assertUtils.assert_equals(text3, '请选择期望交期')
