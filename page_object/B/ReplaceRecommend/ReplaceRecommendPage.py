from common.readelement import Element
from page.basepage import BasePage
from page_object.B.ReplaceRecommend.BusinessReplaceRecommendPage import BusinessReplaceRecommendPage
from page_object.B.ReplaceRecommend.NewReplaceRecommendPage import NewReplaceRecommendPage
from page_object.B.ReplaceRecommend.NotPassedReplaceRecommendPage import NotPassedReplaceRecommendPage
from page_object.B.ReplaceRecommend.PassedReplaceRecommendPage import PassedReplaceRecommendPage

sekorm = Element('B_Element')


class ReplaceRecommendPage(BasePage):
    """替代推荐"""

    def go_NewReplaceRecommendPage(self):
        """替代推荐－新增替代推荐"""
        self.is_click(sekorm['替代推荐－新增替代推荐'])
        return NewReplaceRecommendPage(self.driver)

    def go_PassedReplaceRecommendPage(self):
        """替代推荐－替代推荐处理池"""
        self.is_click(sekorm['替代推荐－替代推荐处理池'])
        return PassedReplaceRecommendPage(self.driver)

    def go_BusinessReplaceRecommendPage(self):
        """替代推荐－替代推荐商务处理池"""
        self.is_click(sekorm['替代推荐－替代推荐商务处理池'])
        return BusinessReplaceRecommendPage(self.driver)

    def go_NotPassedReplaceRecommendPage(self):
        """替代推荐－不通过替代推荐"""
        self.is_click(sekorm['替代推荐－不通过替代推荐'])
        return NotPassedReplaceRecommendPage(self.driver)
