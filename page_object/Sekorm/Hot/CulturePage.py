from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '标志LOGO1': ('xpath', "//img[@src='//www.sekorm.com/front/website/images/information/company_culture.png']"),
    '标志LOGO2': ('xpath', "//img[@src='//www.sekorm.com/front/website/images/information/sekorm_text.png']"),
    '文本': ('xpath', "//div[@class='pull-left about-culture-text']//ul//li//p"),
}


class CulturePage(BasePage):
    """文化与愿景"""

    def check_CulturePage(self):
        """检查页面图片是否正常显示"""
        self.move_to_element(Locator['标志LOGO1'])
        self.move_to_element(Locator['标志LOGO2'])
        text = self.element_text(Locator['文本'])
        return text
