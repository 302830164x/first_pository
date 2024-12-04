from common.readelement import Element
from page.basepage import BasePage
from page_object.B.BIndexPage import BIndexPage

sekorm = Element('B_Element')


class BLoginPage(BasePage):
    """登录页"""

    def b_login_input(self, username, password):
        self.input_text(sekorm['账号'], username)
        self.input_text(sekorm['密码'], password)
        self.is_click(sekorm['登录按钮'])

    def b_login(self, username, password):
        """输入内容"""
        self.b_login_input(username, password)
        return BIndexPage(self.driver)

    def b_login_fail(self, username, password):
        """输入内容"""
        self.b_login_input(username, password)
        return self.element_text(sekorm['登录失败'])

    def get_b_login_text(self):
        """获取对应元素文本"""
        return self.element_text(sekorm['后台登录页'])
