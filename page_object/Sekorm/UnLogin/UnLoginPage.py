from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '未登录窗口-关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),
    '所属国家/地区': ('xpath', "//label[contains(text(),'所属国家/地区')]"),
    '地区选项': ('xpath', "//input[@value='中国 86']"),
    '手机号': ('xpath', "//input[@id='userName']"),
    '密码': ('xpath', "//input[@id='passwordTxt']"),
    '短信验证码': ('xpath', "//input[@id='mobileCode']"),
    '获取验证码': ('xpath', "//a[@id='get_code']"),
    '协议勾选': ('xpath', "//i[@class='icon-agree-circle']"),
    '使用许可协议': ('xpath', "//a[@id='loginLicenseMap']"),
    '隐私协议': ('xpath', "//a[@id='loginPrivacyMap']"),
    '出口协议': ('xpath', "//a[@id='loginExportMap']"),
    '登录/注册按钮': ('xpath', "//input[@id='btn_login']"),
    '密码登录': ('xpath', "//a[@class='pwd-login']"),
    '注册提示': ('xpath', "//p[@id='auto_register_hint']"),
    '忘记密码': ('xpath', "//p[@id='forget_password']//a"),
    '短信登录': ('xpath', "//p[@id='code_login']//a"),

    '登录按钮': ('xpath', "//a[contains(text(),'登录')]"),
    '注册按钮': ('xpath', "//a[contains(text(),'注册')]"),
}


class UnLoginPage(BasePage):
    """未登录-登录弹窗"""

    def close_login(self):
        """关闭登录弹窗"""
        text = self.element_text(Locator['所属国家/地区'])
        self.is_click(Locator['未登录窗口-关闭按钮'])
        return text

    def check_login_layout(self):
        """检查登录页面布局"""
        self.move_to_element(Locator['所属国家/地区'])
        self.move_to_element(Locator['地区选项'])
        self.move_to_element(Locator['手机号'])
        self.move_to_element(Locator['短信验证码'])
        self.move_to_element(Locator['获取验证码'])
        self.move_to_element(Locator['协议勾选'])
        self.move_to_element(Locator['使用许可协议'])
        self.move_to_element(Locator['隐私协议'])
        self.move_to_element(Locator['出口协议'])
        self.move_to_element(Locator['登录/注册按钮'])
        self.move_to_element(Locator['注册提示'])
        self.is_click(Locator['密码登录'])
        self.move_to_element(Locator['手机号'])
        self.move_to_element(Locator['密码'])
        self.move_to_element(Locator['协议勾选'])
        self.move_to_element(Locator['使用许可协议'])
        self.move_to_element(Locator['隐私协议'])
        self.move_to_element(Locator['出口协议'])
        self.move_to_element(Locator['登录/注册按钮'])
        self.move_to_element(Locator['忘记密码'])
        self.is_click(Locator['短信登录'])
        return self.element_text(Locator['注册提示'])
