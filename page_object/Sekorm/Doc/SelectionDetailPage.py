from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '选型表标题': ('xpath', "//p[@class='reference-title']"),
    '厂牌LOGO': ('xpath', "//img[@id='selection-image']"),
    '厂牌介绍': ('xpath', "//span[@id='selection-description']"),
    '搜索输入框': ('xpath', "//input[@id='selection-keyword']"),
    '搜索按钮': ('xpath', "//input[@id='search-btn']"),
    '选型表表头': ('xpath', "//tr[@id='table-head']//p"),
    '选型表表格': ('xpath', "//tr[@class='selection-item-tr']"),
    '全屏按钮': ('xpath', "//div[@id='fullScreen']"),
    '编辑按钮': ('xpath', "//div[@id='selectColumn']"),
    '产品型号名称': ('xpath', "//td[@data-pnid]//span"),
    '品类': ('xpath', "//tr[@id='table-head']//p[contains(text(),'品类')]"),
    '加入型号清单按钮': ('xpath', "//em[@id='selection-collect']"),

    '退出全屏按钮': ('xpath', "//div[@id='noFullScreen']"),
    '编辑表头选项': ('xpath', "//input[@id='品类']"),
    '关闭编辑按钮': ('xpath', "//span[@class='modal-closeBtn']"),
}


class SelectionDetailPage(BasePage):
    """选型表详情页"""

    def check_SelectionDetailPage_layout(self):
        """检查选型表详情页"""
        for i, elm in enumerate(Locator):
            if i < 12:
                self.move_to_element(Locator[elm])
        text = self.element_text(Locator['选型表标题'])
        size = self.img_show(Locator['厂牌LOGO'])
        return text, size

    def check_fullScreen(self):
        """检查全屏按钮"""
        self.is_click(Locator['全屏按钮'])
        num = self.elements_num(Locator['选型表表格'])
        self.is_click(Locator['退出全屏按钮'])
        return num

    def check_selection_search(self, text):
        """检查选型表搜索"""
        num1 = self.elements_num(Locator['选型表表格'])
        self.input_text(Locator['搜索输入框'], text)
        self.is_click(Locator['搜索按钮'])
        sleep()
        num2 = self.elements_num(Locator['选型表表格'])
        return num1, num2

    def check_selection_edit(self):
        """检查编辑"""
        num1 = self.elements_num(Locator['选型表表头'])
        self.is_click(Locator['编辑按钮'])
        self.is_click(Locator['编辑表头选项'])
        self.is_click(Locator['关闭编辑按钮'])
        num2 = self.elements_num(Locator['选型表表头'])
        return num1, num2
