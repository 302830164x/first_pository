from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnServiceCommPage import EnServiceCommPage


Locator = {
    '提示语': ('xpath', "//div[@class='supply-tips']"),
    '发送到邮箱': ('xpath', "//ul[@class='last clearfix']//li[1]"),
    '分享弹窗-标题': ('xpath', "//h3[normalize-space()='Send to email']"),
    '分享弹窗-邮箱': ('xpath', "//input[@id='email']"),
    '分享弹窗-确认按钮': ('xpath', "//button[normalize-space()='Yes']"),
    '分享弹窗-关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),

    '型号': ('xpath', "//h1[@id='supply_detail']"),
    '品牌': ('xpath', "//div[@class='details-brand']"),
    '品牌Logo': ('xpath', "//div[@class='details-brand']//img"),
    '描述': ('xpath', "//p[@class='detail-ct-descMain']"),
    '供应商': ('xpath', "//div[@id='js_supply_module']//div[@class='on-brand-name']"),
    '标签': ('xpath', "//div[@class='supply-detail-quality supply-quality clearfix']"),
    '商城仓库': ('xpath', "//span[contains(text(),'Ship-From：')]"),
    '商城现货': ('xpath', "//span[contains(text(),'In Stock')]"),
    '商城交期': ('xpath', "//span[contains(text(),'EDD')]"),
    '商城价格': ('xpath', "//span[@class='information-title on_text']"),
    'RFQ': ('xpath', "//a[normalize-space()='RFQ']"),
    'Buy': ('xpath', "//a[normalize-space()='Buy']"),

    '规格参数': ('xpath', "//div[@class='space-table']//h3"),
    '订货型号': ('xpath', "//table[@id='supply-detail-table']//tr[1]/td[2]"),
    '规格参数-品牌': ('xpath', "//table[@id='supply-detail-table']//tr[2]/td[2]"),
    '型号系列': ('xpath', "//table[@id='supply-detail-table']//tr[3]/td[2]"),
    '品类': ('xpath', "//table[@id='supply-detail-table']//tr[4]/td[2]"),

    '资料下载': ('xpath', "//div[@class='mt15']//h3"),
    '资料标题': ('xpath', "//a[@class='item_title ']"),
    '预览按钮': ('xpath', "//a[contains(text(),'Preview')]"),
    'PDF预览组件': ('xpath', "//div[@id='viewer']"),
    '预览页下载按钮': ('xpath', "//a[normalize-space()='Download']"),
    '下载按钮': ('xpath', "//a[contains(text(),'Download')]"),

    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '登录提示': ('xpath', "//p[@class='form-error-msg']"),
    '登录弹窗关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),

}


class EnOnPage(BasePage):
    """英文站ON详情页"""

    def check_en_on_layout(self):
        """检查英文站ON详情页"""
        self.move_to_element(Locator['型号'])
        self.move_to_element(Locator['品牌'])
        self.move_to_element(Locator['规格参数'])
        self.move_to_element(Locator['资料下载'])
        return self.element_text(Locator['提示语'])

    def check_en_on_info(self):
        """检查英文站ON详情页ON的各字段信息"""
        self.move_to_element(Locator['品牌Logo'])
        self.move_to_element(Locator['描述'])
        self.move_to_element(Locator['供应商'])
        self.move_to_element(Locator['标签'])
        self.move_to_element(Locator['商城仓库'])
        self.move_to_element(Locator['商城现货'])
        self.move_to_element(Locator['商城交期'])
        self.move_to_element(Locator['订货型号'])
        self.move_to_element(Locator['规格参数-品牌'])
        self.move_to_element(Locator['型号系列'])
        self.move_to_element(Locator['品类'])
        return self.element_text(Locator['型号'])

    def unlogin_click_en_on(self, elm):
        """ON详情页未登录点击"""
        self.is_click(Locator[elm])
        self.is_click(Locator['登录按钮'])
        text = self.element_text(Locator['登录提示'])
        self.is_click(Locator['登录弹窗关闭按钮'])
        return text

    def check_on_RFQ(self):
        """ON详情页 RFQ服务"""
        self.move_to_element(Locator['RFQ'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['RFQ'], 'data-powertip')
        self.is_click(Locator['RFQ'])
        return text, EnServiceCommPage(self.driver)

    def login_click_Buy(self):
        """ON详情页 Buy服务"""
        self.is_click(Locator['Buy'])
        from page_object.Sekorm.EnSekrom.EnShopServicePage import EnShopServicePage
        return EnShopServicePage(self.driver)

    def login_click_Share(self):
        """ON详情页 分享"""
        self.is_click(Locator['发送到邮箱'])
        text1 = self.element_text(Locator['分享弹窗-标题'])
        text2 = self.get_attribute_value(Locator['分享弹窗-邮箱'], 'value')
        self.move_to_element(Locator['分享弹窗-确认按钮'])
        self.is_click(Locator['分享弹窗-关闭按钮'])
        return text1, text2

    def login_click_Preview(self):
        """ON详情页 预览资料"""
        self.move_to_element(Locator['资料标题'])
        self.is_click(Locator['预览按钮'])
        self.switch_window()
        self.move_to_element(Locator['PDF预览组件'])
        self.move_to_element(Locator['预览页下载按钮'])
