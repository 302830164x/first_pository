import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils
from utils.times import sleep


@allure.epic('B台')
@allure.feature('B台检查')
class Test_B:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_b_driver(self, b_driver):
        self.b = b_driver
        self.b.get_url(f'{ini.B_Url}/content/sums/home')

    @allure.story("首页")
    def test_go_BIndexPage(self):
        num = self.b.go_BIndexPage().get_BIndexPage_num()
        assert_text = '搜 索'
        assertUtils.assert_greater_equal(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text), assert_text)

    @allure.story("功能介绍")
    def test_go_ProductFunDecPage(self):
        assert_text = '搜 索'
        num = self.b.go_BIndexPage().go_ProductFunDecPage().get_ProductFunDecPage_num()
        assertUtils.assert_greater_equal(num, 20)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text), assert_text)

    @allure.story("个人中心")
    def test_go_UserCenterPage(self):
        self.b.go_UserCenterPage()
        assert_text = '个人信息', '菜单权限清单'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("通讯录")
    def test_go_UserContactPage(self):
        self.b.go_UserContactPage()
        assert_text = '新建', '邮箱：'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("通知中心")
    def test_go_NotifyCenterPage(self):
        num = self.b.go_NotifyCenterPage()
        assert_text = '通知中心'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text), '通知中心标为已读右键全选/取消全选')

    @allure.story("审批中心")
    def test_go_AuditCenterPage(self):
        self.b.go_AuditCenterPage().check_my_submit()
        assert_text = '搜 索'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text), assert_text)

    @allure.story("外出计划")
    def test_go_OutPlanPage(self):
        self.b.go_OutPlanPage()
        assert_text = '联系人', '筛 选'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-全部客户")
    def test_go_CustomerBenchPage(self):
        num = self.b.go_CustomerPage().go_CustomerBenchPage().get_CustomerBenchPage_num()
        assert_text = '编辑', '新建客户'
        assertUtils.assert_greater_equal(num, 5)
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-我的客户")
    def test_go_PrivateCustomerBenchPage(self):
        self.b.go_CustomerPage().go_PrivateCustomerBenchPage()
        assert_text = '客户团队：', '编辑', '世强先进（深圳）科技股份有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-新客户")
    def test_go_CustomerPoolPage(self):
        self.b.go_CustomerPage().go_CustomerPoolPage()
        assert_text = '检 索', '产生时间：'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_contains(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-管制客户-管制查询")
    def test_go_RestrictSearchPage(self):
        self.b.go_CustomerPage().go_RestrictSearchPage()
        assert_text = '管制查询', '检 索'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-客户信用-授信客户")
    def test_go_CreditPaymentPage(self):
        self.b.go_CustomerPage().go_CreditPaymentPage()
        assert_text = '添加客户', '客户名称/姓名', '已激活'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-客户信用-账期订单审核")
    def test_go_PaymentOrderReviewPage(self):
        self.b.go_CustomerPage().go_PaymentOrderReviewPage()
        assert_text = '搜 索', '销售类型', '处理'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-客户信用-核销清单")
    def test_go_WriteOffListPage(self):
        self.b.go_CustomerPage().go_WriteOffListPage()
        assert_text = '筛 选', '企业账户', '手动核销'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-采集信息客户池")
    def test_go_RiskEpPage(self):
        self.b.go_CustomerPage().go_RiskEpPage()
        assert_text = '导入新的客户', '客户名称', '失效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-PCN、EOL通知-客户通知池")
    def test_go_PcneolEmailNotifyPage(self):
        self.b.go_CustomerPage().go_PcneolEmailNotifyPage()
        assert_text = '筛 选', 'PCN标题/客户/物料'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-PCN、EOL通知-未分发客户")
    def test_go_NoPcneolEmailNotifyPage(self):
        self.b.go_CustomerPage().go_NoPcneolEmailNotifyPage()
        assert_text = '筛 选', 'PCN标题/客户/物料', '管理通知人'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-PCN、EOL通知-型号确认池")
    def test_go_PnConfirmPoolPage(self):
        self.b.go_CustomerPage().go_PnConfirmPoolPage()
        assert_text = '检 索', '资料标题'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("客户工作台-活动营销")
    def test_go_SeminarInfoPage(self):
        self.b.go_CustomerPage().go_SeminarInfoPage()
        assert_text = '筛 选', '研讨会/进程/资源', '关联供应商'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("客户工作台-添加移除标签")
    def test_go_EpTagEditPage(self):
        self.b.go_CustomerPage().go_EpTagEditPage()

    @allure.story("供应商工作台-全部供应商")
    def test_go_SupplierBenchPage(self):
        self.b.go_SupplierPage().go_SupplierBenchPage()
        assert_text = '搜 索', '添加', 'PM'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("供应商工作台-我的供应商")
    def test_go_MySupplierBenchPage(self):
        self.b.go_SupplierPage().go_MySupplierBenchPage()
        assert_text = '搜 索', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story("供应商工作台-供应商评价体系")
    def test_go_SupplierEvaluteBenchPoolPage(self):
        self.b.go_SupplierPage().go_SupplierEvaluteBenchPoolPage()
        assert_text = '搜 索', '暂无数据', '提示：(供应商规模、供应商质量投诉、供应商供应问题）右键显示更多操作'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("供应商工作台-邮件模板管理")
    def test_go_MailTemplateManagementPage(self):
        self.b.go_SupplierPage().go_MailTemplateManagementPage()
        assert_text = '筛 选', '模板ID', '正文模板'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("供应商工作台-品牌管理")
    def test_go_BrandManagePage(self):
        self.b.go_SupplierPage().go_BrandManagePage()
        assert_text = '搜 索', '批量导入品牌', '已传递'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("研讨会数据")
    def test_go_SeminarDataPage(self):
        self.b.go_SeminarDataPage()
        assert_text = '检 索', '研讨会名称', '查看'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("采购订单")
    def test_go_PurchasePage(self):
        self.b.go_PurchasePage()
        assert_text = '搜 索', '供应商名称/PO单号/产品型号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-常用外汇汇率")
    def test_go_ForeignExchangeRatePage(self):
        num = self.b.go_PriceQuotationPage().go_ForeignExchangeRatePage().get_ForeignExchangeRatePage_num()
        assert_text = '查 询', '汇率日期'
        assertUtils.assert_equals(num, 50)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-SRP价格")
    def test_go_PriceWorkBenchPage(self):
        self.b.go_PriceQuotationPage().go_PriceWorkBenchPage()
        assert_text = '查 询', 'SRP币种'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-SRP价格(销售)")
    def test_go_PriceWorkBenchForSalerPage(self):
        self.b.go_PriceQuotationPage().go_PriceWorkBenchForSalerPage()
        assert_text = '查 询', 'SRP币种'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-SBC价格")
    def test_go_SbcPage(self):
        self.b.go_PriceQuotationPage().go_SbcPage()
        assert_text = '查 询', '价格类型'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-SRP待办池")
    def test_go_SrpToDoPage(self):
        self.b.go_PriceQuotationPage().go_SrpToDoPage()
        assert_text = '筛 选', '客户名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-SBC待办池")
    def test_go_SbcToDoPage(self):
        self.b.go_PriceQuotationPage().go_SbcToDoPage()
        assert_text = '筛 选', '供应商名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("价格与报价管理-销售报价管理")
    def test_go_OfferApplyPage(self):
        self.b.go_PriceQuotationPage().go_OfferApplyPage()
        assert_text = '新增报价', '报价ID', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("价格与报价管理-市场报价管理")
    def test_go_OfferApplyForMarketPage(self):
        self.b.go_PriceQuotationPage().go_OfferApplyForMarketPage()
        assert_text = '查 询', '报价ID', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("项目工作台－推荐给我的项目/需求")
    def test_go_RecommendProjectPoolPage(self):
        self.b.go_ProjectWorkbenchPage().go_RecommendProjectPoolPage()
        assert_text = '提示：任一栏目右键显示更多操作'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text), assert_text)

    @allure.story("项目工作台－未响应项目/需求")
    def test_go_UnclaimedProjectPoolPage(self):
        self.b.go_ProjectWorkbenchPage().go_UnclaimedProjectPoolPage()
        assert_text = '提示：任一栏目右键显示更多操作', '当前共有', '创建于：'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_contains(self.b.get_assert_text('li', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("项目工作台－优选型号推荐")
    def test_go_RecommendationEnginePage(self):
        num = self.b.go_ProjectWorkbenchPage().go_RecommendationEnginePage().RecommendationEnginePage_search('ROHM')
        assertUtils.assert_equals(num, 10)

    @allure.story("项目工作台－优选型号推荐2")
    def test_go_PnRecommendationPage(self):
        num = self.b.go_ProjectWorkbenchPage().go_RecommendationEnginePage().RecommendationEnginePage_select()
        assert_text = '搜 索'
        assertUtils.assert_equals(num, 10)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text), assert_text)

    @allure.story("项目工作台－全部项目")
    def test_go_ProjectPoolPage(self):
        num = self.b.go_ProjectWorkbenchPage().go_ProjectPoolPage().get_ProjectPoolPage_num()
        assert_text = '搜 索', '客户/项目/方案需求'
        assertUtils.assert_greater_equal(num, 25)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－我的项目")
    def test_go_MyProjectPage(self):
        self.b.go_ProjectWorkbenchPage().go_MyProjectPage()
        assert_text = '搜 索', '客户/项目/方案需求', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("项目工作台－新项目")
    def test_go_NewProjectPage(self):
        num = self.b.go_ProjectWorkbenchPage().go_NewProjectPage().get_NewProjectPage_num()
        assert_text = '搜 索', '客户/项目'
        assertUtils.assert_greater_equal(num, 50)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－全部需求/方案")
    def test_go_ChancePoolPage(self):
        num = self.b.go_ProjectWorkbenchPage().go_ChancePoolPage().get_ChancePoolPage_num()
        assert_text = '筛 选', 'FAE'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－方案分享池")
    def test_go_ChanceSharePoolPage(self):
        self.b.go_ProjectWorkbenchPage().go_ChanceSharePoolPage()
        assert_text = '筛 选', '项目/方案'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("项目工作台－方案进度池")
    # def test_go_ChanceManagementListPage(self):
    #     self.b.go_ProjectWorkbenchPage().go_ChanceManagementListPage()
    #     assert_text = '搜 索', '项目：', '方案团队'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('th', assert_text[2]), assert_text[2])

    @allure.story("项目工作台－项目型号库")
    def test_go_ChancePoolSimplifiedPage(self):
        num = self.b.go_ProjectWorkbenchPage().go_ChancePoolSimplifiedPage().get_ChancePoolSimplifiedPage_num()
        assert_text = '搜 索', '项目名称'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－批量更新DR")
    def test_go_DrProjectImportPage(self):
        self.b.go_ProjectWorkbenchPage().go_DrProjectImportPage()
        assert_text = '批量更新DR信息', '提 交'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－DR处理池")
    def test_go_DrProjectPage(self):
        self.b.go_ProjectWorkbenchPage().go_DrProjectPage()
        assert_text = '筛 选', '项目名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("项目工作台－DR项目")
    def test_go_DrProjectPoolPage(self):
        self.b.go_ProjectWorkbenchPage().go_DrProjectPoolPage()
        assert_text = '+新建项目', '客户/项目/方案', 'KFAE'
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("项目工作台－事务项目")
    def test_go_JobProjectPoolPage(self):
        self.b.go_ProjectWorkbenchPage().go_JobProjectPoolPage()
        assert_text = '+新建项目', '客户/项目/方案', 'TSE'
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("店铺-店铺管理")
    def test_go_ShopPage(self):
        self.b.go_ShopsPage().go_ShopPage()
        assert_text = 'Sekorm Advanced Technology (Shenzhen) Co., Ltd', '切换店铺'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("店铺-售卖管理")
    def test_go_SalesManagementPage(self):
        self.b.go_ShopsPage().go_SalesManagementPage()
        assert_text = '订单配送方式', '确 认'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("商品-商品管理")
    def test_go_CommodityPage(self):
        self.b.go_CommoditiesPage().go_CommodityPage()
        assert_text = '添加商品', '商品型号', '设置'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("商品-库存管理")
    def test_go_StockManagementPage(self):
        self.b.go_CommoditiesPage().go_StockManagementPage()
        assert_text = '库存分配管理', '序号', '商品库存明细'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("商品-商品标签")
    def test_go_LabelManageListPage(self):
        self.b.go_CommoditiesPage().go_LabelManageListPage()
        assert_text = '标签样式', '部署'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("商品-商品促销")
    def test_go_DiscountPage1(self):
        self.b.go_CommoditiesPage().go_DiscountPage()
        assert_text = '新建促销', '促销名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("商品-仓库管理")
    def test_go_StorehouseManagePage(self):
        self.b.go_CommoditiesPage().go_StorehouseManagePage()
        assert_text = '新增仓库', '仓库名称', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("商品-运费管理")
    def test_go_FreightManagePage(self):
        self.b.go_CommoditiesPage().go_FreightManagePage()
        assert_text = '新增运费模板', '运费模板名称', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("服务管理－服务工作台")
    def test_go_ServiceWorkPage(self):
        num = self.b.go_ServiceManagePage().go_ServiceWorkPage().get_ServiceWorkPage_num()
        assert_text = '服务名称', '全选'
        assertUtils.assert_greater_equal(num, 50)
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("服务管理－研发需求池")
    def test_go_ServiceProcessPage(self):
        self.b.go_ServiceManagePage().go_ServiceProcessPage()
        assert_text = '设置分发规则', '世强先进(深圳)科技股份有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("服务管理－商务需求池")
    def test_go_BusinessDemandPage(self):
        self.b.go_ServiceManagePage().go_BusinessDemandPage()
        assert_text = '设置分发规则', '世强先进（深圳）科技股份有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("服务管理－服务新增")
    def test_go_ServicePage(self):
        num = self.b.go_ServiceManagePage().go_ServicePage().get_ServicePage_num()
        assert_text = '新增服务', '请选择服务类型'
        assertUtils.assert_equals(num, 50)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("服务管理－服务部署")
    def test_go_ServiceDeploymentPage(self):
        self.b.go_ServiceManagePage().go_ServiceDeploymentPage()
        assert_text = '世强硬创服务平台中文站', '添加二级货架', '硬创商城'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("服务管理－亚洲服务新增")
    def test_go_EnServicePage(self):
        self.b.go_ServiceManagePage().go_EnServicePage()
        assert_text = '添加服务', '服务ID', '小量快购'
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("服务管理－材料定制")
    def test_go_MaterialCustomPage(self):
        self.b.go_ServiceManagePage().go_MaterialCustomPage()
        assert_text = '公司名称', '会员类型', '服务商会员'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    # @allure.story("服务管理－供应商合作申请")
    # def test_go_EcoPartnersPage(self):
    #     self.b.go_ServiceManagePage().go_EcoPartnersPage()
    #     assert_text = '筛 选', '公司名称', '详情'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("服务管理－招募服务处理")
    # def test_go_RecruitServicePage(self):
    #     self.b.go_ServiceManagePage().go_RecruitServicePage()
    #     assert_text = '筛 选', '服务名称', '处理'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("服务管理－服务未满足")
    # def test_go_SampleUnmetPage(self):
    #     num = self.b.go_ServiceManagePage().go_SampleUnmetPage().get_SampleUnmetPage_num()
    #     assert_text = '筛 选', '企业名称'
    #     assertUtils.assert_equals(num, 200)
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("服务管理－样品申请")
    # def test_go_SampleHandlePage(self):
    #     num = self.b.go_ServiceManagePage().go_SampleHandlePage().get_SampleHandlePage_num()
    #     assert_text = '筛 选', '客户/单号/行号'
    #     assertUtils.assert_greater_equal(num, 200)
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("服务管理－新样品申请")
    # def test_go_ServiceProcessParentChildPage(self):
    #     num = self.b.go_ServiceManagePage().go_ServiceProcessParentChildPage().get_ServiceProcessParentChildPage_num()
    #     assert_text = '筛 选', '客户/主服务/子服务'
    #     assertUtils.assert_greater_equal(num, 50)
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("服务管理－询价&询交期未满足")
    # def test_go_AskPriceUnmetPage(self):
    #     self.b.go_ServiceManagePage().go_AskPriceUnmetPage()
    #     assert_text = '筛 选', '企业名称', '询交期'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])
    #
    # @allure.story("服务管理－选型帮助未满足")
    # def test_go_SelectionUnmetPage(self):
    #     self.b.go_ServiceManagePage().go_SelectionUnmetPage()
    #     assert_text = '筛 选', '跟进状态', '待跟进'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    # @allure.story("服务管理－奖品服务")
    # def test_go_PrizeServicePoolPage(self):
    #     self.b.go_ServiceManagePage().go_PrizeServicePoolPage()
    #     assert_text = '筛 选', '企业名称', '已领取'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("服务管理－呼叫系统")
    def test_go_CallCenter(self):
        self.b.go_ServiceManagePage().go_CallCenter()
        assert_text = '呼叫记录', '呼叫类型', '已完成'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("服务管理－客服坐席管理")
    def test_go_CallCenterAgentManage(self):
        self.b.go_ServiceManagePage().go_CallCenterAgentManage()
        assert_text = '+新增坐席', '坐席号码', '失效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("服务管理－资源工作台")
    def test_go_ResourceWorkbench(self):
        self.b.go_ServiceManagePage().go_ResourceWorkbench()
        assert_text = '筛 选', '企业/资源/名称', '车辆'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("服务管理－中车EDI")
    def test_go_MidCarEDIList(self):
        self.b.go_ServiceManagePage().go_MidCarEDIList()
        assert_text = '同步数据', '客户订单号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("服务管理－服务记录－记录查询")
    def test_go_SrSelPage(self):
        self.b = self.b.go_ServiceManagePage().go_SrSelPage()
        assert_text = '服务记录查询', '新增服务记录'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        self.b.close_driver().refresh()

    @allure.story("服务管理－服务记录－记录导入")
    def test_go_SrImptPage(self):
        self.b.go_ServiceManagePage().go_SrImptPage()
        assert_text = '服务记录导入', '上传文件'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("服务管理－服务记录－服务类型管理")
    def test_go_SrTypePage(self):
        self.b.go_ServiceManagePage().go_SrTypePage()
        assert_text = '新 增', '系统类型', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("选型帮助－新增选型帮助")
    # def test_go_NewSelectionPage(self):
    #     self.b.go_SelectionPage().go_NewSelectionPage()
    #     assert_text = '公司名称', '批量通过', '不通过'
    #     assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("选型帮助－选型帮助技术处理池")
    # def test_go_PassedSelectionPage(self):
    #     self.b.go_SelectionPage().go_PassedSelectionPage()
    #     assert_text = '公司名称', '服务名称', '已处理'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])
    #
    # @allure.story("选型帮助－选型帮助商务处理池")
    # def test_go_BusinessSelectionPage(self):
    #     self.b.go_SelectionPage().go_BusinessSelectionPage()
    #     assert_text = '公司名称', '服务名称', '已处理'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    # @allure.story("选型帮助－不通过选型帮助")
    # def test_go_NotPassedSelectionPage(self):
    #     self.b.go_SelectionPage().go_NotPassedSelectionPage()
    #     assert_text = '公司名称', '服务名称', '查看'
    #     assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("替代推荐－新增替代推荐")
    def test_go_NewReplaceRecommendPage(self):
        self.b.go_ReplaceRecommendPage().go_NewReplaceRecommendPage()
        assert_text = '公司名称', '批量通过'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("替代推荐－替代推荐处理池")
    def test_go_NewReplaceRecommendPage(self):
        self.b.go_ReplaceRecommendPage().go_NewReplaceRecommendPage()
        assert_text = '公司名称', '项目名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("替代推荐－替代推荐商务处理池")
    def test_go_PassedReplaceRecommendPage(self):
        self.b.go_ReplaceRecommendPage().go_PassedReplaceRecommendPage()
        assert_text = '公司名称', '项目名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("替代推荐－不通过替代推荐")
    def test_go_NotPassedReplaceRecommendPage(self):
        self.b.go_ReplaceRecommendPage().go_NotPassedReplaceRecommendPage()
        assert_text = '公司名称', '项目名称'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
