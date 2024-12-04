import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("主搜")
class Test_Search:
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story('厂牌场景搜索')
    @pytest.mark.parametrize('searchWord', ['泰科', 'ROHM', 'silicon labs'])
    def test_searchBrand(self, searchWord):
        searchPage = self.sekorm.get_search(searchWord)
        assertUtils.assert_greater_equal(searchPage.get_element_num('主搜厂牌场景品牌介绍'), 1)
        assertUtils.assert_contains(searchPage.get_type_text('主搜厂牌场景授权代理商')[0], '授权代理商')
        assertUtils.assert_greater_equal(searchPage.get_text_num('主搜厂牌场景小类', '选型指南'), 5)
        assertUtils.assert_between_equal(searchPage.get_selection_num('主搜厂牌场景小类'), 5, 30)
        # assertUtils.assert_equals(searchPage.get_element_num('主搜厂牌场景服务通栏'), 1)
        assertUtils.assert_between_equal(searchPage.get_element_num("主搜厂牌场景右侧商城"), 1, 10)
        assertUtils.assert_between_equal(searchPage.get_element_num("主搜厂牌场景右侧市场"), 1, 12)

    @allure.story('厂牌场景-点击品牌介绍描述、厂牌图、查看更多')
    @pytest.mark.parametrize('elem', ['主搜厂牌场景品牌介绍描述', '主搜厂牌场景品牌介绍logo', '主搜厂牌场景品牌介绍查看更多'])
    def test_click_MFRProfile(self, elem):
        NewsDetailPage = self.sekorm.get_search('silicon labs').get_MFRProfile_detail(elem)
        NewsDetailPage.check_news_detail_layout()

    @allure.story('厂牌场景-点击品牌介绍品类')
    def test_click_MFRProfileGoods(self):
        for i in self.sekorm.get_search('smi').click_MFRProfile_goods('主搜厂牌场景品牌介绍品类'):
            assertUtils.assert_contains_one(i[0], (f'SMI {i[1]}</span></h1>相关结果约', f'TE connectivity {i[1]}</span></h1'
                                                                                   f'>相关结果约'))

    # @allure.story('厂牌场景-点击授权代理商')
    # def test_click_supplierName(self):
    #     self.sekorm.get_search('silicon labs').click_supplierName('主搜厂牌场景品牌介绍授权代理商')

    @allure.story("搜索结果页-检查相关推荐服务模块-点击服务名称")
    def test_check_right_service(self):
        self.ServiceCommPage = self.sekorm.get_search('MCU').check_right_service()
        assertUtils.assert_contains(self.ServiceCommPage.get_assert_text('span', '液晶显示屏/模组定制'), 'TFT LCD液晶显示屏/模组定制')

    @allure.story("搜索结果页-检查相关推荐ON模块-点击商城型号名称")
    def test_search_go_SupplySearchPage(self):
        text, SupplySearchPage = self.sekorm.get_search('ROHM').go_SupplySearchPage('右侧ON列表-商城ON名称')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_contains_one(text2, [text, 'ROHM'])

    @allure.story("搜索结果页-检查相关推荐ON模块-点击市场型号名称")
    def test_search_go_MallSearchPage(self):
        text, MallSearchPage = self.sekorm.get_search('ROHM').go_MallSearchPage('右侧ON列表-市场ON名称')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_contains_one(text2, [text, 'ROHM'])

    @allure.story("搜索结果页-检查相关推荐ON模块-点击商城查看更多")
    def test_search_go_Supply_read_more(self):
        text, SupplySearchPage = self.sekorm.get_search('ROHM').go_SupplySearchPage('右侧ON列表-商城查看更多')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, 'ROHM')

    @allure.story("搜索结果页-检查相关推荐ON模块-点击市场查看更多")
    def test_search_go_Mall_read_more(self):
        text, MallSearchPage = self.sekorm.get_search('ROHM').go_MallSearchPage('右侧ON列表-市场查看更多')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, 'ROHM')

    @allure.story("搜索结果页-检查相关推荐ON模块-检查描述内容")
    def test_search_check_description(self):
        text1, text2 = self.sekorm.get_search('ROHM').check_right_on_description()
        assertUtils.assert_equals(text1, '电子商城')
        assertUtils.assert_equals(text2, '现货市场')

    @allure.story("搜索结果页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    def test_search_unlogin_click_supply_service(self, elm, text):
        text1, SupplySearchPage = self.sekorm.get_search('ROHM').check_right_supply_service(elm)
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_contains(text1, (elm, text))
        assertUtils.assert_equals(text2, 'ROHM')

    @allure.story("搜索结果页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('市场-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_search_unlogin_click_mall_service(self, elm, text):
        text1, MallSearchPage = self.sekorm.get_search('ROHM').check_right_mall_service(elm)
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_contains(text1, text)
        assertUtils.assert_equals(text2, 'ROHM')

    # @allure.story("搜索结果页-检查相关服务模块")
    # @pytest.mark.parametrize('elm,text', [('BOM配单', '请提交您的BOM清单，世强客服提供所需型号的价格、交期、最小包装、MOQ等信息'),
    #                                       ('技术问答', '请输入您要提问内容，世强及原厂FAE将尽力给您提供疑难解答和技术支持'),
    #                                       ('选型帮助', '请补充您需要选型的产品及参数要求，世强和原厂的技术专家为您推荐功能、价格、供应最优的产品，协助您快速完成设计'),
    #                                       ('设计方案', '请补充您的方案需求，世强和原厂的应用技术专家提供从元器件、接插件及结构件、组部件到电子材料的整体最优选择'),
    #                                       ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    # def test_click_common_service(self, elm, text):
    #     self.ServiceCommPage, assert_text = self.sekorm.get_search('ROHM').click_common_service(elm)
    #     assertUtils.assert_contains(assert_text, (elm, text))
    #     assertUtils.assert_equals(self.ServiceCommPage.get_assert_text('span', elm), elm)

    @allure.story("搜索结果页-点击 右侧广告")
    @pytest.mark.parametrize('elm', ['右侧广告1'])
    def test_search_click_right_advertising(self, elm):
        url = self.sekorm.get_search('ROHM').check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webRight', 'adPack=webSearch', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("搜索结果页-点击 右侧广告")
    @pytest.mark.parametrize('elm', ['右侧广告1'])
    def test_search_next_click_right_advertising(self, elm):
        url = self.sekorm.get_search('ROHM').next_page(True).check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webRight', 'adPack=webSearch', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("搜索结果页-检查左侧广告")
    @pytest.mark.parametrize('elm', ['左侧广告1', '左侧广告2'])
    def test_search_left_advertising(self, elm):
        url = self.sekorm.get_search('ROHM').check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webLeft', 'adPack=webSearch', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    # @allure.story("搜索结果页-检查右侧LOGO墙")
    # def test_check_search_logo(self):
    #     text1, text2, self.BrandSearchPage = self.sekorm.get_search('ROHM').check_logo()
    #     text3 = self.BrandSearchPage.get_search_text()
    #     assertUtils.assert_equals(text1, '')
    #     assertUtils.assert_equals(text2, 'display: block;')
    #     assertUtils.assert_equals(text3, 'ROHM')

    # @allure.story("搜索结果页-检查logo墙下方我要提问按钮、文案")
    # def test_check_search_right_ask(self):
    #     text, AskServicePage = self.sekorm.get_search('ROHM').check_ask()
    #     AskServicePage.get_login().check_AskServicePage()
    #     assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
    #     assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
    #     AskServicePage.quit_login()
