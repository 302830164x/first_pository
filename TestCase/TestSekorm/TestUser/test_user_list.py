import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature('前台型号清单')
class Test_UserList:

    # 首页登录
    @pytest.fixture(scope='class', autouse=True)
    def set_sekorm_login(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.get_login()

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver.go_SekormIndexPage().go_UserListPage()
        yield
        self.sekorm.close_driver()

    @allure.story("检查型号清单布局")
    def test_go_user_list(self):
        text = self.sekorm.check_UserListPage()
        assertUtils.assert_equals(text, '型号清单')

    @allure.story("检查型号清单提交订单页")
    def test_check_UserListPage_submit(self):
        text, ShopServicePage = self.sekorm.check_UserListPage_submit()
        text2 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text, '已选\n3\n个型号')
        assertUtils.assert_equals(text2, '订单填写及核对')

    @allure.story("检查型号清单提交企业支付")
    def test_check_UserListPage_submit(self):
        text, ShopServicePage = self.sekorm.check_UserListPage_business_pay()
        text2 = ShopServicePage.check_submit_order()
        assertUtils.assert_contains(text, '已选\n3\n个型号')
        assertUtils.assert_equals(text2, '订单填写及核对')

    @allure.story("检查型号清单提交样品申请")
    def test_check_UserListPage_sample(self):
        text, SampleApplicationPage = self.sekorm.check_UserListPage_sample()
        text1, text2 = SampleApplicationPage.check_SampleApplicationPage()
        assertUtils.assert_contains(text, '已选\n3\n个型号')
        assertUtils.assert_equals(text1, '样品申请')
        assertUtils.assert_equals(text2, '请输入项目名称')

    @allure.story("检查型号清单提交批量询价")
    def test_check_UserListPage_ark_price(self):
        text, AskPricePage = self.sekorm.check_UserListPage_ark_price()
        text1, text2 = AskPricePage.check_AskPricePage()
        assertUtils.assert_contains(text, '已选\n3\n个型号')
        assertUtils.assert_equals(text1, '价格及供货查询')
        assertUtils.assert_equals(text2, '请输入公司名称')

    @allure.story("检查型号清单提交交期查询")
    def test_check_UserListPage_ark_time(self):
        text, AskTimePage = self.sekorm.check_UserListPage_ark_time()
        text1, text2 = AskTimePage.check_AskTimePage()
        assertUtils.assert_contains(text, '已选\n3\n个型号')
        assertUtils.assert_equals(text1, '交期查询')
        assertUtils.assert_equals(text2, '请输入公司名称')
