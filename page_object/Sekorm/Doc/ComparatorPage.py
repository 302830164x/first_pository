from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '对照表标题': ('xpath', "//p[@class='reference-title']"),
    '搜索输入框': ('xpath', "//input[@id='reference-keyword']"),
    '搜索按钮': ('xpath', "//input[@id='search-btn']"),
    '对照表表头': ('xpath', "//tr[@id='table-head']"),
    '对照表表格': ('xpath', "//table[@id='tbody']//tr"),
    '对照表表格提示': ('xpath', "//p[@id='search-tip']"),
}


class ComparatorPage(BasePage):
    """对照表详情页"""

    def check_comparator_layout(self):
        """检查对照表详情页模块"""
        self.move_to_element(Locator['搜索输入框'])
        self.move_to_element(Locator['搜索按钮'])
        self.move_to_element(Locator['对照表表头'])
        title = self.element_text(Locator['对照表标题'])
        text = self.element_text(Locator['对照表表格提示'])
        num = self.elements_num(Locator['对照表表格'])
        return title, text, num

    def comparator_search(self, text):
        """检查对照表详情页搜索"""
        self.input_text(Locator['搜索输入框'], text)
        sleep()
        self.is_click(Locator['搜索按钮'])
        return self.elements_num(Locator['对照表表格'])
