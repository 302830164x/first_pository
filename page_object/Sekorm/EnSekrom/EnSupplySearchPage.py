from page_object.Sekorm.EnSekrom.EnOnPage import EnOnPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage
from page_object.Sekorm.EnSekrom.EnServiceCommPage import EnServiceCommPage
from page_object.Sekorm.EnSekrom.EnShopServicePage import EnShopServicePage
from page_object.Sekorm.SekormCommon import SekormCommon

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
    '搜索结果总数': ('xpath', "//div[@class='search-result-title']"),
    '品牌墙': ('xpath', "//div[@id='content']//a[1]//img[1]"),
    '型号': ('xpath', "//a[contains(@class,'model-on')]"),
    '厂牌': ('xpath', "//a[@class='model-brand supply_model_brand']"),
    'Documents': ('xpath', "//p[@class='research-data']/a"),
    '描述': ('xpath', "//div[@class='supply-desc']"),
    '供应商': ('xpath', "//div[@class='supply-quality-wrap']"),
    '价格': ('xpath', "//p[@class='clearfix has-enUnitPrice']"),
    '库存': ('xpath', "//p[@class='clearfix has-Stock']"),
    '仓库': ('xpath', "//span[@class='information-title pull-left'][normalize-space()='Ship-From']"),
    '预计交期': ('xpath', "//span[@class='information-title information-tips-title clearfix']"),
    'Buy': ('xpath', "//a[contains(text(),'Buy')]"),
    'RFQ': ('xpath', "//a[contains(text(),'RFQ')]"),

    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '登录提示': ('xpath', "//p[@class='form-error-msg']"),
    '登录弹窗关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),
}


class EnSupplySearchPage(SekormCommon):
    """英文站商城垂搜结果页"""

    def get_search_text(self):
        """获取搜索框搜索词"""
        return self.get_attribute_value(Locator['搜索词'], 'value')

    def check_en_supply_search_layout(self):
        """检查搜索结果页布局"""
        self.move_to_element(Locator['搜索结果总数'])
        self.move_to_element(Locator['品牌墙'])
        self.move_to_element(Locator['型号'])
        self.move_to_element(Locator['厂牌'])
        self.move_to_element(Locator['Documents'])
        self.move_to_element(Locator['描述'])
        self.move_to_element(Locator['供应商'])
        self.move_to_element(Locator['价格'])
        self.move_to_element(Locator['库存'])
        self.move_to_element(Locator['仓库'])
        self.move_to_element(Locator['预计交期'])
        self.move_to_element(Locator['Buy'])
        self.move_to_element(Locator['RFQ'])

    def check_en_supply_search_num(self):
        """检查搜索结果条数"""
        return self.elements_num(Locator['型号'])

    def click_en_supply_search_right_brand(self):
        """点击检查搜索结果页品牌墙"""
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_en_supply_search_on(self, elm):
        """点击检查搜索结果页ON型号"""
        self.is_click(Locator[elm])
        self.switch_window()
        return EnOnPage(self.driver)

    def click_en_supply_search_on_brand(self):
        """点击检查搜索结果页ON厂牌"""
        self.is_click(Locator['厂牌'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def check_en_supply_search_RFQ(self):
        """搜索结果页 RFQ服务"""
        self.move_to_element(Locator['RFQ'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['RFQ'], 'data-powertip')
        self.is_click(Locator['RFQ'])
        return text, EnServiceCommPage(self.driver)

    def unlogin_click_en_on_buy(self):
        """搜索结果页未登录点击"""
        self.is_click(Locator['Buy'])
        self.is_click(Locator['登录按钮'])
        text = self.element_text(Locator['登录提示'])
        self.is_click(Locator['登录弹窗关闭按钮'])
        return text

    def login_click_en_on_buy(self):
        """登录点击Buy"""
        self.is_click(Locator['Buy'])
        return EnShopServicePage(self.driver)