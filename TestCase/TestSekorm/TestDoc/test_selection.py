import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("选型表详情页")
class Test_Selection:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.SelectionDetailPage = self.sekorm.go_SelectionDetailPage_byID(308)
        yield
        self.sekorm.close_driver()

    @allure.story("选型表详情页-检查各个模块布局")
    def test_check_selection_layout(self):
        text, size = self.SelectionDetailPage.check_SelectionDetailPage_layout()
        assertUtils.assert_contains(text, '台达DC/EC风扇选型表')
        assertUtils.assert_equals(size, (160, 80))

    @allure.story("选型表详情页-检查全屏按钮")
    def test_check_fullScreen(self):
        num = self.SelectionDetailPage.check_fullScreen()
        assertUtils.assert_equals(num, 100)

    @allure.story("选型表详情页-检查选型表搜索")
    def test_check_selection_search(self):
        num1, num2 = self.SelectionDetailPage.check_selection_search('25.4mm')
        assertUtils.assert_greater(num1, num2)

    @allure.story("选型表详情页-检查编辑表头")
    def test_check_selection_edit(self):
        num1, num2 = self.SelectionDetailPage.check_selection_edit()
        assertUtils.assert_greater(num1, num2)
