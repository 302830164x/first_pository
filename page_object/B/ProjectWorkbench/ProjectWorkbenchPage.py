from common.readelement import Element
from page.basepage import BasePage
from page_object.B.ProjectWorkbench.ChanceManagementListPage import ChanceManagementListPage
from page_object.B.ProjectWorkbench.ChancePoolPage import ChancePoolPage
from page_object.B.ProjectWorkbench.ChancePoolSimplifiedPage import ChancePoolSimplifiedPage
from page_object.B.ProjectWorkbench.ChanceSharePoolPage import ChanceSharePoolPage
from page_object.B.ProjectWorkbench.DrProjectImportPage import DrProjectImportPage
from page_object.B.ProjectWorkbench.DrProjectPage import DrProjectPage
from page_object.B.ProjectWorkbench.DrProjectPoolPage import DrProjectPoolPage
from page_object.B.ProjectWorkbench.JobProjectPoolPage import JobProjectPoolPage
from page_object.B.ProjectWorkbench.MyProjectPage import MyProjectPage
from page_object.B.ProjectWorkbench.NewProjectPage import NewProjectPage
from page_object.B.ProjectWorkbench.PnRecommendationPage import PnRecommendationPage
from page_object.B.ProjectWorkbench.ProjectPoolPage import ProjectPoolPage
from page_object.B.ProjectWorkbench.RecommendProjectPoolPage import RecommendProjectPoolPage
from page_object.B.ProjectWorkbench.RecommendationEnginePage import RecommendationEnginePage
from page_object.B.ProjectWorkbench.UnclaimedProjectPoolPage import UnclaimedProjectPoolPage

sekorm = Element('B_Element')


class ProjectWorkbenchPage(BasePage):
    """项目工作台"""

    def go_RecommendProjectPoolPage(self):
        """项目工作台－推荐给我的项目/需求"""
        self.is_click(sekorm['项目工作台－推荐给我的项目/需求'])
        return RecommendProjectPoolPage(self.driver)

    def go_UnclaimedProjectPoolPage(self):
        """项目工作台－未响应项目/需求"""
        self.is_click(sekorm['项目工作台－未响应项目/需求'])
        return UnclaimedProjectPoolPage(self.driver)

    def go_RecommendationEnginePage(self):
        """项目工作台－优选型号推荐"""
        self.is_click(sekorm['项目工作台－优选型号推荐'])
        return RecommendationEnginePage(self.driver)

    def go_ProjectPoolPage(self):
        """项目工作台－全部项目"""
        self.is_click(sekorm['项目工作台－全部项目'])
        return ProjectPoolPage(self.driver)

    def go_MyProjectPage(self):
        """项目工作台－我的项目"""
        self.is_click(sekorm['项目工作台－我的项目'])
        return MyProjectPage(self.driver)

    def go_NewProjectPage(self):
        """项目工作台－新项目"""
        self.is_click(sekorm['项目工作台－新项目'])
        return NewProjectPage(self.driver)

    def go_ChancePoolPage(self):
        """项目工作台－全部需求/方案"""
        self.is_click(sekorm['项目工作台－全部需求/方案'])
        return ChancePoolPage(self.driver)

    def go_ChanceSharePoolPage(self):
        """项目工作台－方案分享池"""
        self.is_click(sekorm['项目工作台－方案分享池'])
        return ChanceSharePoolPage(self.driver)

    def go_ChanceManagementListPage(self):
        """项目工作台－方案进度池"""
        self.is_click(sekorm['项目工作台－方案进度池'])
        return ChanceManagementListPage(self.driver)

    def go_ChancePoolSimplifiedPage(self):
        """项目工作台－项目型号库"""
        self.is_click(sekorm['项目工作台－项目型号库'])
        return ChancePoolSimplifiedPage(self.driver)

    def go_DrProjectImportPage(self):
        """项目工作台－批量更新DR"""
        self.is_click(sekorm['项目工作台－批量更新DR'])
        return DrProjectImportPage(self.driver)

    def go_DrProjectPage(self):
        """项目工作台－DR处理池"""
        self.is_click(sekorm['项目工作台－DR处理池'])
        return DrProjectPage(self.driver)

    def go_DrProjectPoolPage(self):
        """项目工作台－DR项目"""
        self.is_click(sekorm['项目工作台－DR项目'])
        return DrProjectPoolPage(self.driver)

    def go_JobProjectPoolPage(self):
        """项目工作台－事务工作台"""
        self.is_click(sekorm['项目工作台－事务项目'])
        return JobProjectPoolPage(self.driver)