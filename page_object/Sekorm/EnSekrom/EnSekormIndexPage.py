from common.readconfig import ini
from common.readelement import Element
from page_object.Sekorm.EnSekrom.EnCooperationPage import EnCooperationPage
from page_object.Sekorm.EnSekrom.EnDocDetailPage import EnDocDetailPage
from page_object.Sekorm.EnSekrom.EnNewsDetailPage import EnNewsDetailPage
from page_object.Sekorm.EnSekrom.EnNewsPage import EnNewsPage
from page_object.Sekorm.EnSekrom.EnOnPage import EnOnPage
from page_object.Sekorm.EnSekrom.EnSearchPage import EnSearchPage
from page_object.Sekorm.EnSekrom.EnSupplyPage import EnSupplyPage
from page_object.Sekorm.EnSekrom.EnSupplySearchPage import EnSupplySearchPage
from page_object.Sekorm.EnSekrom.EnUserListPage import EnUserListPage
from page_object.Sekorm.EnSekrom.EnUserOrderPage import EnUserOrderPage
from page_object.Sekorm.SekormCommon import SekormCommon

sekorm = Element('SekormElement')
Locator = {
    '英文站新产品页': ('xpath', "//a[@id='search_new_product']"),
    '英文站商城页': ('xpath', "//a[@id='search_shopping_mall']"),
    '英文站合作页': ('xpath', "//a[@id='supplier_cooperation']"),
    '英文站购物车': ('xpath', "//span[@class='shopping-cart']"),
    '英文站我的订单': ('xpath', "//a[@id='header_user_unloginStatus']"),
    '登录': ('xpath', "//a[normalize-space()='Sign in / Register']"),
    '登录按钮': ('xpath', "//input[@id='btn_login']"),
    '登录提示': ('xpath', "//p[@class='form-error-msg']"),
    '登录弹窗关闭按钮': ('xpath', "//span[@class='modal-closeBtn']"),
    '搜索框': ('xpath', "//input[@id='searchText']"),
    '搜索按钮': ('xpath', "//input[@id='searchBtn']"),
    '品牌墙翻页': ('xpath', "//i[@id='swiper_brand_next']"),
    '品牌墙页数': ('xpath', "//em[@id='brand_now_page1']"),
    '品牌墙': ('xpath', "(//div[@class='brand-cont'])[3]/a[1]"),
    '首页楼层': ('xpath', "//a[contains(text(),'Electronic News')]"),
    '首页资讯': ('xpath', "(//div[@class='listBox-text'])[1]//a"),
    '首页资讯图片': ('xpath', "//div[@class='listBox-item-v pull-left']//img"),
    'About Us': ('xpath', "//a[normalize-space()='About Us']"),
    'Contact Us': ('xpath', "//a[normalize-space()='Contact Us']"),
    'Supplier Cooperation': ('xpath', "//a[normalize-space()='Supplier Cooperation']"),
    'Chinese': ('xpath', "//a[normalize-space()='Chinese']"),
}


class EnSekormIndexPage(SekormCommon):
    """英文站首页"""

    def go_EnNewsPage(self):
        """跳转英文站新产品页"""
        self.is_click(Locator['英文站新产品页'])
        return EnNewsPage(self.driver)

    def go_EnSupplyPage(self):
        """跳转英文站商城页"""
        self.is_click(Locator['英文站商城页'])
        return EnSupplyPage(self.driver)

    def go_EnCooperationPage(self):
        """跳转英文站合作页"""
        self.is_click(Locator['英文站合作页'])
        return EnCooperationPage(self.driver)

    def go_EnSearchPage(self, text):
        """跳转英文站搜索结果页"""
        self.input_text(Locator['搜索框'], text)
        self.is_click(Locator['搜索按钮'])
        return EnSearchPage(self.driver)

    def go_EnSupplySearchPage(self, text):
        """跳转英文站商城垂直搜索结果页"""
        self.is_click(Locator['英文站商城页'])
        self.input_text(Locator['搜索框'], text)
        self.is_click(Locator['搜索按钮'])
        return EnSupplySearchPage(self.driver)

    def go_EnUserListPage(self):
        """跳转英文站购物车"""
        self.is_click(Locator['英文站购物车'])
        return EnUserListPage(self.driver)

    def go_EnUserOrderPage(self):
        """跳转英文站我的订单"""
        self.is_click(Locator['英文站我的订单'])
        return EnUserOrderPage(self.driver)

    def go_EnNewsDetailPage_by_id(self):
        """通过ID跳转英文站资讯详情页"""
        self.get_url(f'{ini.EnSekormUrl}/news/21379942.html')
        return EnNewsDetailPage(self.driver)

    def go_EnDocDetailPage_by_id(self):
        """通过ID跳转英文站资料详情页"""
        self.get_url(f'{ini.EnSekormUrl}/doc/523059989.html')
        return EnDocDetailPage(self.driver)

    def go_EnOnPage_by_id(self):
        """通过ID跳转英文站ON详情页"""
        self.get_url(f'{ini.EnSekormUrl}/product/500097773.html')
        return EnOnPage(self.driver)

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
        self.is_click(sekorm['首页轮播图'])
        self.switch_window()
        return EnNewsDetailPage(self.driver)

    def click_brand(self):
        """点击首页品牌墙"""
        self.is_click(Locator['品牌墙翻页'])
        num = self.element_text(Locator['品牌墙页数'])
        self.is_click(Locator['品牌墙'])
        self.switch_window()
        return int(num), EnSearchPage(self.driver)

    def click_index_showcase(self):
        """点击首页楼层"""
        self.is_click(Locator['首页楼层'])
        self.switch_window()
        return EnNewsPage(self.driver)

    def click_index_news(self):
        """点击首页资讯"""
        self.is_click(Locator['首页资讯'])
        self.switch_window()
        return EnNewsDetailPage(self.driver)

    def check_index_news_img(self):
        """点击首页资讯"""
        size = self.img_show(Locator['首页资讯图片'])
        self.is_click(Locator['首页资讯图片'])
        self.switch_window()
        return size, EnNewsDetailPage(self.driver)

    def click_about_us(self):
        """点击About Us"""
        self.is_click(Locator['About Us'])
        self.switch_window()

    def click_contact_us(self):
        """点击Contact Us"""
        self.is_click(Locator['Contact Us'])
        self.switch_window()

    def click_supplier_cooperation(self):
        """点击Contact Us"""
        self.is_click(Locator['Supplier Cooperation'])
        self.switch_window()
        return EnCooperationPage(self.driver)

    def click_Chinese(self):
        """点击Chinese"""
        from page_object.Sekorm.SekormIndexPage import SekormIndexPage
        self.is_click(Locator['Chinese'])
        return SekormIndexPage(self.driver)

    def un_login_click_en_top(self, elm):
        """未登录-点击首页顶部各个触发登录的元素"""
        self.is_click(Locator[elm])
        self.is_click(Locator['登录按钮'])
        text = self.element_text(Locator['登录提示'])
        self.is_click(Locator['登录弹窗关闭按钮'])
        return text
