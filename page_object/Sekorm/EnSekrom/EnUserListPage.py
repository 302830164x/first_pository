from page.basepage import BasePage
from page_object.Sekorm.EnSekrom.EnShopServicePage import EnShopServicePage

Locator = {
    '商城名称': ('xpath', "//span[@class='shop-name']"),
    '型号': ('xpath', "//a[@class='model-on']"),
    '厂牌': ('xpath', "//a[@class='model-brand']"),
    '描述': ('xpath', "//div[@class='supply-desc text-left']"),
    '仓库': ('xpath', "//span[@class='pay-local-content']"),
    '单价': ('xpath', "//span[@class='trade-price-content']"),
    '购买数量': ('xpath', "//input[@type='text']"),
    '型号小计': ('xpath', "//span[@class='sub-total information-content']"),
    '订单小计': ('xpath', "//p[@id='totalInfo']"),
    '勾选按钮': ('xpath', "//td[@class='text-left']//i[@class='icon-checkbox']"),
    '删除按钮': ('xpath', "//img[@class='trade-delete-img-icon']"),
    '删除提示': ('xpath', "//div[@class='modal-body-info']"),
    '关闭提示': ('xpath', "//span[@class='modal-closeBtn']"),
    'Remove Selected': ('xpath', "//span[@id='deleteSelective']"),
    'Check Out': ('xpath', "//button[@id='toSettle']"),
}


class EnUserListPage(BasePage):
    """英文站购物车"""

    def check_en_user_list_layout(self):
        """检查英文站购物车布局"""
        self.move_to_element(Locator['商城名称'])
        self.move_to_element(Locator['型号'])
        self.move_to_element(Locator['订单小计'])
        self.move_to_element(Locator['勾选按钮'])
        self.move_to_element(Locator['删除按钮'])
        self.move_to_element(Locator['Remove Selected'])
        return self.element_text(Locator['Check Out'])

    def click_en_list_delete(self, elm):
        """点击购物车移除按钮"""
        self.is_click(Locator[elm])
        text = self.element_text(Locator['删除提示'])
        self.is_click(Locator['关闭提示'])
        return text

    def click_en_check_out(self):
        """英文站购物车结算"""
        self.is_click(Locator['Check Out'])
        return EnShopServicePage(self.driver)
