import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("技术问答")
class Test_Faq:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story("技术问答-检查门楣是否高亮")
    def test_go_FaqPage(self):
        self.sekorm.go_FaqPage()
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('技术问答', 'class'), 'index nav-active')

    @allure.story("技术问答-检查顶部我要提问按钮、文案")
    def test_check_top_ask(self):
        text, AskServicePage = self.sekorm.go_FaqPage().check_top_ask()
        AskServicePage.get_login().check_AskServicePage()
        assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
        AskServicePage.quit_login()

    @allure.story("技术问答-检查列表问答数量")
    def test_check_list_num(self):
        num1, num2= self.sekorm.go_FaqPage().check_list_num()
        assertUtils.assert_equals(num1, 20)
        assertUtils.assert_equals(num2, 10)

    @allure.story("技术问答-检查列表问答内容")
    def test_check_list(self):
        size, text = self.sekorm.go_FaqPage().check_list()
        assertUtils.assert_equals(size, (160, 80))
        assertUtils.assert_contains(text, '发布时间')

    @allure.story("技术问答-未登录点击列表问答内容")
    @pytest.mark.parametrize('elm', ['第10条问答', '第20条问答', '第10条等你来答'])
    def test_click_ask_list(self, elm):
        text = self.sekorm.go_FaqPage().click_ask_list(elm).check_unlogin()
        assertUtils.assert_contains(text, '登录后才可以参与回答')

    @allure.story("技术问答-检查右侧LOGO墙")
    def test_check_ask_logo(self):
        self.BrandSearchPage = self.sekorm.go_FaqPage().check_logo()
        text1 = self.BrandSearchPage.get_search_text()
        assertUtils.assert_equals(text1, 'ROHM')

    # @allure.story("技术问答-检查logo墙下方我要提问按钮、文案")
    # def test_check_right_ask(self):
    #     text, AskServicePage = self.sekorm.go_FaqPage().check_ask()
    #     AskServicePage.get_login().check_AskServicePage()
    #     assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
    #     assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
    #     AskServicePage.quit_login()

    @allure.story("技术问答-点击 右侧广告")
    @pytest.mark.parametrize('elm', ['右侧广告1', '右侧广告2'])
    def test_FaqPage_click_advertising(self, elm):
        url = self.sekorm.go_FaqPage().check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webRight', 'adPack=webFaq', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    # @allure.story("技术问答-检查相关服务模块")
    # @pytest.mark.parametrize('elm,text', [('BOM配单', '请提交您的BOM清单，世强客服提供所需型号的价格、交期、最小包装、MOQ等信息'),
    #                                       ('技术问答', '请输入您要提问内容，世强及原厂FAE将尽力给您提供疑难解答和技术支持'),
    #                                       ('选型帮助', '请补充您需要选型的产品及参数要求，世强和原厂的技术专家为您推荐功能、价格、供应最优的产品，协助您快速完成设计'),
    #                                       ('设计方案', '请补充您的方案需求，世强和原厂的应用技术专家提供从元器件、接插件及结构件、组部件到电子材料的整体最优选择'),
    #                                       ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    # def test_click_common_service(self, elm, text):
    #     self.ServiceCommPage, assert_text = self.sekorm.go_FaqPage().click_common_service(elm)
    #     assertUtils.assert_contains(assert_text, (elm, text))
    #     assertUtils.assert_equals(self.ServiceCommPage.get_assert_text('span', elm), elm)
