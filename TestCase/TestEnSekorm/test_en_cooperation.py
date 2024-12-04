import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('英文站')
@allure.feature("英文站合作页")
class TestEnSekorm:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.en_sekorm = self.sekorm.go_EnSekorm()
        yield
        self.sekorm.close_driver()

    @allure.story("英文站-门楣高亮")
    def test_go_EnCooperationPage(self):
        self.en_sekorm.go_EnCooperationPage()
        assert_text = 'Shopping Cart'
        assertUtils.assert_equals(self.en_sekorm.get_assert_text('a', assert_text), assert_text)
        assertUtils.assert_contains(self.en_sekorm.get_elm_attribute('英文站合作页', 'class'), ('new-nav', 'nav-active'))

    @allure.story("英文站-页面布局检查")
    def test_check_en_cooperation_layout(self):
        text = self.en_sekorm.go_EnCooperationPage().check_en_cooperation_layout()
        assertUtils.assert_equals(text, 'Hardware Innovation')

    @allure.story("英文站-表单按钮检查")
    def test_check_en_cooperation_button(self):
        text = self.en_sekorm.go_EnCooperationPage().check_en_cooperation_button()
        assertUtils.assert_equals(text, 'Please select your cooperation model')
