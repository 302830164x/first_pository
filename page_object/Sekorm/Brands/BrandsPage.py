from common.readelement import Element
from page.basepage import BasePage
from page_object.Sekorm.Search.BrandSearchPage import BrandSearchPage
from page_object.Sekorm.SekormCommon import SekormCommon
from utils.times import sleep

sekorm = Element('SekormElement')
Locator = {
    '代理厂牌列表': ('xpath', "//div[@data-brand]"),
    '厂牌LOGO': ('xpath', "//div[@data-brand]//img"),
    '厂牌介绍': ('xpath', "//div[@data-brand]//a[@class=' read_more']"),
    '厂牌搜索关键词': ('xpath', "//a[@class='brand-tag brand_search_tag']"),
    '厂牌授权代理商': ('xpath', "//span[@class='supplier-name']"),
    '厂牌-线上商城': ('xpath', "//span[@class='brand-service-item'][contains(text(),'线上商城')]"),
    '厂牌-技术资料': ('xpath', "//span[@class='brand-service-item'][contains(text(),'技术资料')]"),
}


class BrandsPage(SekormCommon):
    """代理品牌"""

    def go_BrandSearchPage(self, text):
        self.input_text(sekorm['搜索框'], text)
        self.is_click(sekorm['搜索按钮'])
        return BrandSearchPage(self.driver)

    def check_BrandsPage(self):
        num1 = self.elements_num(Locator['代理厂牌列表'])
        size = self.img_show(Locator['厂牌LOGO'])
        self.move_to_element(Locator['厂牌介绍'])
        self.move_to_element(Locator['厂牌搜索关键词'])
        self.move_to_element(Locator['厂牌授权代理商'])
        self.move_to_element(Locator['厂牌-线上商城'])
        self.move_to_element(Locator['厂牌-技术资料'])
        self.next_page(False)
        sleep()
        num2 = self.elements_num(Locator['代理厂牌列表'])
        return num1, num2, size
