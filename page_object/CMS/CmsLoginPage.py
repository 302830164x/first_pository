from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.CmsIndexPage import CmsIndexPage

sekorm = Element('CmsElement')


class CmsLoginPage(BasePage):
    """登录页类"""

    def cms_login_input(self, username, password):
        """输入内容,点击按钮"""
        self.input_text(sekorm['账号'], username)
        self.input_text(sekorm['密码'], password)
        self.is_click(sekorm['登录按钮'])

    def cms_login(self, username, password):
        """登录"""
        self.cms_login_input(username, password)
        return CmsIndexPage(self.driver)

    def cms_login_fail(self, username, password):
        """登录"""
        self.cms_login_input(username, password)
        return self.element_text(sekorm['登录失败'])

    def get_cms_login_text(self):
        """获取对应元素文本"""
        return self.element_text(sekorm['后台登录页'])
