from page.basepage import BasePage
from common.readelement import Element
from page_object.Openeco.OpenecoIndexPage import OpenecoIndexpage

sekorm = Element('OpenecoElement')


class OpenecoLoginPage(BasePage):
    '''业务伙伴平台登录页'''

    def openeco_login(self, username, password):
        self.input_text(sekorm['账号'], username)
        self.input_text(sekorm['密码'], password)
        self.is_click(sekorm['登录按钮'])
        return OpenecoIndexpage(self.driver)

    def openeco_login_fail(self, username, password):
        self.input_text(sekorm['登录'], username)
        self.input_text(sekorm['密码'], password)
        return self.element_text(sekorm['登录失败'])


