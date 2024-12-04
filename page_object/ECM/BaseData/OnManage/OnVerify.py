from common.readelement import Element
from page.basepage import BasePage

sekorm = Element('EcmElement')


class OnVerify(BasePage):
    """ON待审核"""

    def select_search(self):
        """
        筛选框校验
        """
        self.is_click(sekorm['ON待审核-搜索框-品牌'])
        self.is_click(sekorm['ON待审核-搜索框-LAIRD'])
        self.is_click(sekorm['ON待审核-搜索框-语言'])
        self.is_click(sekorm['ON待审核-搜索框-中文'])
        self.is_click(sekorm['ON待审核-检索按钮'])

