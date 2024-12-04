from page.basepage import BasePage

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
    '列表数据': ('xpath', "//div[@data-brand]"),
}


class BrandSearchPage(BasePage):
    """代理品牌搜索结果页"""

    def get_search_text(self):
        # 获取搜索框关键词
        return self.get_attribute_value(Locator['搜索词'], 'value')

    def if_brand_to_top(self):
        # 判断URL指定厂牌是否置顶
        text1 = self.get_attribute_value(Locator['列表数据'], 'data-brand')
        text2 = self.driver.current_url.split('=')[1]
        if text1 == text2:
            return True
        else:
            return False
