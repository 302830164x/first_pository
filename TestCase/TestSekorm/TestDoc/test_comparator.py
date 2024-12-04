import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature("对照表详情页")
class Test_DocDetail:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.ComparatorPage = self.sekorm.go_ComparatorPage_byID(347)
        yield
        self.sekorm.close_driver()

    @allure.story("对照表详情页-检查各个模块布局")
    def test_check_layout(self):
        title, text, num = self.ComparatorPage.check_comparator_layout()
        assertUtils.assert_contains(title, '得润电子-TE连接器对照表')
        assertUtils.assert_equals(text, '请到检索框查找更多数据')
        assertUtils.assert_greater_equal(num, 10)

    @allure.story("对照表详情页-检查对照表搜索")
    def test_comparator_search(self):
        num = self.ComparatorPage.comparator_search('178303-2')
        assertUtils.assert_between_equal(num, 1, 10)
