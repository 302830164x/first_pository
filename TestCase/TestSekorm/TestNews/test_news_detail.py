import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("资讯详情页")
class Test_NewsDetail:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.NewsDetailPage = self.sekorm.go_NewsDetailPage_byID(32685683)
        self.NewsDetailPage.close_login()
        yield
        self.sekorm.close_driver()

    @allure.story("资讯详情页-检查各个模块布局")
    def test_check_layout(self):
        title, time = self.NewsDetailPage.check_news_detail_layout()
        assertUtils.assert_equals(title, '研讨会 11月3日组部件新品,WAGO, 菲尼克斯, 魏德米勒, TE, 金霸王等（重播）')
        assertUtils.assert_equals(time, '时间： 2022-10-16')

    @allure.story("资讯详情页-检查右侧LOGO墙")
    def test_check_news_logo(self):
        self.BrandSearchPage = self.NewsDetailPage.check_logo()
        text1 = self.BrandSearchPage.get_search_text()
        assertUtils.assert_equals(text1, 'ROHM')

    @allure.story("资讯详情页-检查logo墙下方我要提问按钮、文案")
    def test_check_right_ask(self):
        text, AskServicePage = self.NewsDetailPage.check_ask()
        AskServicePage.get_login().check_AskServicePage()
        assertUtils.assert_equals(text, '世强和原厂的技术专家将在一个工作日内解答，帮助您快速完成研发及采购。')
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', '请输入提问内容'), '请输入提问内容')
        AskServicePage.quit_login()

    @allure.story("资讯详情页-点击 右侧广告")
    @pytest.mark.parametrize('elm', ['右侧广告1', '右侧广告2'])
    def test_NewsDetailPage_click_advertising(self, elm):
        url = self.NewsDetailPage.check_advertising(elm)
        assertUtils.assert_contains(url, ('adSeat=webRight', 'adPack=webNewsDetail', 'adp4'))
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', '热门'), '热门')

    @allure.story("资讯详情页-未登录检查发送邮件、收藏、转发")
    @pytest.mark.parametrize('elm', ['发送到邮箱', '收藏', '转发-微信', '转发-QQ', '转发-微博'])
    def test_check_unlogin_bottom(self, elm):
        self.UnLoginPage = self.NewsDetailPage.check_unlogin_bottom(elm)
        assert_text = self.UnLoginPage.close_login()
        assertUtils.assert_equals(assert_text, '所属国家/地区')

    @allure.story("资讯详情页-检查评论按钮")
    def test_check_comment_button(self):
        display1, display2 = self.NewsDetailPage.check_comment_button()
        assertUtils.assert_greater(display2[1], display1[1])

    @allure.story("资讯详情页-检查点赞按钮")
    def test_check_like(self):
        text1, text2 = self.NewsDetailPage.check_like()
        assertUtils.assert_contains(text1, 'unpraise')
        assertUtils.assert_contains(text2, 'praised')

    @allure.story("资讯详情页-检查相关服务模块")
    @pytest.mark.parametrize('elm,text', [('技术问答', '请输入您要提问内容，世强及原厂FAE将尽力给您提供疑难解答和技术支持'),
                                          ('选型帮助', '请补充您需要选型的产品及参数要求，世强和原厂的技术专家为您推荐功能、价格、供应最优的产品，协助您快速完成设计'),
                                          ('设计方案', '请补充您的方案需求，世强和原厂的应用技术专家提供从元器件、接插件及结构件、组部件到电子材料的整体最优选择'),
                                          ('研发服务', '提交您项目研发过程中遇到的困难，不限于方案定型、器件替代、仿真设计、软件调试、测试方案、编程校准、加工定制建议等'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    def test_click_common_service(self, elm, text):
        self.ServiceCommPage, assert_text = self.NewsDetailPage.click_common_service(elm)
        assertUtils.assert_contains(assert_text, (elm, text))
        assertUtils.assert_equals(self.ServiceCommPage.get_assert_text('span', elm), elm)

    @allure.story("资讯详情页-检查相关推荐ON模块-点击商城型号名称")
    def test_news_go_SupplySearchPage(self):
        text, SupplySearchPage = self.NewsDetailPage.go_SupplySearchPage('右侧ON列表-商城ON名称')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(text, 'TM0696TR-C1-B')
        assertUtils.assert_equals(text2, '')

    @allure.story("资讯详情页-检查相关推荐ON模块-点击市场型号名称")
    def test_news_go_MallSearchPage(self):
        text, MallSearchPage = self.NewsDetailPage.go_MallSearchPage('右侧ON列表-市场ON名称')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_equals(text, 'PJ4056')
        assertUtils.assert_equals(text2, '')

    @allure.story("资讯详情页-检查相关推荐ON模块-点击商城查看更多")
    def test_news_go_Supply_read_more(self):
        text, SupplySearchPage = self.NewsDetailPage.go_SupplySearchPage('右侧ON列表-商城查看更多')
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, '')

    @allure.story("资讯详情页-检查相关推荐ON模块-点击市场查看更多")
    def test_news_go_Mall_read_more(self):
        text, MallSearchPage = self.NewsDetailPage.go_MallSearchPage('右侧ON列表-市场查看更多')
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_equals(text, '查看更多')
        assertUtils.assert_equals(text2, '')

    @allure.story("资讯详情页-检查相关推荐ON模块-检查描述内容")
    def test_check_description(self):
        text1, text2 = self.NewsDetailPage.check_right_on_description()
        assertUtils.assert_equals(text1, '电子商城')
        assertUtils.assert_equals(text2, '现货市场')

    @allure.story("资讯详情页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批')])
    def test_unlogin_click_supply_service(self, elm, text):
        text1, SupplySearchPage = self.NewsDetailPage.check_right_supply_service(elm)
        text2 = SupplySearchPage.get_search_text()
        assertUtils.assert_contains(text1, (elm, text))
        assert text2 == ""

    @allure.story("资讯详情页-检查相关推荐ON模块-未登录点击服务按钮")
    @pytest.mark.parametrize('elm,text', [('市场-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应')])
    def test_unlogin_click_mall_service(self, elm, text):
        text1, MallSearchPage = self.NewsDetailPage.check_right_mall_service(elm)
        text2 = MallSearchPage.get_search_text()
        assertUtils.assert_contains(text1, text)
        assert text2 == ""

    @allure.story("资讯详情页-检查相关推荐模块内容")
    def test_check_recommend(self):
        self.NewsDetailPage.check_recommend_list()
        assert_text = '时间：'
        assertUtils.assert_equals(self.sekorm.get_assert_text('label', assert_text), assert_text)

    @allure.story("资讯详情页-检查相关推荐模块查看更多")
    @pytest.mark.parametrize('elm1,elm2', [('推荐列表', '推荐列表-展开更多')])
    def test_check_read_more(self, elm1, elm2):
        total = self.NewsDetailPage.check_num(elm1)
        assertUtils.assert_between_equal(total, 1, 15)
        if total == 15:
            self.NewsDetailPage.check_common_click(elm2)
            total2 = self.NewsDetailPage.check_num(elm1)
            assertUtils.assert_between_equal(total2, 15, 30)

    @allure.story("资讯详情页-检查点击关键字模块关键字")
    def test_check_keyword(self):
        keyword1, self.SearchPage = self.NewsDetailPage.check_keyword()
        keyword2 = self.SearchPage.get_search_text()
        assertUtils.assert_equals(keyword1, keyword2)

    @allure.story("资讯详情页-检查评论模块的登录、立即注册")
    @pytest.mark.parametrize('elm', ['登录', '立即注册'])
    def test_check_login_comment(self, elm):
        self.UnLoginPage = self.NewsDetailPage.check_unlogin_bottom(elm)
        assert_text = self.UnLoginPage.close_login()
        assertUtils.assert_equals(assert_text, '所属国家/地区')

    @allure.story("资讯详情页-检查评论区")
    def test_check_comment(self):
        num1, num2 = self.NewsDetailPage.check_comment()
        assertUtils.assert_equals(num1, 10)
        assertUtils.assert_equals(num2, 20)

    @allure.story("资讯详情页-检查视频")
    def test_check_video(self):
        play, close, stop_time = self.NewsDetailPage.check_video()
        assertUtils.assert_contains(play, 'display: none')
        assertUtils.assert_contains(close, 'display: block')
        assertUtils.assert_equals('00:07', stop_time)
