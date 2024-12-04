from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.EcmIndexPage import EcmIndexPage

sekorm = Element('EcmElement')


class EcmLoginPage(BasePage):
    """登录页类"""

    def ecm_login_input(self, username, password):
        self.input_text(sekorm['账号'], username)
        self.input_text(sekorm['密码'], password)
        self.is_click(sekorm['登录按钮'])

    def ecm_login(self, username, password):
        """输入内容"""
        self.ecm_login_input(username, password)
        return EcmIndexPage(self.driver)

    def ecm_login_fail(self, username, password):
        """输入内容"""
        self.ecm_login_input(username, password)
        return self.element_text(sekorm['登录失败'])

    def get_ecm_login_text(self):
        """获取对应元素文本"""
        return self.element_text(sekorm['后台首页'])
