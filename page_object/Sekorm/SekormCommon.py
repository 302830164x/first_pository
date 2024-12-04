from common.readelement import Element
from page.basepage import BasePage
from page_object.Sekorm.Search.BrandSearchPage import BrandSearchPage
from page_object.Sekorm.Service.FuturesPage import FuturesPage
from page_object.Sekorm.Service.ServiceCommonPage import ServiceCommPage
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.logger import log

from utils.times import sleep

sekorm = Element('SekormElement')
Locator = {
    '登录': ('xpath', "//a[@class='header_user_unlogin']"),
    '密码登录': ('xpath', "//a[@class='pwd-login']"),
    '手机号输入框': ('xpath', "//input[@id='userName']"),
    '密码输入框': ('xpath', "//input[@id='passwordTxt']"),
    '同意协议': ('xpath', "//label[@id='login_agree_circle']//i[@class='icon-agree-circle']"),
    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '英文站-登录': ('xpath', "//a[normalize-space()='Sign in / Register']"),
    '英文站-密码登录': ('xpath', "//p[@id='password_login']//a[contains(text(),'Sign in via password')]"),
    '英文站-邮箱输入框': ('xpath', "//input[@id='userName']"),
    '英文站-密码输入框': ('xpath', "//input[@id='passwordTxt']"),
    '英文站-登录按钮': ('xpath', "//input[@id='btn_login']"),
    '个人中心': ('xpath', "//span[@id='logined_user']//img"),
    '退出登录': ('xpath', "//a[@id='loginOut']"),
    '厂牌ROHM': ('xpath', "//div[@class='brand-cont']//div[1]//a[1]//img[1]"),
    '厂牌Logo墙': ('xpath', "//div[@class='brand-cont']"),
    '右侧广告1': ('xpath', "//div[@id='ad-wrap']//a[1]"),
    '右侧广告2': ('xpath', "//div[@id='ad-wrap']//a[2]"),
    '左侧广告1': ('xpath', "(//a[@class='zhuge-left-advert'])[1]/img"),
    '左侧广告2': ('xpath', "(//a[@class='zhuge-left-advert'])[2]/img"),
    '我要提问': ('xpath', "//a[@id='user_ask']"),
    '提问文案': ('xpath', "//div[@class='common-ask']/h5"),
    '下一页': ('xpath', "//div[@class='page-block page-next']/a"),
    '第二页': ('xpath', "//a[normalize-space()='2']"),
    'TDK-T': ('xpath', "/html//title[1]"),
    'TDK-D': ('xpath', "//meta[@name='Description']"),
    'TDK-K': ('xpath', "//meta[@name='Keywords']"),
    '技术问答': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'技术问答')]"),
    '选型帮助': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'选型帮助')]"),
    '设计方案': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'设计方案')]"),
    '研发服务': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'研发服务')]"),
    'BOM配单': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'BOM配单')]"),
    '样品申请': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'样品申请')]"),
    '资料下载': ('xpath', "//div[contains(@class,'cd-service-tool')]//li[contains(.,'资料下载')]"),
    '推荐列表': ('xpath', "//div[@id='expandMoreList']/div"),
    '推荐列表-展开更多': ('xpath', "//div[@class='expandMore']"),
    '资讯缩略图': ('xpath', "//div[@class='image-wrapper']//img"),
    '资讯标题': ('xpath', "//h2[@class='search-item-title text-ellipsis']"),
    '资讯简介': ('xpath', "//p[contains(@class,'search-item-summary')]"),
    '资讯类型': ('xpath', "//span[@class='weight-type']"),
    '资讯发布时间': ('xpath', "//div[contains(@class,'search-item')]//span[contains(text(),'发布时间')]"),
    '右侧服务列表-服务名称': ('xpath', "//div[@class='service-item-title']"),
    '右侧服务列表-服务LOGO': ('xpath', "//img[@class='service-item-brand']"),
    '右侧服务列表-服务简介': ('xpath', "//p[@class='service-content-item service-item-top']"),
    '右侧服务列表-服务按钮': ('xpath', "//span[contains(text(),'提交需求')]"),
}
ON_Locator = {
    'ON名称': ('xpath', "//div[contains(@class,'supply-model')]/p[1]/a[1]"),
    '厂牌名称': ('xpath', "//div[contains(@class,'supply-model')]/p[2]/a[1]"),
    '技术资料': ('xpath', "//div[contains(@class,'supply-model')]/p[3]/a[1]"),
    '品类': ('xpath', "//p[@class='desc-category']"),
    '系列': ('xpath', "//p[@class='desc-pn-ps']"),
    '描述': ('xpath', "//p[@class='desc-description']"),
    '最小包装量': ('xpath', "//p[@class='desc-fmtMinPackAmount']"),
    '供应商': ('xpath', "//p[@class='supply-supplier']"),
    '单价': ('xpath', "//p[@class='clearfix has-enUnitPrice']"),
    '现货': ('xpath', "//span[@class='pull-right']/span[1]"),
    '预计交期': ('xpath', "//span[@class='pull-right']/span[2]"),
    '仓库': ('xpath', "//span[@class='information-title pull-left pay-local-content ']"),
    '批次': ('xpath', "//p[@class='clearfix batch-information']"),

    '原厂认证': ('xpath', "(//p[@class='pull-left'][contains(text(),'原厂认证')])"),
    'ON详情页-商城-购买': ('xpath', "//a[@class='on-small-btn js-quick-buy']"),
    'ON详情页-市场-购买': ('xpath', "//a[@class='on-discount-small-btn js-quick-buy']"),
    '购买': ('xpath', "//a[contains(@class,'supply-btn')][contains(text(),'购买')]"),
    '批量询价': ('xpath', "//a[contains(text(),'批量询价')]"),
    '交期查询': ('xpath', "//a[contains(text(),'交期查询')]"),
    '样品申请': ('xpath', "//a[contains(text(),'样品申请')]"),
    '市场-购买': ('xpath', "//a[contains(@class,'supply-blue-btn')][contains(text(),'购买')]"),
    '期货订购': ('xpath', "//a[contains(text(),'期货订购')]"),
    '右侧ON列表-商城标题': ('xpath', "(//div[@class='searchRightSupply-header']//span)[1]"),
    '右侧ON列表-市场标题': ('xpath', "(//div[@class='searchRightSupply-header']//span)[2]"),
    '右侧ON列表-商城ON名称': ('xpath', "//div[@id='searchRightSupply-mall']//a[contains(@class,'searchRightSupply-item-on')]"),
    '右侧ON列表-市场ON名称': (
        'xpath', "//div[@id='searchRightSupply-market']//a[contains(@class,'searchRightSupply-item-on')]"),
    '右侧ON列表-ON品牌': ('xpath', "//p[@class='searchSupply-msg searchSupply-brand']"),
    '右侧ON列表-ON品牌logo': ('xpath', "//p[@class='searchSupply-msg searchSupply-brand']//img"),
    '右侧ON列表-ON品类': ('xpath', "//p[@class='searchSupply-msg searchSupply-goodList'][contains(text(),'品类：')]"),
    '右侧ON列表-ON价格': ('xpath', "//p[contains(text(),'价格：')]"),
    '右侧ON列表-ON现货': ('xpath', "//p[contains(text(),'现货：')]"),
    '右侧ON列表-商城查看更多': ('xpath', "//p[@id='goSupply']//a[@alt='查看更多']"),
    '右侧ON列表-市场查看更多': ('xpath', "//p[@id='goMarket']//a[@alt='查看更多']"),
}


