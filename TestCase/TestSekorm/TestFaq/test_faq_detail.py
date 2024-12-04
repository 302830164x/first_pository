import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("问答详情页")
class Test_FaqDetail:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.FaqDetailPage = self.sekorm.go_FaqDetailPage_byID(92119)
        yield
        self.sekorm.close_driver()

    @allure.story("问答详情页-检查各个模块布局")
    def test_check_layout(self):
        title, time = self.FaqDetailPage.check_layout()
        assertUtils.assert_equals(title, 'RENESAS rl78系列微控制器内置了哪种串行接口？')
        assertUtils.assert_equals(time, '创建于2019-10-29')

    @allure.story("问答详情页-检查右侧LOGO墙")
    def test_check_ask_logo(self):
        self.BrandSearchPage = self.FaqDetailPage.check_logo()
        text1 = self.BrandSearchPage.get_search_text()
        assertUtils.assert_equals(text1, 'ROHM')

    @allure.story("问答详情页-检查logo墙下方我要提问按钮、文案")
    def test_check_right_ask(self):
        text, AskServicePage = self.FaqDetailPage.check_ask()
        AskServicePage.get_login().check_AskServicePage()
        assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
        AskServicePage.quit_login()

    @allure.story("问答详情页-点击 右侧广告")
    @pytest.mark.parametrize('elm', ['右侧广告1', '右侧广告2'])
    def test_FaqPage_click_advertising(self, elm):
        url = self.FaqDetailPage.check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webRight', 'adPack=webFaq', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("问答详情页-检查相关服务展开、收起")
    def test_check_service_open(self):
        close1, open2, close3 = self.FaqDetailPage.check_service_open()
        assertUtils.assert_equals(close1, 'service-brand-collapse')
        assertUtils.assert_equals(open2, 'service-brand-collapse service-brand-collapse-open')
        assertUtils.assert_equals(close3, 'service-brand-collapse')

    @allure.story("问答详情页-未登录检查写回答展开、参与问答")
    def test_check_unlogin_answer_open(self):
        self.UnLoginPage, answer_close, answer_open = self.FaqDetailPage.check_unlogin_answer_open()
        assert_text = self.UnLoginPage.close_login()
        assertUtils.assert_contains(answer_close, 'ask-slide-down')
        assertUtils.assert_contains(answer_open, 'ask-slide-up')
        assertUtils.assert_equals(assert_text, '所属国家/地区')

    @allure.story("问答详情页-点击回答时间，跳转问答详情页")
    def test_check_answer_detail(self):
        url = self.FaqDetailPage.check_answer_detail()
        assertUtils.assert_contains(url, f'{ini.SekormUrl}/faq/ansDetail')
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("问答详情页-未登录检查发送邮件、收藏、转发")
    @pytest.mark.parametrize('elm', ['发送到邮箱', '收藏', '转发-微信', '转发-QQ', '转发-微博'])
    def test_check_unlogin_bottom(self, elm):
        self.UnLoginPage = self.FaqDetailPage.check_unlogin_bottom(elm)
        assert_text = self.UnLoginPage.close_login()
        assertUtils.assert_equals(assert_text, '所属国家/地区')

    @allure.story("问答详情页-检查点赞按钮")
    def test_check_like(self):
        text1, text2 = self.FaqDetailPage.check_like()
        assertUtils.assert_contains(text1, 'unpraise')
        assertUtils.assert_contains(text2, 'praised')

    @allure.story("问答详情页-检查相关服务模块")
    @pytest.mark.parametrize('elm,text', [('技术问答', '请输入您要提问内容，世强及原厂FAE将尽力给您提供疑难解答和技术支持'),
                                          ('选型帮助', '请补充您需要选型的产品及参数要求，世强和原厂的技术专家为您推荐功能、价格、供应最优的产品，协助您快速完成设计'),
                                          ('设计方案', '请补充您的方案需求，世强和原厂的应用技术专家提供从元器件、接插件及结构件、组部件到电子材料的整体最优选择'),
                                          ('研发服务', '提交您项目研发过程中遇到的困难，不限于方案定型、器件替代、仿真设计、软件调试、测试方案、编程校准、加工定制建议等'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    def test_click_common_service(self, elm, text):
        self.ServiceCommPage, assert_text = self.FaqDetailPage.click_common_service(elm)
        assertUtils.assert_contains(assert_text, (elm, text))
        assertUtils.assert_equals(self.ServiceCommPage.get_assert_text('span', elm), elm)

    @allure.story("问答详情页-检查相关推荐ON模块-点击商城型号名称")
    def test_news_go_SupplySearchPage(self):
        text, SupplySearchPage = self.FaqDetailPage.go_SupplySearchPage('右侧ON列表-商城ON名称')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(text, 'ESD05V52D-C')
        assertUtils.assert_equals(text2, '')

    @allure.story("问答详情页-检查相关推荐ON模块-点击市场型号名称")
    def test_news_go_MallSearchPage(self):
        text, MallSearchPage = self.FaqDetailPage.go_MallSearchPage('右侧ON列表-市场ON名称')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_equals(text, 'R5F10BBGKNA#G5')
        assertUtils.assert_equals(text2, '')

    @allure.story("问答详情页-检查相关推荐ON模块-点击商城查看更多")
    def test_news_go_Supply_read_more(self):
        text, SupplySearchPage = self.FaqDetailPage.go_SupplySearchPage('右侧ON列表-商城查看更多')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, '')

    @allure.story("问答详情页-检查相关推荐ON模块-点击市场查看更多")
    def test_news_go_Mall_read_more(self):
        text, MallSearchPage = self.FaqDetailPage.go_MallSearchPage('右侧ON列表-市场查看更多')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, '')

    @allure.story("问答详情页-检查相关推荐ON模块-检查描述内容")
    def test_check_description(self):
        text1, text2 = self.FaqDetailPage.check_right_on_description()
        assertUtils.assert_equals(text1, '电子商城')
        assertUtils.assert_equals(text2, '现货市场')

    @allure.story("问答详情页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('期货订购', '请补充您所需订购的产品型号、厂牌、数量、期望交期等信息')])
    def test_unlogin_click_supply_service(self, elm, text):
        text1, SupplySearchPage = self.FaqDetailPage.check_right_supply_service(elm)
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_contains(text1, (elm, text))
        assert text2 == ""

    @allure.story("问答详情页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('市场-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_unlogin_click_mall_service(self, elm, text):
        text1, MallSearchPage = self.FaqDetailPage.check_right_mall_service(elm)
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_contains(text1, text)
        assert text2 == ""

    @allure.story("问答详情页-检查相关推荐模块内容")
    def test_check_recommend(self):
        self.FaqDetailPage.check_recommend_list()
        assert_text = '时间：'
        assertUtils.assert_equals(self.sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("问答详情页-检查相关推荐模块查看更多")
    @pytest.mark.parametrize('elm1,elm2', [('推荐列表', '推荐列表-展开更多')])
    def test_check_read_more(self, elm1, elm2):
        total = self.FaqDetailPage.check_num(elm1)
        assertUtils.assert_between_equal(total, 1, 15)
        if total == 15:
            self.FaqDetailPage.check_common_click(elm2)
            total2 = self.FaqDetailPage.check_num(elm1)
            assertUtils.assert_between_equal(total2, 15, 30)