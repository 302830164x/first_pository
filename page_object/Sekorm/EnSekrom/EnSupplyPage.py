from page_object.Sekorm.EnSekrom.EnOnPage import EnOnPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage
from page_object.Sekorm.EnSekrom.EnServiceCommPage import EnServiceCommPage
from page_object.Sekorm.EnSekrom.EnShopServicePage import EnShopServicePage
from page_object.Sekorm.SekormCommon import SekormCommon

Locator = {
    'banner图': ('xpath', "//div[@class='swiper-container']"),
    '标语': ('xpath', "//div[@class='ecSupply-tips']/a"),

    '型号': ('xpath', "//a[contains(@class,'model-on')]"),
    '厂牌': ('xpath', "//a[@class='model-brand']"),
    'Documents': ('xpath', "//p[@class='research-data']/a"),
    '描述': ('xpath', "//div[@class='supply-desc']"),
    '供应商': ('xpath', "//div[@class='supply-quality-wrap']"),
    '价格': ('xpath', "//span[@data-unitprice]"),
    '库存': ('xpath', "//span[@data-instock]"),
    '仓库': ('xpath', "//span[contains(@class,'pay-local-content')]"),
    '预计交期': ('xpath', "//span[@data-delivery]"),
    'Buy': ('xpath', "//a[contains(text(),'Buy')]"),
    'RFQ': ('xpath', "//a[contains(text(),'RFQ')]"),

    '授权品牌': ('xpath', "(//div[@id='co_company_list'])[1]//img"),
    '生态伙伴': ('xpath', "(//div[@id='co_company_list'])[2]//img"),
    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '登录提示': ('xpath', "//p[@class='form-error-msg']"),
    '登录弹窗关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),
}


class EnSupplyPage(SekormCommon):
    """英文站商城页"""

    def check_en_supply_layout(self):
        """检查英文站商城布局"""
        self.move_to_element(Locator['banner图'])
        self.move_to_element(Locator['型号'])
        self.move_to_element(Locator['厂牌'])
        self.move_to_element(Locator['Documents'])
        self.move_to_element(Locator['描述'])
        self.move_to_element(Locator['供应商'])
        # self.move_to_element(Locator['价格'])
        self.move_to_element(Locator['库存'])
        self.move_to_element(Locator['仓库'])
        self.move_to_element(Locator['预计交期'])
        return self.element_text(Locator['标语'])

    def check_en_supply_img(self):
        """检查图片是否显示正常"""
        size1 = self.img_show(Locator['授权品牌'])
        size2 = self.img_show(Locator['生态伙伴'])
        return size1, size2

    def click_en_supply_on(self, elm):
        """点击ON名称"""
        self.is_click(Locator[elm])
        self.switch_window()
        return EnOnPage(self.driver)

    def click_en_supply_brand(self, elm):
        """点击ON厂牌"""
        self.is_click(Locator[elm])
        self.switch_window()
        return EnSearchPage(self.driver)

    def check_en_supply_RFQ(self):
        """RFQ服务"""
        self.move_to_element(Locator['RFQ'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['RFQ'], 'data-powertip')
        self.is_click(Locator['RFQ'])
        return text, EnServiceCommPage(self.driver)

    def unlogin_click_en_supply_buy(self):
        """未登录点击Buy"""
        self.is_click(Locator['Buy'])
        self.is_click(Locator['登录按钮'])
        text = self.element_text(Locator['登录提示'])
        self.is_click(Locator['登录弹窗关闭按钮'])
        return text

    def login_click_en_supply_buy(self):
        """登录点击Buy"""
        self.is_click(Locator['Buy'])
        return EnShopServicePage(self.driver)
