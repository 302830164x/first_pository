from selenium.webdriver import Keys

from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//div[@class='lazy-builder-item']"),
    '多选框': ('xpath', "//div[@class='ant-select-selection__placeholder']"),
    '推荐型号': ('xpath', "//li[@role='option'][text()='推荐型号']"),
}


class PnRecommendationPage(BasePage):
    """优选型号推荐"""

    def get_PnRecommendationPage_num(self):
        """获取列表内容条数"""
        self.js_click(Locator['多选框'])
        self.mouse_click(Locator['推荐型号'])
        return self.elements_num(Locator['列表'])
