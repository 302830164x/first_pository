from page_object.Sekorm.Doc.DocDetailPage import DocDetailPage
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.Service.AskPricePage import AskPricePage
from page_object.Sekorm.Service.AskTimePage import AskTimePage
from page_object.Sekorm.Service.FuturesPage import FuturesPage
from page_object.Sekorm.Service.SampleApplicationPage import SampleApplicationPage
from page_object.Sekorm.Service.ShopServicePage import ShopServicePage
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.logger import log
from utils.times import sleep

Locator = {
    '型号': ('xpath', "//h1[@id='supply_detail']"),
    '品牌': ('xpath', "//div[@class='details-brand']"),
    '品牌Logo': ('xpath', "//div[@class='details-brand']//img"),
    '描述': ('xpath', "//p[@class='detail-ct-descMain']"),
    '规格参数': ('xpath', "//div[@class='space-table']//h3"),
    '资料下载': ('xpath', "//div[@class='mt15']//h3"),
    '电子商城': ('xpath', "(//a[@class='module-recom'])[1]"),
    '市场': ('xpath', "(//a[@class='module-recom'])[2]"),
    '相关服务': ('xpath', "//p[contains(text(),'相关研发服务和供应服务')]"),
    '订货型号': ('xpath', "//table[@id='supply-detail-table']//tr[1]/td[2]"),
    '规格参数-品牌': ('xpath', "//table[@id='supply-detail-table']//tr[2]/td[2]"),
    '型号系列': ('xpath', "//table[@id='supply-detail-table']//tr[3]/td[2]"),
    '品类': ('xpath', "//table[@id='supply-detail-table']//tr[4]/td[2]"),
    '描述/说明': ('xpath', "//table[@id='supply-detail-table']//tr[5]/td[2]"),
    '封装/外壳/尺寸': ('xpath', "//table[@id='supply-detail-table']//tr[6]/td[2]"),
    '最小包装量': ('xpath', "//table[@id='supply-detail-table']//tr[7]/td[2]"),
    '包装形式': ('xpath', "//table[@id='supply-detail-table']//tr[8]/td[2]"),
    '生命周期': ('xpath', "//table[@id='supply-detail-table']//tr[9]/td[2]"),
    '停产时间': ('xpath', "//table[@id='supply-detail-table']//tr[10]/td[2]"),

    'Frequency(MHz)': ('xpath', "//table[@id='supply-detail-table']//tr[11]/td[1]"),
    'Flash (kB)': ('xpath', "//table[@id='supply-detail-table']//tr[12]/td[1]"),
    'RAM (kB)': ('xpath', "//table[@id='supply-detail-table']//tr[13]/td[1]"),
    'Comparators(个)': ('xpath', "//table[@id='supply-detail-table']//tr[14]/td[1]"),
    'UART(个)': ('xpath', "//table[@id='supply-detail-table']//tr[15]/td[1]"),
    'SPI(个)': ('xpath', "//table[@id='supply-detail-table']//tr[16]/td[1]"),
    'I2C(个)': ('xpath', "//table[@id='supply-detail-table']//tr[17]/td[1]"),
    'Vdd (min)': ('xpath', "//table[@id='supply-detail-table']//tr[18]/td[1]"),
    'Vdd (max)': ('xpath', "//table[@id='supply-detail-table']//tr[19]/td[1]"),

    '研发服务': ('xpath', "((//div[@class='first-content'])[1]//li)[1]"),
    '商务客服': ('xpath', "((//div[@class='first-content'])[1]//li)[2]"),
    '加入到型号清单': ('xpath', "((//div[@class='first-content'])[1]//li)[3]"),

    '预览': ('xpath', "//a[contains(text(),'预览')]"),
    '下载': ('xpath', "//a[contains(text(),'下载')]"),
    '资料标题': ('xpath', "//a[@class='item_title']"),
    '查看更多': ('xpath', "//div[@id='loadMore']"),
    '商城供应商': ('xpath', "//div[@id='js_supply_module']//div[@class='on-brand-name']"),
    '商城标签': ('xpath', "//div[@id='js_supply_module']//p[contains(text(),'原厂认证')]"),
    '商城现货和交期': ('xpath', "//div[@id='js_supply_module']//span[@class='on_text2 allow-sall']"),
    '商城仓库': ('xpath', "//div[@id='js_supply_module']//span[@class='information-content pay-local-content']"),
    '商城价格': ('xpath', "//div[@id='js_supply_module']//span[@class='information-title on_text']"),

    '市场供应商': ('xpath', "//div[@id='js_discount_module']//div[@class='on-brand-name']"),
    '市场现货和交期': ('xpath', "//div[@id='js_discount_module']//span[@class='on_text2 allow-sall']"),
    '市场仓库': ('xpath', "//div[@id='js_discount_module']//span[@class='information-content pay-local-content']"),
    '市场价格': ('xpath', "//div[@id='js_discount_module']//span[@class='information-title on_text']"),
    '市场批次': ('xpath', "//div[@id='js_discount_module']//span[contains(text(),'批次：')]"),


    '批量询价': ('xpath', "//a[contains(text(),'批量询价')]"),
    '交期查询': ('xpath', "//a[contains(text(),'交期查询')]"),
    '样品申请': ('xpath', "//a[contains(text(),'样品申请')]"),
    '期货订购': ('xpath', "//a[contains(text(),'期货订购')]"),
    'ON详情页-商城-购买': ('xpath', "//a[@class='on-small-btn js-quick-buy']"),
    'ON详情页-市场-购买': ('xpath', "//a[@class='on-discount-small-btn js-quick-buy']"),
}


