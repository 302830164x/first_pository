import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature('前台个人中心')
class Test_UserInfo:

    # 首页登录
    @pytest.fixture(scope='class', autouse=True)
    def set_sekorm_login(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.get_login()

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver.go_SekormIndexPage().go_UserInfoPage()
        yield
        self.sekorm.close_driver()

    @allure.story("跳转个人中心")
    def test_go_userinfo(self):
        self.sekorm.check_user_info()

    @allure.story("跳转做任务")
    def test_click_user_info(self):
        self.sekorm.click_user_info('做任务')
        assert_text = '今日赚取经验值', '日常任务'
        assertUtils.assert_contains(self.sekorm.get_assert_text('p', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("跳转修改密码")
    def test_click_change_keyword(self):
        self.sekorm.click_user_info('账户设置').click_user_info('修改密码')
        assert_text = '手机号', '获取验证码', '登录密码'
        assertUtils.assert_contains(self.sekorm.get_assert_text('label', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.sekorm.get_assert_text('label', assert_text[2]), assert_text[2])

    @allure.story("点击账号安全")
    def test_click_user_info_1(self):
        self.sekorm.click_user_info('账户设置').click_user_info('账号安全')
        assert_text = '世强硬创平台使用许可协议', '如何注销账号？'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("点击账号安全-账号注销")
    def test_click_user_info_toCancellation(self):
        self.sekorm.click_user_info('账户设置').click_user_info('账号安全').click_user_info('账号注销')
        assert_text = '注销后，您将放弃以下权益:', '同意注销'
        assertUtils.assert_equals(self.sekorm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('button', assert_text[1]), assert_text[1])

    @allure.story("点击收货地址")
    def test_click_user_info_2(self):
        self.sekorm.click_user_info('账户设置').click_user_info('收货地址')
        assert_text = '最多可创建6个收货地址', '默认地址', '收货人'
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.sekorm.get_assert_text('i', assert_text[2]), assert_text[2])

    @allure.story("点击发票抬头管理")
    def test_click_user_info_3(self):
        self.sekorm.click_user_info('账户设置').click_user_info('发票抬头管理')
        assert_text = '发票抬头', '炯鳌商贸(上海)有限公司'
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story("点击修改我的企业信息")
    def test_click_user_info_4_2(self):
        self.sekorm.click_user_info('修改企业信息')
        assert_text = '请填写企业域名的工作邮箱，以便世强硬创为您提供B2B服务', '企业全称：', '获取验证码'
        assertUtils.assert_equals(self.sekorm.get_assert_text('p', assert_text[0]), assert_text[0])
        assertUtils.assert_contains(self.sekorm.get_assert_text('dt', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("点击批量询价")
    def test_click_user_info_11(self):
        num = self.sekorm.click_user_info('更多选型').click_user_info('批量询价').check_list_num()
        assertUtils.assert_greater_equal(num, 4)

    @allure.story("点击交期查询")
    def test_click_user_info_11_2(self):
        num = self.sekorm.click_user_info('更多选型').click_user_info('交期查询').check_list_num()
        assertUtils.assert_greater_equal(num, 2)

    @allure.story("点击技术问题")
    def test_click_user_info_8(self):
        self.sekorm.click_user_info('更多选型').click_user_info('技术问题')
        assert_text = '技术问题'
        assertUtils.assert_contains(self.sekorm.get_assert_text('span', assert_text), assert_text)

    @allure.story("点击我的资料")
    def test_click_user_info_5(self):
        self.sekorm.click_user_info('我的收藏').click_user_info('我的资料-我的下载')
        assert_text = 'LS6R0400 SERIES Dc Disconnect Switch', '2022-04-24'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('td', assert_text[1]), assert_text[1])

    @allure.story("点击我的资料-我的收藏")
    def test_click_user_info_5_2(self):
        self.sekorm.click_user_info('我的收藏').click_user_info('我的收藏')
        assert_text = '标题', '删除', '历史记录'
        assertUtils.assert_equals(self.sekorm.get_assert_text('th', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("点击我的资料-历史记录")
    def test_click_user_info_5_3(self):
        self.sekorm.click_user_info('我的收藏').click_user_info('我的资料-历史记录')
        assert_text = '我的下载', '我的收藏'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("点击我的收藏")
    def test_click_user_info_5_2(self):
        self.sekorm.click_user_info('我的收藏')
        assert_text = '标题', '删除', '历史记录'
        assertUtils.assert_equals(self.sekorm.get_assert_text('th', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("点击我的消息")
    def test_click_user_info_6(self):
        self.sekorm.click_user_info('我的消息')
        assert_text = '标题', '世强硬创平台'
        assertUtils.assert_equals(self.sekorm.get_assert_text('th', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('td', assert_text[1]), assert_text[1])

    @allure.story("搜索活动")
    def test_click_user_info_9(self):
        num = self.sekorm.check_search('活动').check_list_num()
        assertUtils.assert_greater_equal(num, 2)

    @allure.story("搜索奖品发放")
    def test_click_user_info_10(self):
        num = self.sekorm.check_search('奖品发放').check_list_num()
        assertUtils.assert_greater_equal(num, 5)

    @allure.story("搜索样品申请")
    def test_click_user_info_12(self):
        num = self.sekorm.check_search('样品申请').check_list_num()
        assertUtils.assert_greater_equal(num, 3)

    @allure.story("搜索加工定制")
    def test_click_user_info_13(self):
        num = self.sekorm.check_search('加工定制').check_list_num()
        assertUtils.assert_greater_equal(num, 2)

    @allure.story("搜索小量快购")
    def test_click_user_info_14(self):
        num = self.sekorm.check_search('小量快购').check_list_num()
        assertUtils.assert_greater_equal(num, 20)

    @allure.story("搜索选型帮助")
    def test_click_user_info_15(self):
        num = self.sekorm.check_search('选型帮助').check_list_num()
        assertUtils.assert_greater_equal(num, 1)

    @allure.story("搜索期货订购")
    def test_click_user_info_16(self):
        num = self.sekorm.check_search('期货订购').check_list_num()
        assertUtils.assert_greater_equal(num, 2)

    @allure.story("点击历史记录-查看更多")
    def test_click_user_info_17(self):
        self.sekorm.click_user_info('历史记录')
        assert_text = '热门', '购买清单'
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_contains(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("点击历史记录-查看更多")
    def test_click_user_info_18(self):
        self.sekorm.click_user_info('历史记录-查看更多')
        assert_text = '我的下载', '我的收藏'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])
