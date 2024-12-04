from page_object.Sekorm.Search.BrandSearchPage import BrandSearchPage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.Service.AskPricePage import AskPricePage
from page_object.Sekorm.Service.AskTimePage import AskTimePage
from page_object.Sekorm.Service.FuturesPage import FuturesPage
from page_object.Sekorm.Service.SampleApplicationPage import SampleApplicationPage
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage
from utils.times import sleep

Locator = {
    '供应商': ('xpath', "//p[@class='supply-supplier']"),
    '原厂认证': ('xpath', "(//p[@class='pull-left'][contains(text(),'原厂认证')])"),
    '世强自营': ('xpath', "(//p[@class='pull-left'][contains(text(),'世强自营')])"),
    '授权代理': ('xpath', "(//p[@class='pull-left'][contains(text(),'授权代理')])"),
    '一支起订': ('xpath', "(//p[@class='pull-left'][contains(text(),'一支起订')])"),
    '轮播图': ('xpath', "//img[@alt='beta_电商banner']"),
    '授权代理品牌': ('xpath', "(//div[@id='co_company_list'])[1]//li//img"),
    '生态合作伙伴': ('xpath', "(//div[@id='co_company_list'])[2]//li//img"),
    '小量快购': ('xpath', "//a[@class='supply-btn js-quick-buy'][contains(text(),'小量快购')]"),
    '购买': ('xpath', "//a[@class='supply-btn js-quick-buy'][contains(text(),'购买')]"),
    '样品申请': ('xpath', "//a[@class='supply-btn js_apply_sample'][contains(text(),'样品申请')]"),
    '批量询价': ('xpath', "//a[@class='supply-btn js-ask-price'][contains(text(),'批量询价')]"),
    '交期查询': ('xpath', "//a[@class='supply-btn js-delivery'][contains(text(),'交期查询')]"),
    '期货订购': ('xpath', "//a[@class='supply-btn js-futures-ordering'][contains(text(),'期货订购')]"),
}


class SupplyPage(SekormCommon):
    """电子商城"""

    def check_img(self, elm):
        """检查图片是否加载成功，返回图片尺寸，加载失败返回（0,0）"""
        return self.img_show(Locator[elm])

    def click_img(self, elm):
        """点击授权品牌、生态合作图片，跳转厂牌搜索结果页"""
        self.element_move_to_center(Locator[elm])
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return BrandSearchPage(self.driver)

    def check_supply_supplier(self):
        """检查供应商/品质保证"""
        self.move_to_element(Locator['原厂认证'])
        self.move_to_element(Locator['世强自营'])
        self.move_to_element(Locator['授权代理'])
        self.move_to_element(Locator['一支起订'])
        return self.element_text(Locator['供应商'])

    def supply_submit_order(self):
        """从商城提交订单"""
        self.move_to_element(Locator['购买'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['购买'], 'data-powertip')
        self.is_click(Locator['购买'])
        return text, ShopServicePage(self.driver)

    def check_supply_sample(self):
        """检查商城样品申请服务按钮"""
        self.move_to_element(Locator['样品申请'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['样品申请'], 'data-powertip')
        self.is_click(Locator['样品申请'])
        return text, SampleApplicationPage(self.driver)

    def check_supply_ask_price(self):
        """检查商城 批量询价 服务按钮"""
        self.move_to_element(Locator['批量询价'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['批量询价'], 'data-powertip')
        self.is_click(Locator['批量询价'])
        return text, AskPricePage(self.driver)

    def check_supply_ask_time(self):
        """检查商城 交期查询 服务按钮"""
        self.move_to_element(Locator['交期查询'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['交期查询'], 'data-powertip')
        self.is_click(Locator['交期查询'])
        return text, AskTimePage(self.driver)

    def check_supply_futures(self):
        """检查商城 期货订购 服务按钮"""
        self.move_to_element(Locator['期货订购'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['期货订购'], 'data-powertip')
        self.is_click(Locator['期货订购'])
        self.switch_window()
        return text, FuturesPage(self.driver)
