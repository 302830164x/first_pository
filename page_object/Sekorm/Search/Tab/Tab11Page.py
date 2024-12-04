from page.basepage import BasePage

Locator = {
    '搜索列表': ('xpath', "//div[@id='multiple-search_0']/div"),
    '合作页-Logo': ('xpath', "//div[@class='search-cooperate-banner']/img"),
}


class Tab11Page(BasePage):
    """tab=11的门楣"""

    def check_tab11_list_num(self):
        """检查tab11页面列表数据量"""
        return self.elements_num(Locator['搜索列表'])

    def check_img_show(self, elm):
        """检查tab11页面图片展示"""
        return self.img_show(Locator[elm])
