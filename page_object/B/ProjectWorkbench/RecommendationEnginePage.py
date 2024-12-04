from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '输入框': ('xpath', "//input[@id='searchValue']"),
    '搜索按钮': ('xpath', "//button[@type='submit']"),
    '列表': ('xpath', "//div[@class='lazy-builder-item']"),
    '多选框': ('xpath', "//div[@class='ant-select-selection__placeholder']"),
    '推荐型号': ('xpath', "//li[@role='option'][text()='推荐型号']"),
}


class RecommendationEnginePage(BasePage):
    """优选型号推荐"""

    def get_RecommendationEnginePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])

    def RecommendationEnginePage_search(self, text):
        """搜索"""
        self.input_text(Locator['输入框'], text)
        sleep()
        self.is_click(Locator['搜索按钮'])
        sleep(3)
        return self.get_RecommendationEnginePage_num()

    def RecommendationEnginePage_select(self):
        """选中多选项"""
        self.js_click(Locator['多选框'])
        self.mouse_click(Locator['推荐型号'])
        return self.elements_num(Locator['列表'])

