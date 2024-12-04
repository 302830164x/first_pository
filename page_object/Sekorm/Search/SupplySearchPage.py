from page.basepage import BasePage
from page_object.Sekorm.Service.AskPricePage import AskPricePage
from page_object.Sekorm.Service.AskTimePage import AskTimePage
from page_object.Sekorm.Service.FuturesPage import FuturesPage
from page_object.Sekorm.Service.SampleApplicationPage import SampleApplicationPage
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
    '小量快购': ('xpath', "//a[@class='supply-btn js-quick-buy'][contains(text(),'小量快购')]"),
    '购买': ('xpath', "//a[@class='supply-btn js-quick-buy'][contains(text(),'购买')]"),
    '样品申请': ('xpath', "//a[@class='supply-btn js_apply_sample'][contains(text(),'样品申请')]"),
    '批量询价': ('xpath', "//a[@class='supply-btn js-ask-price'][contains(text(),'批量询价')]"),
    '交期查询': ('xpath', "//a[@class='supply-btn js-delivery'][contains(text(),'交期查询')]"),
    '期货订购': ('xpath', "//a[@class='supply-btn js-futures-ordering'][contains(text(),'期货订购')]"),
}


class SupplySearchPage(BasePage):
    """电子商城搜索结果页"""

    def get_search_text(self):
        return self.get_attribute_value(Locator['搜索词'], 'value')

    def supply_search_submit_order(self):
        """从商城提交订单"""
        self.move_to_element(Locator['购买'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['购买'], 'data-powertip')
        self.is_click(Locator['购买'])
        return text, ShopServicePage(self.driver)

    def check_supply_search_sample(self):
        """检查电子商城搜索结果页样品申请服务按钮"""
        self.move_to_element(Locator['样品申请'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['样品申请'], 'data-powertip')
        self.is_click(Locator['样品申请'])
        return text, SampleApplicationPage(self.driver)

    def check_supply_search_ask_price(self):
        """检查电子商城搜索结果页 批量询价 服务按钮"""
        self.move_to_element(Locator['批量询价'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['批量询价'], 'data-powertip')
        self.is_click(Locator['批量询价'])
        return text, AskPricePage(self.driver)

    def check_supply_search_ask_time(self):
        """检查电子商城搜索结果页 交期查询 服务按钮"""
        self.move_to_element(Locator['交期查询'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['交期查询'], 'data-powertip')
        self.is_click(Locator['交期查询'])
        return text, AskTimePage(self.driver)

    def check_supply_search_futures(self):
        """检查电子商城搜索结果页 期货订购 服务按钮"""
        self.move_to_element(Locator['期货订购'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['期货订购'], 'data-powertip')
        self.is_click(Locator['期货订购'])
        self.switch_window()
        return text, FuturesPage(self.driver)
