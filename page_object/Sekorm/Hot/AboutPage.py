from page.basepage import BasePage

Locator = {
    '团队合照1': ('xpath', "//img[@class='about-us-intro-icon1']"),
    '团队合照2': ('xpath', "//img[@class='about-us-intro-icon2']"),
    '团队合照3': ('xpath', "//img[@class='about-us-intro-icon3']"),
    '厂牌LOGO': ('xpath', "//div[@id='content']//li[1]//a[1]//img[1]"),
    '高亮文本': ('xpath', "//span[@class='item-active']"),
}


class AboutPage(BasePage):
    """公司简介"""

    def check_AboutPage(self):
        """检查页面图片是否正常显示"""
        self.move_to_element(Locator['团队合照1'])
        self.move_to_element(Locator['团队合照2'])
        self.move_to_element(Locator['团队合照3'])
        size = self.img_show(Locator['厂牌LOGO'])
        text = self.element_text(Locator['高亮文本'])
        return size, text
