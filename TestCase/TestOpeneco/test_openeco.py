import allure
import pytest
from common.readconfig import ini
from utils.assertUtils import assertUtils
from time import sleep

@allure.epic('合作伙伴平台')
@allure.feature('合作伙伴平台检查')
class Test_Openeco():

    @pytest.fixture(autouse=True)
    def set_openeco_driver(self, openeco_driver):
        self.openeco = openeco_driver
        self.openeco.get_url(f'{ini.Openeco_Url}/content/sums/userCenter')

    @allure.story('首页')
    def test_go_shouye(self):
        text = self.openeco.go_openeco_index().get_bubble_text()
        assert_text = '您的关键词标签，帮助您获得精准信息'
        assertUtils.assert_equals(text, assert_text)
        self.openeco.click_editbutton()

    @allure.story('项目推送')
    def test_go_projectpush(self):
        projectpush = self.openeco.go_projectpush()
        text = projectpush.get_filter_value()
        assert_text = '推送给我的需求'
        assertUtils.assert_equals(text, assert_text)
        projectpush.click_select()
