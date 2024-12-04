import allure
import pytest
from utils.assertUtils import assertUtils
from utils.times import sleep


@allure.epic('前台')
@allure.feature('前台我的订单')
class Test_UserOrder:

    # 首页登录
    @pytest.fixture(scope='class', autouse=True)
    def set_sekorm_login(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.get_login()

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver.go_SekormIndexPage().go_UserOrderPage()
        yield
        self.sekorm.close_driver()

    @allure.story("通过搜索查询订单")
    @pytest.mark.parametrize('text', ['小量快购', '930216103324', 'UPD79F7024MC-CAA-AX'])
    def test_go_order_detail_by_id(self, text):
        text = self.sekorm.find_order_by_search(text)
        assertUtils.assert_equals(text, 'UPD79F7024MC-CAA-AX')

    @allure.story("点击查看详情跳转订单详情页")
    def test_go_order_detail_by_check(self):
        OrderDetailPage = self.sekorm.go_OrderDetailPage_by_check()
        text = OrderDetailPage.check_order_detail_layout()
        assertUtils.assert_equals(text, 'UPD79F7024MC-CAA-AX')

    @allure.story("获取列表订单数量")
    def test_go_order_check_order_num(self):
        num1, num2 = self.sekorm.check_order_num()
        assertUtils.assert_equals(num1, 20)
        assertUtils.assert_greater(num2, 20)
