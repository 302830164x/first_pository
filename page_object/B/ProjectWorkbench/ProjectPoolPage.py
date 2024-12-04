from common.readelement import Element
from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '列表': ('xpath', "//div[@class='line-ellipsis']"),
}


class ProjectPoolPage(BasePage):
    """全部项目"""

    def get_ProjectPoolPage_num(self):
        """获取列表内容条数"""
        sleep()
        return self.elements_num(Locator['列表'])
