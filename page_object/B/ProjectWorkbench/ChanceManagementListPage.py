from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]"),
}


class ChanceManagementListPage(BasePage):
    """方案进度池"""
    pass
