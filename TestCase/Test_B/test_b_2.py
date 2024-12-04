import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils


@allure.epic('B台')
@allure.feature('B台检查_2')
class Test_B:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_b_driver(self, b_driver):
        self.b = b_driver
        self.b.get_url(f'{ini.B_Url}/content/sums/home')

    @allure.story("ON管理－ON管理")
    def test_go_OnManagePage(self):
        self.b.go_CommodityManagePage().go_OnManagePage()
        assert_text = '批量导入', '产品线', '修改'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－ON服务商信息")
    def test_go_OnSpManagePage(self):
        self.b.go_CommodityManagePage().go_OnSpManagePage()
        assert_text = '批量导入', '物料状态', '修改'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－ON多语言管理")
    def test_go_MultiLangOnManagePage(self):
        self.b.go_CommodityManagePage().go_MultiLangOnManagePage()
        assert_text = '批量导入', '序号', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－ON服务商信息Ex")
    def test_go_MultiLangOnSpManagePage(self):
        self.b.go_CommodityManagePage().go_MultiLangOnSpManagePage()
        assert_text = '批量导入', '序号', '修改'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－ON审核")
    def test_go_MultiLangOnVerifyPage(self):
        self.b.go_CommodityManagePage().go_MultiLangOnVerifyPage()
        assert_text = '批量审核', '序号', '审核'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("ON管理－资料关联ON")
    def test_go_OnDocPage(self):
        self.b.go_CommodityManagePage().go_OnDocPage()
        assert_text = '上传资料', '序号', '查看'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("ON管理－型号参数校对")
    # def test_go_OnTransPage(self):
    #     self.b.go_CommodityManagePage().go_OnTransPage()
    #     assert_text = '规格参数字段校对', '序号', '确认'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－ON重量和尺寸维护")
    def test_go_OnWeightSizePage(self):
        self.b.go_CommodityManagePage().go_OnWeightSizePage()
        assert_text = '批量导入', '序号', '设置'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("ON管理－库存管理")
    # def test_go_SaleProxyPage(self):
    #     self.b.go_CommodityManagePage().go_SaleProxyPage()
    #     assert_text = '导入库存', '序号', '设置'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－预期库存检查表")
    def test_go_DynamictablePage(self):
        self.b.go_CommodityManagePage().go_DynamictablePage()
        assert_text = '搜 索', '产品线'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("ON管理－库存检查")
    def test_go_OnInventoryCheckPage(self):
        self.b.go_CommodityManagePage().go_OnInventoryCheckPage()
        assert_text = '筛 选', '序号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("ON管理－快购设置")
    # def test_go_SupplySetPage(self):
    #     self.b.go_CommodityManagePage().go_SupplySetPage()
    #     assert_text = '快购导入', '序号', '设置'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("ON管理－促销管理")
    # def test_go_DiscountPage2(self):
    #     self.b.go_CommodityManagePage().go_DiscountPage()
    #     assert_text = '创建促销', '促销名称', '详情'
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("ON管理－客户物料")
    def test_go_CustomerMaterialPage(self):
        self.b.go_CommodityManagePage().go_CustomerMaterialPage()
        assert_text = '新增客户物料', '客户/客户物料', '生效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("ON管理－交易受限型号")
    def test_go_RestrictPage(self):
        num = self.b.go_CommodityManagePage().go_RestrictPage().get_RestrictPage_num()
        assert_text = '历史操作记录', 'EUS'
        assertUtils.assert_greater_equal(num, 20)
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("ON管理－发货地管理")
    # def test_go_DeliveryAddrPage(self):
    #     self.b.go_CommodityManagePage().go_DeliveryAddrPage()
    #     assert_text = '新增发货地', '序号', '成都仓'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("ON管理－第一次消费ON清单")
    def test_go_OnFirstConsumePage(self):
        num = self.b.go_CommodityManagePage().go_OnFirstConsumePage().get_OnFirstConsumePage_num()
        assert_text = '筛 选', '来源类型'
        assertUtils.assert_greater_equal(num, 1)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("ON管理－第一次消费ON待办池")
    def test_go_OnFirstConsumeToDoPage(self):
        self.b.go_CommodityManagePage().go_OnFirstConsumeToDoPage()
        assert_text = '筛 选', '来源类型'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    # @allure.story("ON管理－我的文件库")
    # def test_go_MyFilePage(self):
    #     self.b.go_CommodityManagePage().go_MyFilePage()
    #     assert_text = '序号', '数据导入', '编辑'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("ON管理－ON工作台")
    # def test_go_OnWorkPage(self):
    #     self.b.go_CommodityManagePage().go_OnWorkPage()
    #     assert_text = '查找ON', '序号'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("ON管理－新增数据查询")
    # def test_go_PreScreeningPage(self):
    #     self.b.go_CommodityManagePage().go_PreScreeningPage()
    #     assert_text = '数据保存', '序号'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("订单与应收管理－我的订单")
    def test_go_MyOrderWorkbenchPage(self):
        self.b.go_OrderManagePage().go_MyOrderWorkbenchPage()
        assert_text = '搜 索', '暂无数据，请使用搜索功能查找相关数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story("订单与应收管理－潜在异常")
    def test_go_UnusualOrderPage(self):
        self.b.go_OrderManagePage().go_UnusualOrderPage()
        assert_text = '筛 选', '订单号', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("订单与应收管理－问题供应")
    def test_go_ProblemSupplyPage(self):
        self.b.go_OrderManagePage().go_ProblemSupplyPage()
        assert_text = '筛 选', '产品线'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("订单与应收管理－问题订单")
    def test_go_OrderWorkbenchProblemPage(self):
        self.b.go_OrderManagePage().go_OrderWorkbenchProblemPage()
        assert_text = '筛 选', '订单类型', '订单号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    # @allure.story("订单与应收管理－我的小量快购订单")
    # def test_go_MyOrderPage(self):
    #     self.b.go_OrderManagePage().go_MyOrderPage()
    #     assert_text = '筛 选', '订单号', '已取消'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    # @allure.story("订单与应收管理－小量快购订单池")
    # def test_go_OrderPerformPage(self):
    #     self.b.go_OrderManagePage().go_OrderPerformPage()
    #     assert_text = '筛 选', '订单号', '已付款'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("订单与应收管理－SO待办池")
    def test_go_OrderWorkbenchSoToDoPage(self):
        self.b.go_OrderManagePage().go_OrderWorkbenchSoToDoPage()
        assert_text = '筛 选', '订单号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("订单与应收管理－物流信息查询")
    def test_go_LogisticsInfoPage(self):
        self.b.go_OrderManagePage().go_LogisticsInfoPage()
        assert_text = '搜 索', '单据类型', '订单号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("订单与应收管理－资金流水")
    def test_go_TransactionRecordPage(self):
        self.b.go_OrderManagePage().go_TransactionRecordPage()
        assert_text = '筛 选', '流水类型'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("订单与应收管理－应收账款工作台")
    def test_go_AccountReceivablePage(self):
        self.b.go_OrderManagePage().go_AccountReceivablePage()
        assert_text = '筛 选', '经营单位', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("订单与应收管理－发票池")
    def test_go_InvoicePoolPage(self):
        self.b.go_OrderManagePage().go_InvoicePoolPage()
        assert_text = '筛 选', '客户名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("标签管理－标签模板")
    def test_go_TagManagePage(self):
        self.b.go_TagPage().go_TagManagePage()
        assert_text = '筛 选', '客户名称', '修改'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("标签管理－模板管理")
    def test_go_TemplateManagePage(self):
        self.b.go_TagPage().go_TemplateManagePage()
        assert_text = '制作模板', '客户名称/标签类型', '有效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("标签管理－API数据集")
    def test_go_TagDatasetPage(self):
        self.b.go_TagPage().go_TagDatasetPage()
        assert_text = '添加数据', '字段名称', '修改'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story("标签管理－商品标签管理")
    # def test_go_ProductLabelPage(self):
    #     self.b.go_TagPage().go_ProductLabelPage()
    #     assert_text = '标签名称', '部署'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("标签管理－标签打印")
    def test_go_TagPrintPage(self):
        self.b.go_TagPage().go_TagPrintPage()
        assert_text = '客户名称', '导入标签数据'
        assertUtils.assert_equals(self.b.get_assert_text('label', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容管理－文章管理")
    def test_go_EcnewPage(self):
        self.b.go_ContentManagePage().go_EcnewPage()
        assert_text = '提交文章', '已发布'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容管理－资料管理")
    def test_go_SubmitEcdocPage(self):
        self.b.go_ContentManagePage().go_SubmitEcdocPage()
        assert_text = '提交资料', '已发布'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容管理－公告管理")
    def test_go_SpEcdocPage(self):
        self.b.go_ContentManagePage().go_SpEcdocPage()
        assert_text = '批量新增', '型号/系列', '详情'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("内容管理－代理协议管理")
    def test_go_AgencyAgreementPage(self):
        self.b.go_ContentManagePage().go_AgencyAgreementPage()
        assert_text = '上传代理协议', '签约主体', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("内容管理－视频素材管理")
    def test_go_MaterialManagementPage(self):
        self.b.go_ContentManagePage().go_MaterialManagementPage()
        assert_text = '邀请上传视频', '视频ID', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("内容管理－视频成品管理")
    def test_go_FinishManagementPage(self):
        self.b.go_ContentManagePage().go_FinishManagementPage()
        assert_text = '新建', '视频ID', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("内容管理－选型器")
    def test_go_SelectionPage(self):
        self.b.go_ContentManagePage().go_SelectionPage()
        assert_text = '筛 选', '选型器名称', '审核通过'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("内容管理－对照表")
    def test_go_ReferencePage(self):
        self.b.go_ContentManagePage().go_ReferencePage()
        assert_text = '筛 选', '对照表名称', '生效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－数字营销")
    def test_go_DigitalMarketingPage(self):
        self.b.go_StatisticsPage().go_DigitalMarketingPage()
        assert_text = '平台广告资源统计', '广告名称', '首页'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－服务统计")
    def test_go_ServiceStatisticsPage(self):
        self.b.go_StatisticsPage().go_ServiceStatisticsPage()
        assert_text = '商务服务下提交的商品统计', '服务提交量统计', '小量快购'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－数据统计通用工具")
    def test_go_StatisticalToolsPage(self):
        self.b.go_StatisticsPage().go_StatisticalToolsPage()
        assert_text = '导 入', '报表名称', '更新报表'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("统计报表－页面统计")
    def test_go_WebpuvPage(self):
        self.b.go_StatisticsPage().go_WebpuvPage()
        assert_text = '整站统计', '页面统计', '首页'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－会员统计")
    def test_go_MemstatPage(self):
        self.b.go_StatisticsPage().go_MemstatPage()
        assert_text = '会员统计', '活跃用户', '汇总'
        assertUtils.assert_equals(self.b.get_assert_text('h2', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－定制统计")
    def test_go_WebpuvCustomPage(self):
        self.b.go_StatisticsPage().go_WebpuvCustomPage()
        assert_text = '定制统计', '页面统计', '硬创商城'
        assertUtils.assert_equals(self.b.get_assert_text('h2', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('b', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－品牌资源统计")
    def test_go_BrandStatPage(self):
        num = self.b.go_StatisticsPage().go_BrandStatPage().get_BrandStatPage_num()
        assert_text = '品牌资源统计', '筛 选'
        assertUtils.assert_greater_equal(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－ON运营台")
    def test_go_OnStoragePage(self):
        self.b.go_StatisticsPage().go_OnStoragePage()
        assert_text = '筛 选', '序号', '有效'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－ON资源统计")
    def test_go_OnStatPage(self):
        num = self.b.go_StatisticsPage().go_OnStatPage().get_OnStatPage_num()
        assert_text = 'ON-资料统计', '全部资料'
        assertUtils.assert_greater_equal(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－服务内容统计")
    def test_go_ServiceContentStatPage(self):
        self.b.go_StatisticsPage().go_ServiceContentStatPage()
        assert_text = '筛 选', '序号', '传感器定制'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－服务资源统计")
    def test_go_ServiceResourceStatPage(self):
        self.b.go_StatisticsPage().go_ServiceResourceStatPage()
        assert_text = '筛 选', '序号', '传感器定制'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－资源消费统计")
    def test_go_BrandConsumePage(self):
        self.b.go_StatisticsPage().go_BrandConsumePage()
        assert_text = '筛 选', '序号', '10Gtek'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("统计报表－企业资源消费统计")
    def test_go_EpServiceStatPage(self):
        self.b.go_StatisticsPage().go_EpServiceStatPage()
        assert_text = '检 索', '服务工程师数量', '武汉光迅科技股份有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－企业关系维护")
    def test_go_EpmPage(self):
        self.b.go_StatisticsPage().go_EpmPage()
        assert_text = '新增主企业', '官邮后缀', '@sekorm.com'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    # @allure.story("统计报表－ON数量统计")
    # def test_go_OnDataStatPage(self):
    #     self.b.go_StatisticsPage().go_OnDataStatPage()
    #     assert_text = '发送邮件', '平台上线ON数量', 'ACAM'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－SKU数据统计")
    def test_go_ProviderStatisticsPage(self):
        self.b.go_StatisticsPage().go_ProviderStatisticsPage()
        assert_text = '筛 选', '序号', 'ACAM'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－样品ON未满足视图")
    def test_go_SampleUnMetViewPage(self):
        self.b.go_StatisticsPage().go_SampleUnMetViewPage()
        assert_text = '查 询', '序号', 'SP123WF100JT2E'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("统计报表－供应商评分")
    def test_go_SupplierScorePage(self):
        self.b.go_StatisticsPage().go_SupplierScorePage()
        assert_text = '批量上传', '序号', 'AARONIA'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－物料出货明细表")
    def test_go_ShippingDetailsPage(self):
        self.b.go_StatisticsPage().go_ShippingDetailsPage()
        assert_text = '筛 选', '样品库存'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－出货统计表")
    def test_go_MonthShipmentPage(self):
        self.b.go_StatisticsPage().go_MonthShipmentPage()
        assert_text = '筛 选', '样品库存'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－搜索词统计")
    def test_go_SearchTermStatisticsPage(self):
        num = self.b.go_StatisticsPage().go_SearchTermStatisticsPage().get_SearchTermStatisticsPage_num()
        assert_text = '筛 选', '序号'
        assertUtils.assert_equals(num, 200)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－搜索行为日志")
    def test_go_SearchBehaviorLogPage(self):
        self.b.go_StatisticsPage().go_SearchBehaviorLogPage()
        assert_text = '筛 选', '序号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－出库详情表")
    def test_go_MonthShipmentDetailPage(self):
        self.b.go_StatisticsPage().go_MonthShipmentDetailPage()
        assert_text = '筛 选', '客户名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－潜在需求表")
    def test_go_PotentialReqStatPage(self):
        self.b.go_StatisticsPage().go_PotentialReqStatPage()
        assert_text = '批量导入查询ON', '汇总'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("统计报表－样品预测")
    def test_go_ForecastPage(self):
        self.b.go_StatisticsPage().go_ForecastPage()
        assert_text = '筛 选', '样品类型', '免费样品'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－客户出货统计")
    def test_go_ShipmentStatPage(self):
        self.b.go_StatisticsPage().go_ShipmentStatPage()
        assert_text = '筛 选', '出货总金额', '武汉光迅科技股份有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("统计报表－商品预测供需表")
    def test_go_GoodsForecastPage(self):
        self.b.go_StatisticsPage().go_GoodsForecastPage()
        assert_text = '筛 选', 'FCST', '富满电子'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－平台SDB")
    def test_go_SdbPage(self):
        self.b.go_StatisticsPage().go_SdbPage()
        assert_text = '检 索', '序号', '深圳市世强元件网络有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－新平台SDB")
    def test_go_NewSdbPage(self):
        num = self.b.go_StatisticsPage().go_NewSdbPage().get_NewSdbPage_num()
        assert_text = '检 索', '经营商'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－供应释放")
    def test_go_SdbReleaseManagementPage(self):
        self.b.go_StatisticsPage().go_SdbReleaseManagementPage()
        assert_text = '导 入', '检 索', 'SO行号'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－潜在需求SDB")
    def test_go_PotentialSdbPage(self):
        self.b.go_StatisticsPage().go_PotentialSdbPage()
        assert_text = '检 索', '序号', '世强控股有限公司'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("统计报表－客户行为记录")
    def test_go_SrSearchListV2Page(self):
        num = self.b.go_StatisticsPage().go_SrSearchListV2Page().get_SrSearchListV2Page_num()
        assert_text = '筛 选', '序号',
        assertUtils.assert_greater_equal(num, 5)
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("统计报表－服务商行为记录")
    def test_go_SrSearchSpListPage(self):
        self.b.go_StatisticsPage().go_SrSearchSpListPage()
        assert_text = '筛 选', '序号', '平台'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("统计报表－OT统计")
    def test_go_DinStatisticsPage(self):
        self.b.go_StatisticsPage().go_DinStatisticsPage()
        assert_text = '查 看', 'DIN方案总数', '方案和技术中心'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("邮件发送清单")
    def test_go_GroupEmailPage(self):
        self.b.go_GroupEmailPage()
        assert_text = '筛 选', '邮件主题', '暂无数据'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("销售业绩归属－业绩分成设置")
    def test_go_PerFormanceSharingPage(self):
        self.b.go_SalesPerformancePage().go_PerFormanceSharingPage()
        assert_text = '业绩分成设置', '客户名称/TSE', '世强先进(深圳)科技股份有限公司(内部)'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("销售业绩归属－确认业绩比例")
    def test_go_ConFirmPerFormancePage(self):
        self.b.go_SalesPerformancePage().go_ConFirmPerFormancePage()
        assert_text = '修改业绩比例', 'ERP客户编码', '筛 选'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("销售业绩归属－录入业绩比例")
    def test_go_EnterPerFormancePage(self):
        self.b.go_SalesPerformancePage().go_EnterPerFormancePage()
        assert_text = '筛 选', 'ERP客户编码'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("销售业绩归属－我的业绩分成")
    def test_go_MyPerformanceSharePage(self):
        self.b.go_SalesPerformancePage().go_MyPerformanceSharePage()
        assert_text = '2023下半年', '客户名称/TSE'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("DW核算管理－DW-PN设置")
    def test_go_DWPerformancePage(self):
        self.b.go_DWAchievementPage().go_DWPerformancePage()
        assert_text = '导出数据', '序号', '思瑞浦'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("DW核算管理－DW核算订单池")
    def test_go_DWAccountingOrderPoolPage(self):
        num = self.b.go_DWAchievementPage().go_DWAccountingOrderPoolPage().get_DWAccountingOrderPoolPage_num()
        assert_text = '终端客户', '序号'
        assertUtils.assert_greater_equal(num, 5)
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("DW核算管理－DIN分配池")
    def test_go_DinDistributionPoolPage(self):
        self.b.go_DWAchievementPage().go_DinDistributionPoolPage()
        assert_text = '终端客户', '序号', '已分配'
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("DW核算管理－DW分配池")
    def test_go_DWDistributionPoolPage(self):
        num = self.b.go_DWAchievementPage().go_DWDistributionPoolPage().get_DWDistributionPoolPage_num()
        assert_text = '终端客户', '序号'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("设置－组织架构")
    # def test_go_EpTeamStructurePage(self):
    #     self.b.go_SettingsPage().go_EpTeamStructurePage()
    #     assert_text = '企业/部门', '世强先进（深圳）科技股份有限公司'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story("设置－客户标签管理")
    def test_go_EnterpriseTagsManagePage(self):
        self.b.go_SettingsPage().go_EnterpriseTagsManagePage()
        assert_text = '新建标签', '标签名称', '编辑'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("设置－供应商标签管理")
    def test_go_SupplierTagsManagePage(self):
        self.b.go_SettingsPage().go_SupplierTagsManagePage()
        assert_text = '新建标签', '标签名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story("设置－品牌标签管理")
    # def test_go_BrandTagsManagePage(self):
    #     self.b.go_SettingsPage().go_BrandTagsManagePage()
    #     assert_text = '新建标签', '标签名称', '编辑'
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.b.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("设置－第三方系统")
    def test_go_ExternalSystemPage(self):
        self.b.go_SettingsPage().go_ExternalSystemPage()
        assert_text = '搜 索', '第三方系统名称'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("设置－第三方系统管理")
    def test_go_ExternalSystemManagePage(self):
        self.b.refresh()
        self.b.go_SettingsPage().go_ExternalSystemManagePage()
        assert_text = '搜 索', '第三方系统名称', '肯耐珂萨学习平台'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("设置－第三方系统授权")
    def test_go_ExternalSystemAuthorizationPage(self):
        self.b.refresh()
        self.b.go_SettingsPage().go_ExternalSystemAuthorizationPage()
        assert_text = '搜 索', '第三方系统名称', '肯耐珂萨学习平台'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story("设置－审批流程管理")
    def test_go_WorkflowManageListPage(self):
        self.b.refresh()
        self.b.go_SettingsPage().go_WorkflowManageListPage()
        assert_text = '检 索', '审批流程名称', '加入服务团队审批'
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.b.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("退出登录、未登录页、登录失败")
    def test_quit(self):
        # 退出登录、未登录页
        text = self.b.quit_b_login().go_b_login().get_b_login_text()
        assert text == '版权所有：深圳市世强元件网络有限公司    粤ICP备05117344号'
        # 登录失败
        text = self.b.go_b_login().b_login_fail('13647913494', '123')
        assert text == '手机号或密码有误，请重新输入或找回密码'