import allure
import pytest
from utils.assertUtils import assertUtils


@allure.epic('前台')
@allure.feature('前台首页')
class Test_Sekorm:

    # # 首页登录
    # @pytest.fixture(scope='class', autouse=True)
    # def set_sekorm_login(self, sekorm_driver):
    #     self.sekorm = sekorm_driver
    #     self.sekorm.get_login()

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.sekorm.go_SekormIndexPage()
        yield
        self.sekorm.close_driver()

    @allure.story("首页-检查登录、退出登录")
    def test_check_login_quit(self):
        self.sekorm.get_login().quit_login()
        assert_text = '登录', '注册'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("首页-检查title、热门是否高亮")
    def test_click_hot(self):
        self.sekorm.go_HotPage()
        assertUtils.assert_contains(self.sekorm.get_title(), '全球领先的研发服务平台')
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('热门', 'class'), 'index nav-active')

    @allure.story("首页-轮播图切换")
    def test_switch_banner(self):
        size1, size2, size3, size4 = self.sekorm.go_HotPage().banner_change()
        assertUtils.assert_equals(size1, (1200, 680))
        assertUtils.assert_equals(size2, (1200, 680))
        assertUtils.assert_equals(size3, (1200, 680))
        assertUtils.assert_equals(size4, (1200, 680))

    @allure.story("首页-轮播图点击")
    def test_click_banner(self):
        self.sekorm.go_HotPage().click_banner()
        url = self.sekorm.driver.current_url
        assertUtils.assert_contains(url, ('adSeat=webBanner', 'adPack=webHot', 'adp4'))

    @allure.story("首页-检查1000家banner")
    def test_check_webRightBanner1(self):
        size, BrandsPage = self.sekorm.go_HotPage().check_webRightBanner1()
        BrandsPage.check_BrandsPage()
        assertUtils.assert_equals(size, (1180, 440))

    @allure.story("首页-研发服务banner")
    def test_check_webRightBanner2(self):
        size, Tab11Page = self.sekorm.go_HotPage().check_webRightBanner2()
        num = Tab11Page.check_tab11_list_num()
        assertUtils.assert_equals(size, (580, 220))
        assertUtils.assert_greater_equal(num, 7)

    @allure.story("首页-供应服务banner")
    def test_check_webRightBanner3(self):
        size, Tab11Page = self.sekorm.go_HotPage().check_webRightBanner3()
        num = Tab11Page.check_tab11_list_num()
        assertUtils.assert_equals(size, (580, 220))
        assertUtils.assert_greater_equal(num, 7)

    @allure.story('首页-点击首页橱窗')
    @pytest.mark.parametrize('showCase', ['首页热门橱窗', '首页新技术橱窗', '首页电子商城橱窗'])
    def test_index_showcase(self, showCase):
        text = self.sekorm.get_index_showcase(showCase)
        assertUtils.assert_contains_one(text, ('为您推荐以下相关内容', '电子商城'))

    @allure.story("首页-楼层广告")
    @pytest.mark.parametrize('elm', ['楼层广告1', '楼层广告2', '楼层广告3', '楼层广告4'])
    def test_check_check_webFloor_advertise(self, elm):
        size, Tab11Page = self.sekorm.go_HotPage().check_webFloor_advertise(elm)
        num = Tab11Page.check_tab11_list_num()
        assertUtils.assert_equals(size, (1192, 200))
        assertUtils.assert_greater_equal(num, 12)

    @allure.story("首页-热门楼层内容")
    def test_check_webFloor_hot(self):
        size, NewsDetailPage = self.sekorm.go_HotPage().check_webFloor_hot()
        NewsDetailPage.check_news_detail_layout()
        assertUtils.assert_equals(size, (180, 130))

    @allure.story("首页-新技术楼层内容")
    def test_check_webFloor_news(self):
        size, NewsDetailPage = self.sekorm.go_HotPage().check_webFloor_news()
        NewsDetailPage.check_news_detail_layout()
        assertUtils.assert_equals(size, (180, 130))

    @allure.story("首页-电子商城楼层内容")
    def test_check_webFloor_supply(self):
        size, SupplySearchPage = self.sekorm.go_HotPage().check_webFloor_supply()
        text = SupplySearchPage.get_search_text()
        assertUtils.assert_equals(size, (160, 80))
        assertUtils.assert_equals(text, 'TDK InvenSense')

    @allure.story("首页-技术资料楼层内容")
    def test_check_webFloor_doc(self):
        size, DocDetailPage = self.sekorm.go_HotPage().check_webFloor_doc()
        DocDetailPage.check_doc_detail_layout()
        assertUtils.assert_equals(size, (180, 130))

    @allure.story("首页-加工定制楼层内容")
    def test_check_webFloor_customize(self):
        size, ServiceCommPage = self.sekorm.go_HotPage().check_webFloor_customize()
        assertUtils.assert_equals(size, (364, 324))
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', '获取验证码'), '获取验证码')

    @allure.story("首页-技术问答楼层内容")
    def test_check_webFloor_faq(self):
        FaqDetailPage = self.sekorm.go_HotPage().check_webFloor_faq()
        FaqDetailPage.check_layout()

    @allure.story("首页-采购服务楼层内容")
    def test_check_webFloor_procurement(self):
        size, NewsDetailPage = self.sekorm.go_HotPage().check_webFloor_procurement()
        NewsDetailPage.check_news_detail_layout()
        assertUtils.assert_equals(size, (364, 324))

    @allure.story("首页-合作楼层内容")
    def test_check_webFloor_cooperate(self):
        size, NewsDetailPage = self.sekorm.go_HotPage().check_webFloor_cooperate()
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', '获取验证码'), '获取验证码')
        assertUtils.assert_equals(size, (364, 324))

    @allure.story("首页-授权品牌楼层内容")
    def test_check_webFloor_supply(self):
        size, BrandSearchPage = self.sekorm.go_HotPage().check_webFloor_brands()
        assert BrandSearchPage.if_brand_to_top()
        assertUtils.assert_equals(size, (160, 80))

    @allure.story("首页-未登录-点击顶部")
    @pytest.mark.parametrize('elm', ['型号清单', '购买清单', '登录', '注册'])
    def test_Unlogin_click_top(self, elm):
        self.UnLoginPage = self.sekorm.go_HotPage().Unlogin_click_top(elm)
        text = self.UnLoginPage.check_login_layout()
        assertUtils.assert_equals(text, '未注册的手机号验证后，将自动创建为账号')
        self.UnLoginPage.close_login()

    @allure.story("首页-未登录-楼层-个人中心")
    @pytest.mark.parametrize('elm', ['个人中心'])
    def test_Unlogin_click_bottom(self, elm):
        self.UnLoginPage = self.sekorm.go_HotPage().Unlogin_click_bottom(elm)
        text = self.UnLoginPage.check_login_layout()
        assertUtils.assert_equals(text, '未注册的手机号验证后，将自动创建为账号')
        self.UnLoginPage.close_login()

    @allure.story("首页-未登录-历史记录模块")
    def test_Unlogin_click_history(self):
        self.sekorm.go_HotPage().Unlogin_click_history()
        assert_text = '所属国家/地区'
        assertUtils.assert_equals(self.sekorm.get_assert_text('label', assert_text), assert_text)
        self.sekorm.get_back()

    @allure.story("首页底部-关于本网站-各个协议")
    @pytest.mark.parametrize('elm', ['世强硬创平台使用许可协议', '世强硬创平台隐私政策', '世强硬创平台出口声明'])
    def test_go_AgreementPage(self, elm):
        self.sekorm.go_AgreementPage(elm)
        assertUtils.assert_equals(self.sekorm.get_assert_text('h3', elm), elm)

    @allure.story("首页底部-关于本网站-站点地图")
    @pytest.mark.parametrize('elm', ['商品导航', '品牌导航'])
    def test_go_SitemapPage(self, elm):
        self.sekorm.go_SitemapPage()
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', elm), elm)

    @allure.story("首页底部-语言-English")
    def test_go_EnSekormIndexPage(self):
        self.sekorm.go_EnSekormIndexPage()
        assertUtils.assert_contains(self.sekorm.get_title(), 'Services Platform – Sekorm')
        assert_text = 'Shopping Cart'
        assertUtils.assert_equals(self.sekorm.get_assert_text('a', assert_text), assert_text)
        self.sekorm.get_back()

    @allure.story("首页-底部版权")
    def test_check_bottom(self):
        self.sekorm.scroll_to_bottom()
        assertUtils.assert_contains(self.sekorm.get_assert_text('span', '版权所有'), ('版权所有', '1998-', '深圳市世强元件网络有限公司'))
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('备案号', 'href'),
                                  'https://beian.miit.gov.cn/#/Integrated/recordQuery')
        assertUtils.assert_equals(self.sekorm.get_elm_attribute('许可证', 'href'),
                                  'https://tsm.miit.gov.cn/dxxzsp/xkz/xkzgl/resource/qiyesearch.jsp?'
                                  'num=%E7%B2%A4B2-20200964&type=xuke')

    @allure.story("首页-悬浮按钮文本检查")
    @pytest.mark.parametrize('elm,kind,text', [('悬浮按钮-研发客服', 'div', '微信一对一服务，研发客服为您提供疑难解答和技术支持'),
                                               ('悬浮按钮-商务客服', 'div', '微信一对一服务，商务客服为您解答样品、价格、交期、订单、发票等商务相关问题'),
                                               ('悬浮按钮-服务热线', 'p', 'contact@sekorm.com')])
    def test_check_floating_text(self, elm, kind, text):
        self.sekorm.go_HotPage().check_floating_text(elm)
        assertUtils.assert_contains(self.sekorm.get_assert_text(kind, text), text)

    # @allure.story("登录-首页-悬浮按钮点击检查")
    # @pytest.mark.parametrize('elm', ['悬浮按钮-研发客服', '悬浮按钮-商务客服'])
    # def test_click_floating(self, elm):
    #     url = self.sekorm.go_HotPage().click_floating(elm)
    #     assertUtils.assert_contains(url, 'https://work.weixin.qq.com/kfid/')
    #     assertUtils.assert_equals(self.sekorm.get_assert_text('a', '下载微信'), '下载微信咨询客服')

    @allure.story("未登录-首页-悬浮按钮点击检查")
    @pytest.mark.parametrize('elm', ['悬浮按钮-研发客服', '悬浮按钮-商务客服', '悬浮按钮-收藏'])
    def test_click_floating(self, elm):
        self.UnLoginPage = self.sekorm.go_HotPage().click_floating(elm)
        assert_text = self.UnLoginPage.close_login()
        assertUtils.assert_equals(assert_text, '所属国家/地区')

    @allure.story("进入代理品牌")
    def test_007(self):
        num1, num2, size = self.sekorm.go_BrandsPage().check_BrandsPage()
        assertUtils.assert_equals(num1, 12)
        assertUtils.assert_equals(num2, 12)
        assertUtils.assert_equals(size, (180, 130))

    @allure.story("进入代理品牌搜索结果页")
    def test_go_BrandSearchPage(self):
        text = self.sekorm.go_BrandsPage().go_BrandSearchPage('epson').get_search_text()
        assertUtils.assert_equals(text, 'epson')

    @allure.story("进入技术资料搜索结果页")
    def test_go_DocSearchPage(self):
        text = self.sekorm.go_DocSearchPage('epson').get_search_text()
        assertUtils.assert_equals(text, 'epson')

    @allure.story("进入采购服务")
    def test_009(self):
        num = self.sekorm.go_Tab11_Purchasing().check_tab11_list_num()
        assertUtils.assert_greater_equal(num, 12)

    @allure.story("进入合作")
    def test_0010(self):
        Tab11Page = self.sekorm.go_Tab11_Cooperation()
        num = Tab11Page.check_tab11_list_num()
        size = Tab11Page.check_img_show('合作页-Logo')
        assertUtils.assert_greater_equal(num, 5)
        assertUtils.assert_equals(size, (2400, 300))

    @allure.story("进入新技术-EDA软件")
    def test_0011(self):
        Tab11Page = self.sekorm.go_Tab11_Page()
        num = Tab11Page.check_tab11_list_num()
        assertUtils.assert_greater_equal(num, 12)

    @allure.story("进入电子商城-IC")
    def test_0012(self):
        Tab12Page = self.sekorm.go_Tab12_Page()
        num = Tab12Page.check_tab12_list_num()
        assertUtils.assert_greater_equal(num, 50)

    @allure.story("进入热门-汽车电子")
    def test_0013(self):
        Tab13Page = self.sekorm.go_Tab13_Page()
        num = Tab13Page.check_tab13_list_num()
        assertUtils.assert_greater_equal(num, 12)

    @allure.story("进入公司简介")
    def test_go_AboutPage(self):
        size, text = self.sekorm.go_AboutPage().check_AboutPage()
        assertUtils.assert_equals(size, (240, 144))
        assertUtils.assert_equals(text, '应用创新')

    @allure.story("进入文化与愿景")
    def test_go_CulturePage(self):
        text = self.sekorm.go_CulturePage().check_CulturePage()
        assertUtils.assert_contains(text, ('企业愿景', '世强将继续致力于成为中国最好、最具知名度与竞争力的元器件及测试测量仪器分销商'))

    @allure.story("进入企业里程碑")
    def test_go_MilestonePage(self):
        self.sekorm.go_MilestonePage()
        assert_text = 'SEKORM+世强硬创平台O2O智能硬件创新服务平台成功上线', '世强在深圳成立，成为HP半导体元件（ AVAGO）分销商'
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('li', assert_text[1]), assert_text[1])

    @allure.story("进入客户与服务")
    def test_go_IndexServicePage(self):
        self.sekorm.go_IndexServicePage()
        assert_text = '创新服务', '强大的“三位一体”全服务链团队'
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.sekorm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("进入联系我们")
    def test_go_Connect_NewsDetail(self):
        title, time = self.sekorm.go_Connect_NewsDetail().check_news_detail_layout()
        assertUtils.assert_equals(title, '世强（Sekorm）办公地址')
        assertUtils.assert_contains(time, ('时间', '2024'))


if __name__ == '__main__':
    pytest.main(['test_sekorm.py', '-s'])