class SekormCommon(BasePage):
    """公共模块方法"""

    def get_elm_attribute(self, elm, attribute_name):
        """获取指定元素的某个属性的值"""
        return self.get_attribute_value(sekorm[elm], attribute_name)

    def check_logo(self):
        """检查Logo墙展开和收起，点击logo列表"""
        self.move_to_element(Locator['厂牌Logo墙'])
        self.is_click(Locator['厂牌ROHM'])
        self.switch_window()
        sleep()
        return BrandSearchPage(self.driver)

    def check_advertising(self, elm):
        """点击左侧、右侧广告"""
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return self.driver.current_url

    def check_ask(self):
        """检查Logo墙下方提问按钮"""
        self.element_move_to_center(Locator['我要提问'])
        text = self.element_text(Locator['提问文案'])
        self.is_click(Locator['我要提问'])
        self.switch_window()
        sleep()
        from page_object.Sekorm.Service.AskServicePage import AskServicePage
        return text, AskServicePage(self.driver)

    def next_page(self, next_action):
        """
        翻页
        :param next_action: 传入True or False
        :return: 如果传入True，返回self则可以链路继续执行，如果传入False，返回页面属性值，用于判断第二页是否高亮
        """
        self.is_click(Locator['下一页'])
        sleep()
        active = self.get_attribute_value(Locator['第二页'], 'class')
        # 根据参数判断是否进行翻页后操作
        if next_action:
            return self
        else:
            return active

    def check_TDK(self):
        """获取页面TDK"""
        T = self.element_text(Locator['TDK-T'])
        D = self.get_attribute_value(Locator['TDK-D'], 'content')
        K = self.get_attribute_value(Locator['TDK-K'], 'content')
        return T, D, K

    def click_common_service(self, elm):
        """检查相关服务模块的服务"""
        self.element_move_to_center(Locator[elm])
        self.move_to_element(Locator[elm])
        text = self.get_attribute_value(Locator[elm], 'data-powertip')
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return ServiceCommPage(self.driver), text

    def check_common_click(self, elm):
        """检查相关推荐-各种点击"""
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return self

    def check_num(self, elm):
        """检查公共模块的内容条数"""
        self.element_move_to_center(Locator[elm])
        return self.elements_num(Locator[elm])

    def go_OnPage(self, elm):
        """ON模块-点击ON名称、技术资料，跳转ON详情页"""
        from page_object.Sekorm.Supply.OnPage import OnPage
        self.is_click(ON_Locator[elm])
        self.switch_window()
        sleep()
        return OnPage(self.driver)

    def go_brand_search(self):
        """ON模块-点击厂牌名称，跳转厂牌搜索结果页"""
        self.is_click(ON_Locator['厂牌名称'])
        self.switch_window()
        sleep()
        return BrandSearchPage(self.driver)

    def check_description(self):
        """ON模块-检查描述列"""
        self.element_move_to_center(ON_Locator['品类'])
        self.move_to_element(ON_Locator['品类'])
        self.move_to_element(ON_Locator['系列'])
        self.move_to_element(ON_Locator['描述'])
        return self.element_text(ON_Locator['最小包装量'])

    def check_supplier(self):
        """ON模块-检查供应商/品质保证"""
        self.move_to_element(ON_Locator['原厂认证'])
        return self.element_text(ON_Locator['供应商'])

    def check_ON_information(self):
        """ON模块-检查单价（含增值税）"""
        self.move_to_element(ON_Locator['单价'])
        self.move_to_element(ON_Locator['现货'])
        self.move_to_element(ON_Locator['仓库'])
        return self.element_text(ON_Locator['预计交期'])

    def unlogin_click_service(self, elm):
        """ON模块-未登录-点击ON服务"""
        self.element_move_to_center(ON_Locator[elm])
        self.move_to_element(ON_Locator[elm])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(ON_Locator[elm], 'data-powertip')
        self.is_click(ON_Locator[elm])
        return text, UnLoginPage(self.driver)

    def go_FuturesPage(self):
        """未登录-点击ON服务"""
        self.is_click(ON_Locator['期货订购'])
        self.switch_window()
        sleep()
        return FuturesPage(self.driver)

    def go_SupplySearchPage(self, elm):
        """详情页右侧ON模块-点ON名称，进入商城垂搜"""
        from page_object.Sekorm.Search.SupplySearchPage import SupplySearchPage
        text = self.element_text(ON_Locator[elm])
        self.is_click(ON_Locator[elm])
        self.switch_window()
        sleep()
        return text, SupplySearchPage(self.driver)

    def go_MallSearchPage(self, elm):
        """详情页右侧ON模块-点ON名称，进入市场垂搜"""
        from page_object.Sekorm.Search.MallSearchPage import MallSearchPage
        text = self.element_text(ON_Locator[elm])
        self.is_click(ON_Locator[elm])
        self.switch_window()
        sleep()
        return text, MallSearchPage(self.driver)

    def check_right_on_description(self):
        """右侧ON模块-检查ON信息"""
        text1 = self.element_text(ON_Locator['右侧ON列表-商城标题'])
        text2 = self.element_text(ON_Locator['右侧ON列表-市场标题'])
        self.move_to_element(ON_Locator['右侧ON列表-商城ON名称'])
        self.move_to_element(ON_Locator['右侧ON列表-ON品牌'])
        self.move_to_element(ON_Locator['右侧ON列表-ON品牌logo'])
        self.move_to_element(ON_Locator['右侧ON列表-ON品类'])
        self.move_to_element(ON_Locator['右侧ON列表-ON价格'])
        self.move_to_element(ON_Locator['右侧ON列表-ON现货'])
        self.move_to_element(ON_Locator['右侧ON列表-市场ON名称'])
        return text1, text2

    def check_right_service(self):
        """右侧服务模块-检查服务信息"""
        self.move_to_element(Locator['右侧服务列表-服务名称'])
        self.move_to_element(Locator['右侧服务列表-服务LOGO'])
        self.move_to_element(Locator['右侧服务列表-服务简介'])
        self.is_click(Locator['右侧服务列表-服务按钮'])
        self.switch_window()
        return ServiceCommPage(self.driver)

    def check_right_supply_service(self, elm):
        """右侧ON模块-检查商城ON服务"""
        from page_object.Sekorm.Search.SupplySearchPage import SupplySearchPage
        self.element_move_to_center(ON_Locator[elm])
        self.move_to_element(ON_Locator[elm])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(ON_Locator[elm], 'data-powertip')
        self.is_click(ON_Locator[elm])
        self.switch_window()
        return text, SupplySearchPage(self.driver)

    def check_right_mall_service(self, elm):
        """右侧ON模块-检查市场ON服务"""
        from page_object.Sekorm.Search.MallSearchPage import MallSearchPage
        self.element_move_to_center(ON_Locator[elm])
        self.move_to_element(ON_Locator[elm])
        # 获取悬浮按钮时显示的文案
        text = self.get_attribute_value(ON_Locator[elm], 'data-powertip')
        self.is_click(ON_Locator[elm])
        self.switch_window()
        return text, MallSearchPage(self.driver)

    def check_recommend_list(self):
        """检查推荐列表和点击"""
        from page_object.Sekorm.News.NewsDetailPage import NewsDetailPage
        self.move_to_element(Locator['资讯缩略图'])
        self.move_to_element(Locator['资讯标题'])
        self.move_to_element(Locator['资讯简介'])
        self.move_to_element(Locator['资讯类型'])
        self.move_to_element(Locator['资讯发布时间'])
        self.is_click(Locator['资讯缩略图'])
        self.switch_window()
        sleep()
        return NewsDetailPage(self.driver)

    def get_login(self):
        """首页进行登录"""
        if self.is_existence(Locator['个人中心']):
            log.info("已登录")
            return self
        else:
            log.info("未登录")
            self.is_click(Locator['登录'])
            self.is_click(Locator['密码登录'])
            self.input_text(Locator['手机号输入框'], '15913623753')
            self.input_text(Locator['密码输入框'], '12qwblue')
            self.is_click(Locator['同意协议'])
            self.is_click(Locator['登录按钮'])
            return self

    def quit_login(self):
        """退出登录"""
        self.move_to_element(Locator['个人中心'])
        sleep()
        self.is_click(Locator['退出登录'])
        return self

    def get_en_login(self):
        """英文站进行登录"""
        sleep(0.3)
        if self.is_existence(Locator['个人中心']):
            log.info("已登录")
            return self
        else:
            log.info("未登录")
            self.is_click(Locator['英文站-登录'])
            self.is_click(Locator['英文站-密码登录'])
            self.input_text(Locator['英文站-邮箱输入框'], 'peter_fang@sekorm.com')
            self.input_text(Locator['英文站-密码输入框'], '123456')
            self.is_click(Locator['英文站-登录按钮'])
            return self
