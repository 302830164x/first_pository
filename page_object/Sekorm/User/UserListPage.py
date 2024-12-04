from page.basepage import BasePage
from page_object.Sekorm.Service.AskPricePage import AskPricePage
from page_object.Sekorm.Service.AskTimePage import AskTimePage
from page_object.Sekorm.Service.SampleApplicationPage import SampleApplicationPage
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage

Locator = {
    '型号清单标题': ('xpath', "//span[@class='checklist-title']"),
    '新建清单': ('xpath', "//a[@id='newCheckList']"),
    '清单折叠按钮': ('xpath', "//span[@class='inventoryName']"),
    '型号': ('xpath', "//a[@class='model-on']"),
    '厂牌': ('xpath', "//a[@class='model-brand']"),
    '来源': ('xpath', "//span[@class='sourceRoad']"),
    '描述': ('xpath', "//div[contains(@class,'supply-desc text-left')]"),
    '供应商': ('xpath', "(//td[contains(@class,'text-left')])[6]"),
    '仓库/预计交期': ('xpath', "(//td[contains(@class,'text-left')])[7]"),
    '单价': ('xpath', "//div[@data-price]"),
    '需求数量': ('xpath', "//input[@class='pcs']"),
    '小计': ('xpath', "//span[@data-price]"),
    '清单列表删除按钮': ('xpath', "//span[@class='trade-delete handle-type']"),
    '合计': ('xpath', "//p[contains(@class,'total_num')]"),
    '分享型号': ('xpath', "//span[@class='share-btn primary-blue-btn']"),
    '批量导入型号': ('xpath', "//span[@class='primary-blue-btn importPnCode']"),
    '快速添加型号': ('xpath', "//span[@class='primary-blue-btn addPnCode']"),
    '批量询价': ('xpath', "//a[contains(text(),'批量询价')]"),
    '交期查询': ('xpath', "//a[contains(text(),'交期查询')]"),
    '样品申请': ('xpath', "//a[contains(text(),'样品申请')]"),
    '企业支付': ('xpath', "//a[contains(text(),'企业支付')]"),
    '立即结算': ('xpath', "//a[contains(text(),'立即结算')]"),

    '型号清单复选按钮1': ('xpath', "//input[@value='27068']"),
    '型号清单复选按钮2': ('xpath', "//input[@value='14181']"),
}


class UserListPage(BasePage):
    """型号清单页"""

    def check_UserListPage(self):
        """检查型号清单页布局"""
        text = self.element_text(Locator['型号清单标题'])
        for elm in Locator:
            # 遍历检查每次页面元素是否存在
            self.move_to_element(Locator[elm])
        return text

    def check_UserListPage_submit(self):
        """检查型号清单提交订单"""
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        text = self.element_text(Locator['合计'])
        self.is_click(Locator['立即结算'])
        return text, ShopServicePage(self.driver)

    def check_UserListPage_business_pay(self):
        """检查型号清单提交企业支付"""
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        text = self.element_text(Locator['合计'])
        self.is_click(Locator['企业支付'])
        return text, ShopServicePage(self.driver)

    def check_UserListPage_sample(self):
        """检查型号清单提交样品申请"""
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        text = self.element_text(Locator['合计'])
        self.is_click(Locator['样品申请'])
        return text, SampleApplicationPage(self.driver)

    def check_UserListPage_ark_price(self):
        """检查型号清单提交批量询价"""
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        text = self.element_text(Locator['合计'])
        self.is_click(Locator['批量询价'])
        return text, AskPricePage(self.driver)

    def check_UserListPage_ark_time(self):
        """检查型号清单提交交期查询"""
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        self.is_click(Locator['型号清单复选按钮1'])
        self.is_click(Locator['型号清单复选按钮2'])
        text = self.element_text(Locator['合计'])
        self.is_click(Locator['交期查询'])
        return text, AskTimePage(self.driver)
