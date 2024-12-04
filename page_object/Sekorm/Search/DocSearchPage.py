from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '搜索词': ('xpath', "//input[@id='searchWord']"),
}


class DocSearchPage(BasePage):
    """技术资料垂直搜索结果页"""

    def get_search_text(self):
        return self.get_attribute_value(Locator['搜索词'], 'value')
