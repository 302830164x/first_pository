from page_object.Sekorm.SekormCommon import SekormCommon

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
    '搜索结果总数': ('xpath', "//div[@class='search-result-title']"),
    '搜索结果标题': ('xpath', "//a[@class='item_title']"),
    '品牌墙': ('xpath', "//div[@id='content']//a[1]//img[1]"),
    '商城模块': ('xpath', "//p[@class='title']//span"),
    '商城模块-型号': ('xpath', "//div[@id='searchRightSupply-mall']//a[@class='searchRightSupply-item-on']"),
    '商城模块-厂牌': ('xpath', "//p[@class='searchSupply-msg searchSupply-brand']"),
    '商城模块-厂牌LOGO': ('xpath', "//p[@class='searchSupply-msg searchSupply-brand']//img"),
    '商城模块-品类': ('xpath', "//p[@class='searchSupply-msg searchSupply-goodList']"),
    '商城模块-价格': ('xpath', "//div[@id='searchRightSupply-mall']//p[@class='searchSupply-msg']"),
    '商城模块-库存': ('xpath', "//p[@id='searchSupply-supplyFmt']"),
    '商城模块-Buy': ('xpath', "//a[@class='supply-btn '][contains(text(),'Buy')]"),
    '商城模块-RFQ': ('xpath', "//a[@class='supply-btn '][contains(text(),'RFQ')]"),
    '商城模块-More': ('xpath', "//a[normalize-space()='More']"),
}


class EnSearchPage(SekormCommon):
    """英文站搜索结果页"""

    def get_search_text(self):
        """获取搜索框搜索词"""
        return self.get_attribute_value(Locator['搜索词'], 'value')

    def check_en_search_layout(self):
        """检查搜索结果页布局"""
        self.move_to_element(Locator['搜索结果总数'])
        self.move_to_element(Locator['搜索结果标题'])
        self.move_to_element(Locator['品牌墙'])
        self.move_to_element(Locator['商城模块'])

    def check_en_search_on(self):
        """检查搜索结果页商城模块信息"""
        self.move_to_element(Locator['商城模块-型号'])
        self.move_to_element(Locator['商城模块-厂牌'])
        self.move_to_element(Locator['商城模块-厂牌LOGO'])
        self.move_to_element(Locator['商城模块-品类'])
        self.move_to_element(Locator['商城模块-价格'])
        self.move_to_element(Locator['商城模块-库存'])
        self.move_to_element(Locator['商城模块-Buy'])
        self.move_to_element(Locator['商城模块-RFQ'])

    def check_en_search_num(self):
        """检查搜索结果页条数"""
        return self.elements_num(Locator['搜索结果标题'])

    def click_en_search_right_brand(self):
        """点击检查搜索结果页品牌墙"""
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return EnSearchPage(self.driver)

    def click_en_search_title(self):
        """点击检查搜索结果页文章标题"""
        from page_object.Sekorm.EnSekrom.EnDocDetailPage import EnDocDetailPage
        self.is_click(Locator['搜索结果标题'])
        self.switch_window()
        return EnDocDetailPage(self.driver)

    def click_en_search_on(self, elm):
        """点击商城模块"""
        self.is_click(Locator[elm])
        self.switch_window()
        from page_object.Sekorm.EnSekrom.EnSupplySearchPage import EnSupplySearchPage
        return EnSupplySearchPage(self.driver)
