import allure
import pytest
from utils.assertUtils import assertUtils
from utils.logger import log


@allure.epic('前台')
@allure.feature("ON详情页")
class Test_On:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_sekorm_driver(self, sekorm_driver):
        self.sekorm = sekorm_driver
        self.onPage = self.sekorm.go_OnPage_byID(23021019)
        yield
        self.sekorm.close_driver()

    @allure.story("ON详情页-检查ON详细页各个模块")
    def test_check_ON(self):
        list1 = self.onPage.check_ON()
        list2 = ['C8051F390-A-GMR', '品牌：SILICON LABS', '规格参数', '资料下载', '电子商城', '现货市场', '相关研发服务和供应服务']
        assertUtils.assert_equals(list1, list2)

    @allure.story("ON详情页-检查TDK")
    def test_check_TDK(self):
        T, D, K = self.onPage.check_TDK()
        assertUtils.assert_contains(T, ('C8051F390-A-GMR', 'SILICON LABS'))
        assertUtils.assert_contains(D, ('8051,50MHz,16kB', 'MCU'))
        assertUtils.assert_contains(K, ('C8051F390-A-GMR', 'C8051F'))

    @allure.story("ON详情页-检查规格参数字段")
    def test_check_detail(self):
        list1 = self.onPage.check_detail()
        list2 = ['C8051F390-A-GMR', 'SILICON LABS', 'C8051F390;C8051F390-A-GM;C8051F39x;C8051;C8051F',
                 'Mixed-Signal MCU', '8051,50MHz,16kB 8-bit MCU.', 'QFN24', '1,500', '', '有效(ACTIVE)', '',
                 'Frequency(MHz)', 'Flash (kB)', 'RAM (kB)', 'Comparators(个)', 'UART(个)', 'SPI(个)', 'I2C(个)',
                 'Vdd (min)', 'Vdd (max)']
        assertUtils.assert_equals(list1, list2)

    @allure.story("ON详情页-未登录检查发送邮箱、加入型号清单按钮、资料下载列表的预览、下载按钮")
    @pytest.mark.parametrize('elm', ['研发服务', '商务客服', '加入到型号清单', '预览', '下载'])
    def test_unlogin_check_button(self, elm):
        self.UnLoginPage = self.onPage.unlogin_click(elm)
        assert_text = '所属国家/地区'
        assertUtils.assert_equals(self.UnLoginPage.get_assert_text('label', assert_text), assert_text)
        self.UnLoginPage.close_login()

    @allure.story("ON详情页-检查点击资料下载列表的资料标题")
    def test_click_doc_title(self):
        doc_title = self.onPage.click_doc_title()
        assertUtils.assert_equals(self.onPage.get_assert_text('span', doc_title), doc_title)

    @allure.story("ON详情页-检查资料数量、加载更多")
    def test_check_doc_num(self):
        assertUtils.assert_equals(self.onPage.check_doc_num(), (12, 24))

    @allure.story("ON详情页-检查商城模块字段")
    def test_check_on_supply(self):
        text1, text2 = self.onPage.check_on_supply()
        assertUtils.assert_equals(text1, '授权代理商：世强先进（深圳）科技股份有限公司')
        assertUtils.assert_contains(text2, '当天发货')

    @allure.story("ON详情页-检查市场模块字段")
    def test_check_on_mall(self):
        text1, text2 = self.onPage.check_on_mall()
        assertUtils.assert_equals(text1, '认证企业：武汉联特科技股份有限公司')
        assertUtils.assert_contains(text2, ('约', '工作日'))

    @allure.story("ON详情页-未登录检查'小量快购', '批量询价', '交期查询', '样品申请', '下单购买'按钮")
    @pytest.mark.parametrize('elm,text', [('ON详情页-商城-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应'),
                                          ('批量询价', '请提交您需要查询的产品型号、厂牌、数量等信息，世强提供大批量采购在线报价服务'),
                                          ('交期查询', '根据您的项目以及所需型号、厂牌、数量等信息，世强客服在1个工作日内响应，提供在线回复交期服务'),
                                          ('样品申请', '请提交您需要申请的样品型号、品牌、数量、项目信息，样品需求由原厂审核正品保证，世强会努力协助您获批'),
                                          ('ON详情页-市场-购买', '支持小批量采购，最低1PCS起订，快速发货，工作日1小时内专属客服响应。')])
    def test_unlogin_supply_service(self, elm, text):
        text1, self.UnLoginPage = self.onPage.unlogin_click_service(elm)
        text2 = self.UnLoginPage.close_login()
        assertUtils.assert_contains(text1, text)
        assertUtils.assert_equals(text2, '所属国家/地区')

    @allure.story("ON详情页-检查期货订购服务")
    def test_on_go_FuturesPage(self):
        FuturesPage = self.onPage.get_login().go_FuturesPage()
        FuturesPage.check_futures_join_cart()
        on_name, brand_name = FuturesPage.check_on_brand()
        assert on_name, "型号不为空"
        assert brand_name, "厂牌不为空"

    @allure.story("ON详情页-检查相关服务模块")
    @pytest.mark.parametrize('elm,text', [('技术问答', '请输入您要提问内容，世强及原厂FAE将尽力给您提供疑难解答和技术支持'),
                                          ('选型帮助', '请补充您需要选型的产品及参数要求，世强和原厂的技术专家为您推荐功能、价格、供应最优的产品，协助您快速完成设计'),
                                          ('设计方案', '请补充您的方案需求，世强和原厂的应用技术专家提供从元器件、接插件及结构件、组部件到电子材料的整体最优选择'),
                                          ('研发服务', '提交您项目研发过程中遇到的困难，不限于方案定型、器件替代、仿真设计、软件调试、测试方案、编程校准、加工定制建议等'),
                                          ('资料下载', '请提交您需要的资料信息(厂牌/型号/系列/类型)')])
    def test_click_common_service(self, elm, text):
        self.ServiceCommPage, assert_text = self.onPage.click_common_service(elm)
        assertUtils.assert_contains(assert_text, (elm, text))
        assertUtils.assert_equals(self.ServiceCommPage.get_assert_text('span', elm), elm)
