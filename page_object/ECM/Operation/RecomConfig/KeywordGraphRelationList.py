from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row')]"),
}


class KeywordGraphRelationList(BasePage):
    """二元关系图谱分析"""

    def get_KeywordGraphRelationList_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