class OnPage(SekormCommon):
    """ON详情页"""

    def check_layout(self):
        """检查ON详情页布局"""
        self.move_to_element(Locator['描述'])
        self.move_to_element(Locator['型号'])
        self.move_to_element(Locator['品牌'])
        self.move_to_element(Locator['资料下载'])
        self.move_to_element(Locator['相关服务'])
        return self.element_text(Locator['规格参数'])

    def check_ON(self):
        """检查ON详情页各个模块"""
        text = []
        self.move_to_element(Locator['品牌Logo'])
        self.move_to_element(Locator['描述'])
        text.append(self.element_text(Locator['型号']))
        text.append(self.element_text(Locator['品牌']))
        text.append(self.element_text(Locator['规格参数']))
        text.append(self.element_text(Locator['资料下载']))
        text.append(self.element_text(Locator['电子商城']))
        text.append(self.element_text(Locator['市场']))
        text.append(self.element_text(Locator['相关服务']))
        return text

    def check_detail(self):
        """检查ON详情页-规格参数字段"""
        text = []
        self.element_move_to_center(Locator['规格参数'])
        text.append(self.element_text(Locator['订货型号']))
        text.append(self.element_text(Locator['规格参数-品牌']))
        text.append(self.element_text(Locator['型号系列']))
        text.append(self.element_text(Locator['品类']))
        text.append(self.element_text(Locator['描述/说明']))
        text.append(self.element_text(Locator['封装/外壳/尺寸']))
        text.append(self.element_text(Locator['最小包装量']))
        text.append(self.element_text(Locator['包装形式']))
        text.append(self.element_text(Locator['生命周期']))
        text.append(self.element_text(Locator['停产时间']))
        text.append(self.element_text(Locator['Frequency(MHz)']))
        text.append(self.element_text(Locator['Flash (kB)']))
        text.append(self.element_text(Locator['RAM (kB)']))
        text.append(self.element_text(Locator['Comparators(个)']))
        text.append(self.element_text(Locator['UART(个)']))
        text.append(self.element_text(Locator['SPI(个)']))
        text.append(self.element_text(Locator['I2C(个)']))
        text.append(self.element_text(Locator['Vdd (min)']))
        text.append(self.element_text(Locator['Vdd (max)']))
        return text

    def unlogin_click(self, elm):
        """未登录检查发送邮箱、加入型号清单按钮、资料下载列表的预览、下载按钮"""
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return UnLoginPage(self.driver)

    def click_doc_title(self):
        """点击资料下载列表的资料标题"""
        text = self.element_text(Locator['资料标题'])
        self.is_click(Locator['资料标题'])
        self.switch_window()
        sleep()
        return text

    def check_doc_num(self):
        """检查资料下载列表的资料数量、加载更多功能"""
        num1 = self.elements_num(Locator['资料标题'])
        self.is_click(Locator['查看更多'])
        num2 = self.elements_num(Locator['资料标题'])
        return num1, num2

    def check_on_supply(self):
        """检查ON商城模板"""
        text1 = self.element_text(Locator['商城供应商'])
        text2 = self.element_text(Locator['商城现货和交期'])
        self.move_to_element(Locator['商城标签'])
        self.move_to_element(Locator['商城仓库'])
        self.move_to_element(Locator['商城价格'])
        return text1, text2

    def check_on_mall(self):
        """检查ON市场模板"""
        text1 = self.element_text(Locator['市场供应商'])
        text2 = self.element_text(Locator['市场现货和交期'])
        self.move_to_element(Locator['市场仓库'])
        self.move_to_element(Locator['市场价格'])
        self.move_to_element(Locator['市场批次'])
        return text1, text2

    def go_FuturesPage(self):
        """点击期货订购"""
        self.is_click(Locator['期货订购'])
        self.switch_window()
        sleep()
        return FuturesPage(self.driver)

    def on_submit_order(self, elm):
        """从ON详情页提交订单"""
        self.move_to_element(Locator[elm])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator[elm], 'data-powertip')
        self.is_click(Locator[elm])
        return text, ShopServicePage(self.driver)

    def check_on_sample(self):
        """检查ON详情页样品申请服务按钮"""
        self.move_to_element(Locator['样品申请'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['样品申请'], 'data-powertip')
        self.is_click(Locator['样品申请'])
        return text, SampleApplicationPage(self.driver)

    def check_on_ask_price(self):
        """检查ON详情页 批量询价 服务按钮"""
        self.move_to_element(Locator['批量询价'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['批量询价'], 'data-powertip')
        self.is_click(Locator['批量询价'])
        return text, AskPricePage(self.driver)

    def check_on_ask_time(self):
        """检查ON详情页 交期查询 服务按钮"""
        self.move_to_element(Locator['交期查询'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['交期查询'], 'data-powertip')
        self.is_click(Locator['交期查询'])
        return text, AskTimePage(self.driver)

    def check_on_futures(self):
        """检查ON详情页 期货订购 服务按钮"""
        self.move_to_element(Locator['期货订购'])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(Locator['期货订购'], 'data-powertip')
        self.is_click(Locator['期货订购'])
        self.switch_window()
        return text, FuturesPage(self.driver)
