from random import sample

from common.readconfig import ini
from common.readelement import Element
from page_object.Sekorm.Brands.BrandsPage import BrandsPage
from page_object.Sekorm.Doc.ComparatorPage import ComparatorPage
from page_object.Sekorm.Doc.DocDetailPage import DocDetailPage
from page_object.Sekorm.Doc.SelectionDetailPage import SelectionDetailPage
from page_object.Sekorm.EnSekrom.EnSekormIndexPage import EnSekormIndexPage
from page_object.Sekorm.Faq.FaqDetailPage import FaqDetailPage
from page_object.Sekorm.Faq.FaqPage import FaqPage
from page_object.Sekorm.Hot.AboutPage import AboutPage
from page_object.Sekorm.Hot.AgreementPage import AgreementPage
from page_object.Sekorm.Hot.CulturePage import CulturePage
from page_object.Sekorm.Hot.HotPage import HotPage
from page_object.Sekorm.Hot.IndexServicePage import IndexServicePage
from page_object.Sekorm.Hot.MilestonePage import MilestonePage
from page_object.Sekorm.Hot.SitemapPage import SitemapPage
from page_object.Sekorm.Mall.MallPage import MallPage
from page_object.Sekorm.News.NewsDetailPage import NewsDetailPage
from page_object.Sekorm.News.NewsPage import NewsPage
from page_object.Sekorm.Search.DocSearchPage import DocSearchPage
from page_object.Sekorm.Search.MallSearchPage import MallSearchPage
from page_object.Sekorm.Search.SearchPage import SearchPage
from page_object.Sekorm.Search.SupplySearchPage import SupplySearchPage
from page_object.Sekorm.Search.Tab.Tab11Page import Tab11Page
from page_object.Sekorm.Search.Tab.Tab12Page import Tab12Page
from page_object.Sekorm.Search.Tab.Tab13Page import Tab13Page
from page_object.Sekorm.SekormCommon import SekormCommon
from page_object.Sekorm.Supply.OnPage import OnPage
from page_object.Sekorm.Supply.SupplyPage import SupplyPage
from page_object.Sekorm.User.UserInfoPage import UserInfoPage
from page_object.Sekorm.User.UserListPage import UserListPage
from page_object.Sekorm.User.UserOrderPage import UserOrderPage
from utils.times import sleep

sekorm = Element('SekormElement')
Locator = {
    '个人中心': ('xpath', "//span[@id='logined_user']//img"),
    '型号清单': ('xpath', "//a[@class='checklist-cart']"),
    '我的订单': ('xpath', "//a[@id='header_user_order_logined']"),
}


