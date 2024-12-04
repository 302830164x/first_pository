from page_object.Sekorm.Search.BrandSearchPage import BrandSearchPage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage
from page_object.Sekorm.Supply.OnPage import OnPage
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.times import sleep

Locator = {
    '供应商': ('xpath', "//p[@class='supply-supplier']"),
    '轮播图': ('xpath', "//img[@alt='折扣市场广告Banner图片']"),
    '授权代理品牌': ('xpath', "(//div[@id='co_company_list'])[1]//li//img"),
    '生态合作伙伴': ('xpath', "(//div[@id='co_company_list'])[2]//li//img"),
    '提示文案': ('xpath', "//div[contains(@class,'tips-content')]"),
    '购买': ('xpath', "//a[contains(@class,'supply-btn')][contains(text(),'购买')]"),
}


class MallPage(SekormCommon):
    """现货市场"""

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

    def get_tips_text(self):
        """获取轮播图下的提示文案"""
        return self.element_text(Locator['提示文案'])

    def check_mall_supplier(self):
        """检查供应商/品质保证"""
        self.move_to_element(Locator['供应商'])
        return self.elements_num(Locator['供应商'])

    def mall_submit_order(self):
        """从商城提交订单"""
        self.move_to_element(Locator['购买'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['购买'], 'data-powertip')
        self.is_click(Locator['购买'])
        return text, ShopServicePage(self.driver)
