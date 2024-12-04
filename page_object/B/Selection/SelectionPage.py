from common.readelement import Element
from page.basepage import BasePage
from page_object.B.Selection.BusinessSelectionPage import BusinessSelectionPage
from page_object.B.Selection.NewSelectionPage import NewSelectionPage
from page_object.B.Selection.PassedSelectionPage import PassedSelectionPage
from page_object.B.ServiceManage.ServiceManagePage import ServiceManagePage

sekorm = Element('B_Element')


class SelectionPage(BasePage):
    """选型帮助"""

    def go_NewSelectionPage(self):
        """选型帮助－新增选型帮助"""
        self.is_click(sekorm['选型帮助－新增选型帮助'])
        return NewSelectionPage(self.driver)

    def go_PassedSelectionPage(self):
        """选型帮助－选型帮助技术处理池"""
        self.is_click(sekorm['选型帮助－选型帮助技术处理池'])
        return PassedSelectionPage(self.driver)

    def go_BusinessSelectionPage(self):
        """选型帮助－选型帮助商务处理池"""
        self.is_click(sekorm['选型帮助－选型帮助商务处理池'])
        return BusinessSelectionPage(self.driver)

    def go_NotPassedSelectionPage(self):
        """选型帮助－不通过选型帮助"""
        self.is_click(sekorm['选型帮助－不通过选型帮助'])
        return ServiceManagePage(self.driver)