class SekormIndexPage(SekormCommon):
    """前台首页"""

    def go_SekormIndexPage(self):
        """点击首页图标"""
        self.is_click(sekorm['首页图标'])
        return SekormIndexPage(self.driver)

    def go_HotPage(self):
        """跳转热门"""
        self.is_click(sekorm['热门'])
        return HotPage(self.driver)

    def go_NewsPage(self):
        """跳转新技术"""
        self.is_click(sekorm['新技术'])
        return NewsPage(self.driver)

    def go_SupplyPage(self):
        """跳转电子商城"""
        self.is_click(sekorm['电子商城'])
        return SupplyPage(self.driver)

    def go_FaqPage(self):
        """跳转技术问答"""
        self.is_click(sekorm['技术问答'])
        return FaqPage(self.driver)

    def go_MallPage(self):
        """跳转现货市场"""
        self.is_click(sekorm['现货市场'])
        return MallPage(self.driver)

    def go_BrandsPage(self):
        """跳转代理品牌"""
        self.is_click(sekorm['代理品牌'])
        return BrandsPage(self.driver)

    def go_Tab11_Page(self):
        """跳转tab=11的门楣"""
        self.move_to_element(sekorm['新技术'])
        self.is_click(sekorm['新技术-EDA软件'])
        return Tab11Page(self.driver)

    def go_Tab12_Page(self ):
        """跳转tab=12的门楣"""
        self.move_to_element(sekorm['电子商城'])
        self.is_click(sekorm['电子商城-IC'])
        return Tab12Page(self.driver)

    def go_Tab13_Page(self):
        """跳转tab=13的门楣"""
        self.move_to_element(sekorm['热门'])
        self.is_click(sekorm['热门-汽车电子'])
        return Tab13Page(self.driver)

    def go_Tab11_Purchasing(self):
        """跳转采购服务"""
        self.is_click(sekorm['采购服务'])
        return Tab11Page(self.driver)

    def go_Tab11_Cooperation(self):
        """跳转合作"""
        self.is_click(sekorm['合作'])
        return Tab11Page(self.driver)

    def go_Connect_NewsDetail(self):
        """联系我们"""
        self.is_click(sekorm['联系我们'])
        self.switch_window()
        sleep()
        return NewsDetailPage(self.driver)

    def go_NewsDetailPage_byID(self, new_id):
        """根据ID跳转资讯详情页"""
        self.get_url(f'{ini.SekormUrl}/news/{new_id}.html')
        return NewsDetailPage(self.driver)

    def go_DocDetailPage_byID(self, doc_id):
        """根据ID跳转资料详情页"""
        self.get_url(f'{ini.SekormUrl}/doc/{doc_id}.html')
        return DocDetailPage(self.driver)

    def go_FaqDetailPage_byID(self, faq_id):
        """根据ID跳转问答详情页"""
        self.get_url(f'{ini.SekormUrl}/faq/{faq_id}.html')
        return FaqDetailPage(self.driver)

    def go_OnPage_byID(self, on_id):
        """根据ID跳转ON详情页"""
        self.get_url(f'{ini.SekormUrl}/product/{on_id}.html')
        return OnPage(self.driver)

    def go_ComparatorPage_byID(self, comparator_id):
        """根据ID跳转对照表详情页"""
        self.get_url(f'{ini.SekormUrl}/comparator/{comparator_id}.html')
        return ComparatorPage(self.driver)

    def go_SelectionDetailPage_byID(self, selection_id):
        """根据ID跳转选型表详情页"""
        self.get_url(f'{ini.SekormUrl}/selection/{selection_id}.html')
        return SelectionDetailPage(self.driver)

    def go_EnSekorm(self):
        """根据访问跳转英文站"""
        self.get_url(ini.EnSekormUrl)
        return EnSekormIndexPage(self.driver)

    def go_UserInfoPage(self):
        """跳转个人中心"""
        self.is_click(Locator['个人中心'])
        return UserInfoPage(self.driver)

    def go_UserListPage(self):
        """跳转型号清单"""
        self.is_click(Locator['型号清单'])
        return UserListPage(self.driver)

    def go_UserOrderPage(self):
        """跳转我的订单"""
        self.is_click(Locator['个人中心'])
        return UserOrderPage(self.driver)

    def get_search(self, text):
        """搜索"""
        self.input_text(sekorm['搜索框'], text)
        self.is_click(sekorm['搜索按钮'])
        return SearchPage(self.driver)

    def go_SupplySearchPage(self, text):
        """电子商城垂直搜索"""
        self.is_click(sekorm['电子商城'])
        self.input_text(sekorm['搜索框'], text)
        self.is_click(sekorm['搜索按钮'])
        return SupplySearchPage(self.driver)

    def go_MallSearchPage(self, text):
        """现货市场垂直搜索"""
        self.is_click(sekorm['现货市场'])
        self.input_text(sekorm['搜索框'], text)
        self.is_click(sekorm['搜索按钮'])
        return MallSearchPage(self.driver)

    def go_DocSearchPage(self, text):
        """技术资料搜索结果页"""
        self.is_click(sekorm['技术资料频道'])
        self.switch_window()
        self.input_text(sekorm['搜索框'], text)
        self.is_click(sekorm['搜索按钮'])
        return DocSearchPage(self.driver)

    def go_AgreementPage(self, elm):
        """点击首页底部-关于本网站-各个协议"""
        self.scroll_to_bottom()
        self.is_click(sekorm[elm])
        self.switch_window()
        sleep()
        return AgreementPage(self.driver)

    def go_SitemapPage(self):
        """点击首页底部-关于本网站-站点地图"""
        self.scroll_to_bottom()
        self.is_click(sekorm['站点地图'])
        self.switch_window()
        sleep()
        return SitemapPage(self.driver)

    def go_EnSekormIndexPage(self):
        """点击首页底部-语言-English，跳转英文站"""
        self.scroll_to_bottom()
        self.is_click(sekorm['English'])
        return EnSekormIndexPage(self.driver)

    def go_AboutPage(self):
        """跳转公司简介"""
        self.scroll_to_bottom()
        self.is_click(sekorm['公司简介'])
        self.switch_window()
        sleep()
        return AboutPage(self.driver)

    def go_CulturePage(self):
        """文化与愿景"""
        self.scroll_to_bottom()
        self.is_click(sekorm['文化与愿景'])
        self.switch_window()
        sleep()
        return CulturePage(self.driver)

    def go_MilestonePage(self):
        """企业里程碑"""
        self.scroll_to_bottom()
        self.is_click(sekorm['企业里程碑'])
        self.switch_window()
        sleep()
        return MilestonePage(self.driver)

    def go_IndexServicePage(self):
        """客户与服务"""
        self.scroll_to_bottom()
        self.is_click(sekorm['客户与服务'])
        self.switch_window()
        sleep()
        return IndexServicePage(self.driver)

    def get_index_showcase(self, elem):
        """获取首页热门橱窗并挨个点击"""
        self.is_click(sekorm[elem])
        self.switch_window()
        return self.get_source

