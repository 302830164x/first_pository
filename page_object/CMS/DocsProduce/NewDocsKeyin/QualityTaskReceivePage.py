
from common.readelement import Element
from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class QualityTaskReceivePage(BasePage):
    """领取质检任务"""

    def get_QualityTaskReceivePage_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
