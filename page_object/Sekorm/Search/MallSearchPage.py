from page.basepage import BasePage
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
    '购买': ('xpath', "//a[contains(@class,'supply-btn')][contains(text(),'购买')]"),
}


class MallSearchPage(BasePage):
    """现货市场搜索结果页"""

    def get_search_text(self):
        return self.get_attribute_value(Locator['搜索词'], 'value')

    def mall_search_submit_order(self):
        """从商城提交订单"""
        self.move_to_element(Locator['购买'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['购买'], 'data-powertip')
        self.is_click(Locator['购买'])
        return text, ShopServicePage(self.driver)
