from random import sample

from common.readelement import Element
from page.basepage import BasePage
from page_object.Sekorm.News.NewsDetailPage import NewsDetailPage
from page_object.Sekorm.SekormCommon import SekormCommon

sekorm = Element('SekormElement')


class SearchPage(SekormCommon):
    """主搜搜索结果页"""

    def get_text_num(self, elem, text):
        """获取指定元素固定文本的个数"""
        return self.elements_text(sekorm[elem]).count(text)

    def get_type_text(self, elem):
        """获取指定元素固定文本的个数"""
        return self.elements_text(sekorm[elem])

    def get_selection_num(self, elem):
        """获取置顶选型器个数"""
        offset = 0
        for i in self.elements_text(sekorm[elem]):
            if offset > 0 and i != "选型表":
                return offset
            if i == "选型表":
                offset += 1
        return offset

    def get_element_num(self, elem):
        """获取相同元素的个数"""
        self.element_move_to_center(sekorm[elem])
        num = self.elements_num(sekorm[elem])
        return num

    def get_MFRProfile_detail(self, elem):
        """点击品牌介绍"""
        self.is_click(sekorm[elem])
        self.switch_window()
        return NewsDetailPage(self.driver)

    def click_MFRProfile_goods(self, elem):
        """点击品牌介绍品类品类"""
        text_list = []
        data = {}
        for i in self.elements_text(sekorm[elem]):
            for k in i.replace('\n查看更多', '').split(' '):
                text_list.append(k)
        for k in text_list:
            data.update({f'{elem}' + k: f'xpath==//a[text()="{k}"]'})
        sekorm.dump(data)
        for m in sample(text_list, 3):
            self.is_click(sekorm[f'{elem}' + m])
            yield self.get_source, m
            self.get_back()

    def get_search_text(self):
        """获取搜索框搜索词"""
        return self.get_attribute_value(sekorm['搜索词'], 'value')
