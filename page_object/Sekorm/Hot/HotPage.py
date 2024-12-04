from common.readelement import Element
from page.basepage import BasePage
from page_object.Sekorm.Brands.BrandsPage import BrandsPage
from page_object.Sekorm.Doc.DocDetailPage import DocDetailPage
from page_object.Sekorm.Faq.FaqDetailPage import FaqDetailPage
from page_object.Sekorm.News.NewsDetailPage import NewsDetailPage
from page_object.Sekorm.Search.BrandSearchPage import BrandSearchPage
from page_object.Sekorm.Search.SupplySearchPage import SupplySearchPage
from page_object.Sekorm.Search.Tab.Tab11Page import Tab11Page
from page_object.Sekorm.Service.ServiceCommonPage import ServiceCommPage
from page_object.Sekorm.UnLogin.UnLoginPage import UnLoginPage
from utils.times import sleep

sekorm = Element('SekormElement')


class HotPage(BasePage):
    """热门"""

    def banner_change(self):
        """轮播图切换"""
        self.move_to_element(sekorm['首页轮播图'])
        size1 = self.img_show(sekorm['轮播图照片'])
        self.is_click(sekorm['首页轮播图下一页'])
        size2 = self.img_show(sekorm['轮播图照片'])
        self.is_click(sekorm['首页轮播图下一页'])
        size3 = self.img_show(sekorm['轮播图照片'])
        self.is_click(sekorm['首页轮播图下一页'])
        size4 = self.img_show(sekorm['轮播图照片'])
        self.is_click(sekorm['首页轮播图下一页'])
        self.is_click(sekorm['首页轮播图上一页'])
        self.is_click(sekorm['首页轮播图上一页'])
        self.is_click(sekorm['首页轮播图上一页'])
        self.is_click(sekorm['首页轮播图上一页'])
        return size1, size2, size3, size4

    def click_banner(self):
        """点击轮播图"""
        self.move_to_element(sekorm['首页轮播图'])
        self.is_click(sekorm['首页轮播图下一页'])
        self.is_click(sekorm['首页轮播图'])
        self.switch_window()
        return NewsDetailPage(self.driver)

    def check_webRightBanner1(self):
        """检查1000家banner"""
        size = self.img_show(sekorm['1000家banner'])
        self.is_click(sekorm['1000家banner'])
        self.switch_window()
        return size, BrandsPage(self.driver)

    def check_webRightBanner2(self):
        """研发服务banner"""
        size = self.img_show(sekorm['研发服务banner'])
        self.is_click(sekorm['研发服务banner'])
        self.switch_window()
        return size, Tab11Page(self.driver)

    def check_webRightBanner3(self):
        """供应服务banner"""
        size = self.img_show(sekorm['供应服务banner'])
        self.is_click(sekorm['供应服务banner'])
        self.switch_window()
        return size, Tab11Page(self.driver)

    def check_webFloor_advertise(self, elm):
        """检查楼层广告"""
        size = self.img_show(sekorm[elm])
        self.is_click(sekorm[elm])
        self.switch_window()
        return size, Tab11Page(self.driver)

    def check_webFloor_hot(self):
        """检查热门楼层内容"""
        size = self.img_show(sekorm['热门楼层内容'])
        self.is_click(sekorm['热门楼层内容'])
        self.switch_window()
        return size, NewsDetailPage(self.driver)

    def check_webFloor_news(self):
        """检查新技术楼层内容"""
        size = self.img_show(sekorm['新技术楼层内容'])
        self.is_click(sekorm['新技术楼层内容'])
        self.switch_window()
        return size, NewsDetailPage(self.driver)

    def check_webFloor_supply(self):
        """检查电子商城楼层内容"""
        size = self.img_show(sekorm['电子商城楼层内容'])
        self.is_click(sekorm['电子商城楼层内容'])
        self.switch_window()
        return size, SupplySearchPage(self.driver)

    def check_webFloor_doc(self):
        """检查技术资料楼层内容"""
        size = self.img_show(sekorm['技术资料楼层内容'])
        self.is_click(sekorm['技术资料楼层内容'])
        self.switch_window()
        return size, DocDetailPage(self.driver)

    def check_webFloor_customize(self):
        """检查加工定制楼层内容"""
        size = self.img_show(sekorm['加工定制楼层内容'])
        self.is_click(sekorm['加工定制楼层内容'])
        self.switch_window()
        return size, ServiceCommPage(self.driver)

    def check_webFloor_faq(self):
        """检查技术问答楼层内容"""
        self.is_click(sekorm['技术问答楼层内容'])
        self.switch_window()
        return FaqDetailPage(self.driver)

    def check_webFloor_procurement(self):
        """检查采购服务楼层内容"""
        size = self.img_show(sekorm['采购服务楼层内容'])
        self.is_click(sekorm['采购服务楼层内容'])
        self.switch_window()
        return size, NewsDetailPage(self.driver)

    def check_webFloor_cooperate(self):
        """检查合作楼层内容"""
        size = self.img_show(sekorm['合作楼层内容'])
        self.is_click(sekorm['合作楼层内容'])
        self.switch_window()
        return size, ServiceCommPage(self.driver)

    def check_webFloor_brands(self):
        """检查授权品牌楼层内容"""
        size = self.img_show(sekorm['授权品牌楼层内容'])
        self.is_click(sekorm['授权品牌楼层内容'])
        self.switch_window()
        return size, BrandSearchPage(self.driver)

    def Unlogin_click_top(self, elm):
        """未登录-点击首页顶部各个触发登录的元素"""
        self.move_to_element(sekorm['型号清单-0'])
        self.is_click(sekorm[elm])
        return UnLoginPage(self.driver)

    def Unlogin_click_bottom(self, elm):
        """未登录-点击首页个人中心各个触发登录的元素"""
        self.scroll_to_bottom()
        self.is_click(sekorm[elm])
        self.switch_window()
        sleep()
        return UnLoginPage(self.driver)

    def Unlogin_click_history(self):
        """未登录-点击首页历史模块触发登录"""
        self.scroll_to_bottom()
        self.is_click(sekorm['历史记录模块'])
        return UnLoginPage(self.driver)

    def check_floating_text(self, elm):
        """检查悬浮按钮文本"""
        self.move_to_element(sekorm[elm])

    def click_floating(self, elm):
        """检查悬浮按钮点击"""
        self.is_click(sekorm[elm])
        return UnLoginPage(self.driver)
