import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils
from utils.times import sleep


@allure.epic('CMS')
@allure.feature('CMS检查')
class Test_CMS:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_cms_driver(self, cms_driver):
        self.cms = cms_driver
        self.cms.get_url(f'{ini.CmsUrl}/content/cums/home')

    @allure.story("首页")
    def test_go_CmsIndexPage(self):
        assertUtils.assert_equals(self.cms.get_cms_index_text(), '首页')
        assertUtils.assert_equals(self.cms.get_cms_index_list_num(), 20)

    @allure.story("个人中心")
    def test_go_UserCenterPage(self):
        self.cms.go_UserCenterPage()
        assert_text = '个人基础信息', '保 存'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("公告发布")
    def test_go_NoticePage(self):
        num = self.cms.go_NoticePage().get_NoticePage_num()
        assert_text = '公告发布', '详情'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-作者-提主题")
    def test_go_SelfSubjectPage(self):
        self.cms.go_NewsProducePage().go_SelfSubjectPage()
        assert_text = '提主题', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-作者-待认领主题")
    def test_go_ReceiveSubjectPage(self):
        self.cms.go_NewsProducePage().go_ReceiveSubjectPage()
        assert_text = '待认领主题', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-作者-已认领主题")
    def test_go_PendingSubjectPage(self):
        self.cms.go_NewsProducePage().go_PendingSubjectPage()
        assert_text = '已认领主题', '释 放'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-作者-我的文章")
    def test_go_AuthorEcnewPage(self):
        self.cms.go_NewsProducePage().go_AuthorEcnewPage()
        assert_text = '我的文章', '暂无数据'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-审核专家-待认领文章")
    def test_go_WaitReceivePage(self):
        self.cms.go_NewsProducePage().go_WaitReceivePage()
        assert_text = '待认领文章', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-审核专家-已认领文章")
    def test_go_WaitAuditPage(self):
        self.cms.go_NewsProducePage().go_WaitAuditPage()
        assert_text = '已认领文章', '释 放'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-审核专家-我审核的文章")
    def test_go_MyAuditPage(self):
        self.cms.go_NewsProducePage().go_MyAuditPage()
        assert_text = '我审核的文章', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-资讯管理员-待审核主题")
    def test_go_WaitAuditSubjectPage(self):
        self.cms.go_NewsProducePage().go_WaitAuditSubjectPage()
        assert_text = '待审核主题', '通 过'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-资讯管理员-已通过主题")
    def test_go_PassedSubjectPage(self):
        self.cms.go_NewsProducePage().go_PassedSubjectPage()
        assert_text = '已通过主题', '认领设置', '不通过', '认领设置'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[3]), assert_text[3])

    @allure.story("资讯生产-资讯管理员-未通过主题")
    def test_go_NotPassedSubjectPage(self):
        self.cms.go_NewsProducePage().go_NotPassedSubjectPage()
        assert_text = '未通过主题', '筛 选', '中文'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-待发布文章")
    def test_go_WaitPublishEcnewPage(self):
        self.cms.go_NewsProducePage().go_WaitPublishEcnewPage()
        assert_text = '待发布文章', '筛 选', '审核'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-已发布文章")
    def test_go_PublishEcnewPage(self):
        self.cms.go_NewsProducePage().go_PublishEcnewPage()
        assert_text = '已发布文章', '标 识', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-未通过文章")
    def test_go_NotPassEcnewPage(self):
        self.cms.go_NewsProducePage().go_NotPassEcnewPage()
        assert_text = '未通过文章', '释放主题', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-已失效文章")
    def test_go_DisabledEcnewPage(self):
        self.cms.go_NewsProducePage().go_DisabledEcnewPage()
        assert_text = '已失效文章', '生 效', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-管理设置")
    def test_go_ManageSettingsPage(self):
        self.cms.go_NewsProducePage().go_ManageSettingsPage()
        assert_text = '管理设置', '保存设置', '主题不审核'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资讯生产-资讯管理员-导入主题")
    def test_go_ImportSubjectPage(self):
        self.cms.go_NewsProducePage().go_ImportSubjectPage()
        assert_text = '导入主题', '详情'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story("资讯生产-资讯管理员-关键词检查")
    def test_go_EcnewKeywordCheckPage(self):
        self.cms.go_NewsProducePage().go_EcnewKeywordCheckPage()
        assert_text = '关键词检查', '筛 选', '同步搜索词'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料KEYIN-领取任务")
    def test_go_TaskReceivePage(self):
        self.cms.go_DocsProducePage().go_TaskReceivePage()
        assert_text = '领取任务', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料KEYIN-我的任务")
    def test_go_MyTaskPage(self):
        self.cms.go_DocsProducePage().go_MyTaskPage()
        assert_text = '我的任务', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料KEYIN-质检")
    def test_go_TskQualityPage(self):
        self.cms.go_DocsProducePage().go_TskQualityPage()
        assert_text = '质检', '筛 选', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料KEYIN-按厂牌质检")
    def test_go_BrandQualityPage(self):
        self.cms.go_DocsProducePage().go_BrandQualityPage()
        assert_text = '批量抽样', '查看合格资料'
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料KEYIN-任务管理")
    def test_go_TaskManagePage(self):
        self.cms.go_DocsProducePage().go_TaskManagePage()
        assert_text = '任务管理', '筛 选', '明细'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-新增资料")
    def test_go_EcdocImportPage(self):
        self.cms.go_DocsProducePage().go_EcdocImportPage()
        assert_text = '新增资料', '新增资料', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-新资料管理")
    def test_go_NewDocManagePage(self):
        self.cms.go_DocsProducePage().go_NewDocManagePage()
        assert_text = '新资料管理', '筛 选', '技术收集'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-待领取资料")
    def test_go_DocNotClaimPage(self):
        num = self.cms.go_DocsProducePage().go_DocNotClaimPage().get_DocNotClaimPage_list_num()
        assert_text = '待领取资料', '批量作废(0)'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料管理-已领取资料")
    def test_go_DocClaimPage(self):
        self.cms.go_DocsProducePage().go_DocClaimPage()
        assert_text = '已领取资料', '释放(0)'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料管理-批次管理")
    def test_go_BatchManagementPage(self):
        num = self.cms.go_DocsProducePage().go_BatchManagementPage().get_BatchManagementPage_list_num()
        assert_text = '批次管理', '筛 选'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料管理-未发布资料")
    def test_go_NotPublishPage(self):
        num = self.cms.go_DocsProducePage().go_NotPublishPage().get_NotPublishPage_list_num()
        assert_text = '未发布资料', '筛 选'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料管理-已发布资料")
    def test_go_PublishPage(self):
        self.cms.go_DocsProducePage().go_PublishPage()
        assert_text = '已发布资料', '筛 选', 'Keyin'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-资料类型管理")
    def test_go_EcdocTypeManagePage(self):
        self.cms.go_DocsProducePage().go_EcdocTypeManagePage()
        assert_text = '资料类型管理', '筛 选', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-标签规则设置")
    def test_go_LabelPage(self):
        self.cms.go_DocsProducePage().go_LabelPage()
        assert_text = '标签规则管理', '新增规则', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-厂牌/类型匹配设置")
    def test_go_EcdocTypeBrandPage(self):
        self.cms.go_DocsProducePage().go_EcdocTypeBrandPage()
        assert_text = '厂牌/类型匹配设置', '筛 选', '生效'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-作废文档管理")
    def test_go_EcdocInvalidPage(self):
        self.cms.go_DocsProducePage().go_EcdocInvalidPage()
        assert_text = '作废文档管理', '筛 选', '未处理'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-资料KEYIN总览")
    def test_go_BrandTotalPage(self):
        self.cms.go_DocsProducePage().go_BrandTotalPage()
        assert_text = 'KEYIN资料总览', '设置每月领取限制', '合计'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-质检数据总览")
    def test_go_QualityInspTotalPage(self):
        self.cms.go_DocsProducePage().go_QualityInspTotalPage()
        assert_text = '质检数据总览', '筛 选', '合计'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料管理-新质检数据总览")
    def test_go_NewQualityInspTotalPage(self):
        num = self.cms.go_DocsProducePage().go_NewQualityInspTotalPage().get_NewQualityInspTotalPage_list_num()
        assert_text = '新质检数据总览', '筛 选'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料管理-新提取数据总览")
    def test_go_NewExtractInspTotalPage(self):
        num = self.cms.go_DocsProducePage().go_NewExtractInspTotalPage().get_NewQualityInspTotalPage_list_num()
        assert_text = '新提取数据总览', '筛 选'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-领取提取任务")
    def test_go_ExtractTaskReceivePage(self):
        self.cms.go_DocsProducePage().go_ExtractTaskReceivePage()
        assert_text = '领取提取任务', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-我的提取")
    def test_go_MyExtractTaskPage(self):
        self.cms.go_DocsProducePage().go_MyExtractTaskPage()
        assert_text = '我的提取', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-质检分批")
    def test_go_QualityBatchPage(self):
        self.cms.go_DocsProducePage().go_QualityBatchPage()
        assert_text = '质检分批', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-批次抽样")
    def test_go_BatchSamplePage(self):
        self.cms.go_DocsProducePage().go_BatchSamplePage()
        assert_text = '批次抽样', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-领取质检任务")
    def test_go_QualityTaskReceivePage(self):
        num = self.cms.go_DocsProducePage().go_QualityTaskReceivePage().get_QualityTaskReceivePage_num()
        assert_text = '领取质检任务', '筛 选'
        assertUtils.assert_greater_equal(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-我的质检")
    def test_go_MyTaskQualityPage(self):
        self.cms.go_DocsProducePage().go_MyTaskQualityPage()
        assert_text = '我的质检', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-新资料KEYIN-平台审核")
    def test_go_TaskQualityAuditPage(self):
        self.cms.go_DocsProducePage().go_TaskQualityAuditPage()
        assert_text = '平台审核', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-领取任务")
    def test_go_TaskReceivePage2(self):
        self.cms.go_DocsProducePage().go_TaskReceivePage2()
        assert_text = '领取任务', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-我的任务")
    def test_go_MyTaskPage2(self):
        self.cms.go_DocsProducePage().go_MyTaskPage2()
        assert_text = '我的任务', '筛 选', '暂无数据'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('p', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料二次提取-质检")
    def test_go_TaskQualityPage(self):
        self.cms.go_DocsProducePage().go_TaskQualityPage()
        assert_text = '质检', '筛 选', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料二次提取-按厂牌质检")
    def test_go_BrandQualityPage2(self):
        self.cms.go_DocsProducePage().go_BrandQualityPage2()
        assert_text = '按厂牌质检', '查看合格资料'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-任务管理")
    def test_go_TaskManagePage2(self):
        self.cms.go_DocsProducePage().go_TaskManagePage2()
        assert_text = '任务管理', '筛 选', '明细'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料二次提取-已领取资料")
    def test_go_ReceiveManagePage(self):
        num = self.cms.go_DocsProducePage().go_ReceiveManagePage().get_ReceiveManagePage_num()
        sleep(20)
        assert_text = '已领取资料', '已处理'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-待领取资料")
    def test_go_UnreceivedManagePage(self):
        num = self.cms.go_DocsProducePage().go_UnreceivedManagePage().get_UnreceivedManagePage_list_num()
        sleep(5)
        assert_text = '待领取资料', '作废(0)'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-已完成资料")
    def test_go_CompleteManagePage(self):
        self.cms.go_DocsProducePage().go_CompleteManagePage()
        assert_text = '已完成资料', '筛 选', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料二次提取-预览日志明细")
    def test_go_PreviewDetailPage(self):
        num = self.cms.go_DocsProducePage().go_PreviewDetailPage().get_PreviewDetailPage_list_num()
        assert_text = '预览日志明细', '筛 选'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-预览次数/分钟")
    def test_go_PreviewCountPage(self):
        num = self.cms.go_DocsProducePage().go_PreviewCountPage().get_PreviewCountPage_list_num()
        assert_text = '预览次数/分钟', '筛 选'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料二次提取-二次提取总览")
    def test_go_BrandTotalPage2(self):
        self.cms.go_DocsProducePage().go_BrandTotalPage2()
        assert_text = '二次提取总览', '设置每月领取限制', '合计'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料翻译-待确认资料")
    def test_go_WaitDocTransPage(self):
        self.cms.go_DocsProducePage().go_WaitDocTransPage()
        assert_text = '待翻译资料确认', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料翻译-领取资料")
    def test_go_TaskReceivePage3(self):
        self.cms.go_DocsProducePage().go_TaskReceivePage3()
        assert_text = '领取翻译资料', '领取(0)'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料翻译-我的资料")
    def test_go_MyTaskPage3(self):
        self.cms.go_DocsProducePage().go_MyTaskPage3()
        assert_text = '我的翻译资料', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料生产-资料翻译-翻译资料管理")
    def test_go_EcdocManagePage(self):
        self.cms.go_DocsProducePage().go_EcdocManagePage()
        assert_text = '翻译资料管理', '筛 选', '查看质检记录'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料生产-资料翻译-翻译资料发布")
    def test_go_EcdocPublishPage(self):
        self.cms.go_DocsProducePage().go_EcdocPublishPage()
        assert_text = '翻译资料发布', '筛 选', '生效'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料采集-地址管理")
    def test_go_WebsitePage(self):
        self.cms.go_DocsCollectPage().go_WebsitePage()
        assert_text = '地址管理', '添加新任务', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料采集-标题来源管理")
    def test_go_TitleSourcePage(self):
        self.cms.go_DocsCollectPage().go_TitleSourcePage()
        assert_text = '标题来源管理', '筛 选', '正常'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("资料采集-任务调度管理")
    def test_go_TaskDispatchPage(self):
        self.cms.go_DocsCollectPage().go_TaskDispatchPage()
        assert_text = '任务调度管理', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("资料采集-采集情况管理")
    def test_go_TaskMonitorPage(self):
        self.cms.go_DocsCollectPage().go_TaskMonitorPage()
        assert_text = '采集情况管理', '筛 选', '正常'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("资料采集-链接采集校验")
    def test_go_LinkMonitorPage(self):
        self.cms.go_DocsCollectPage().go_LinkMonitorPage()
        assert_text = '链接采集校验', '链接', '采 集'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('label', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("资料采集-链接过滤校验")
    def test_go_TaskMonitorPage(self):
        self.cms.go_DocsCollectPage().go_LinkValidatePage()
        assert_text = '链接过滤校验', '链接', '校 验'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('label', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("资料采集-导入链接管理")
    def test_go_ImportFileurlPage(self):
        self.cms.go_DocsCollectPage().go_ImportFileurlPage()
        assert_text = '导入资料链接', '筛 选', '详情'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料采集-通过过滤字符管理")
    def test_go_GeneralFilterPage(self):
        self.cms.go_DocsCollectPage().go_GeneralFilterPage()
        assert_text = '通用过滤字符管理', '搜索', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("新增资料管理-资料管理")
    def test_go_NewDocPage(self):
        num = self.cms.go_NewDocsManagePage().go_NewDocPage().get_NewDocPage_list_num()
        assert_text = '资料管理', '按选中失效'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("新增资料管理-疑似重复资料管理")
    def test_go_DuplicateFilePage(self):
        self.cms.go_NewDocsManagePage().go_DuplicateFilePage()
        assert_text = '疑似重复资料管理', '设为非重复资料', '文件名'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("B台提交内容-文章")
    def test_go_EcnewbPage(self):
        self.cms.go_BSubmitsContentPage().go_EcnewbPage()
        assert_text = '文章', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("B台提交内容-资料")
    def test_go_SpmsEcdocPage(self):
        self.cms.go_BSubmitsContentPage().go_SpmsEcdocPage()
        sleep(5)
        assert_text = '资料', '筛 选'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("B台提交内容-选型表")
    def test_go_SelectionPage(self):
        self.cms.go_BSubmitsContentPage().go_SelectionPage()
        assert_text = '选型表', '通 过'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("关键词翻译-已翻译管理")
    def test_go_TranslationManagePage(self):
        self.cms.go_KeywordTranslationPage().go_TranslationManagePage()
        sleep(30)
        assert_text = '已翻译管理', '翻译正确(0)', '修正翻译'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("关键词翻译-翻译替换管理")
    def test_go_TransReplaceManagePage(self):
        self.cms.go_KeywordTranslationPage().go_TransReplaceManagePage()
        assert_text = '翻译替换管理', '添加翻译替换', '操作日志'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料发布-资料发布")
    def test_go_EcdocPublishPage(self):
        self.cms.go_DocsPublishPage().go_EcdocPublishPage()
        assert_text = '资料发布', '添加新资料', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("资料发布-原词有误处理")
    def test_go_WrongWordPage(self):
        num = self.cms.go_DocsPublishPage().go_WrongWordPage().get_WrongWordPage_list_num()
        assert_text = '原词有误处理', '筛 选',
        assertUtils.assert_equals(num, 200)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("发布资料去重-重复资料")
    def test_go_EcdocRepeatPage(self):
        self.cms.go_RemoveDuplicationPage().go_EcdocRepeatPage()
        assert_text = '重复资料', '筛 选', '有效'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("发布资料去重-疑似重复资料")
    def test_go_EdocSuspectPage(self):
        self.cms.go_RemoveDuplicationPage().go_EdocSuspectPage()
        assert_text = '疑似重复资料', '筛 选', '有效'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资讯结算-资讯结算报表")
    def test_go_BillCountPage(self):
        self.cms.go_ContentSettlementPage().go_BillCountPage()
        assert_text = '资讯结算报表', '筛 选', '合计'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资讯结算-资讯计费规则配置")
    def test_go_BillRulePage(self):
        num = self.cms.go_ContentSettlementPage().go_BillRulePage().get_BillRulePage_num()
        sleep(5)
        assert_text = '资讯计费规则配置', '新 增'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容结算-资讯结算-资讯计费原始报表")
    def test_go_BillSourcePage(self):
        num = self.cms.go_ContentSettlementPage().go_BillSourcePage().get_BillSourcePage_list_num()
        assert_text = '资讯计费原始报表', '筛 选'
        assertUtils.assert_equals(num, 50)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容结算-资料KEYIN结算-KEYIN结算报表")
    def test_go_KeyinBillCountPage(self):
        self.cms.go_ContentSettlementPage().go_KeyinBillCountPage()
        assert_text = '资料keyin结算报表', '检 索', '合计'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资料KEYIN结算-KEYIN规则配置")
    def test_go_KeyinBillRulePage(self):
        num = self.cms.go_ContentSettlementPage().go_KeyinBillRulePage().get_KeyinBillRulePage_num()
        assert_text = '资料keyin规则配置', '筛 选'
        assertUtils.assert_greater_equal(num, 20)
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("内容结算-资料KEYIN结算-KEYIN原始报表")
    def test_go_KeyinBillSourcePage(self):
        self.cms.go_ContentSettlementPage().go_KeyinBillSourcePage()
        assert_text = 'KEYIN原始报表', '筛 选', '提取正确'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资料翻译结算-翻译结算报表")
    def test_go_TransBillCountPage(self):
        self.cms.go_ContentSettlementPage().go_TransBillCountPage()
        assert_text = '资料翻译结算报表', '检 索', '翻译费用'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资料翻译结算-翻译规则配置")
    def test_go_TransBillRulePage(self):
        self.cms.go_ContentSettlementPage().go_TransBillRulePage()
        assert_text = '资料翻译规则配置', '新 增', '审核通过'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story("内容结算-资料翻译结算-翻译原始报表")
    def test_go_TransBillSourcePage(self):
        self.cms.go_ContentSettlementPage().go_TransBillSourcePage()
        assert_text = '检 索', '资料发布ID', '资料发布名'
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("内容结算-内容计费规则审核")
    def test_go_BillRuleAuditPage(self):
        self.cms.go_ContentSettlementPage().go_BillRuleAuditPage()
        assert_text = '内容计费规则审核', '审核通过', '计费类型'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story("视频管理-视频素材管理")
    def test_go_VideoMaterialManagePage(self):
        self.cms.go_VideoManagePage().go_VideoMaterialManagePage()
        assert_text = '视频素材管理', '检 索', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("视频管理-视频成品管理")
    def test_go_VideoProductManagePage(self):
        self.cms.go_VideoManagePage().go_VideoProductManagePage()
        assert_text = '视频成品管理', '筛 选', '查看'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("设置-用户管理")
    def test_go_UsersManagePage(self):
        self.cms.go_UsersManagePage()
        assert_text = '用户管理', '筛 选', '编辑'
        assertUtils.assert_equals(self.cms.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.cms.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.cms.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story("退出登录、未登录页、登录检查")
    def test_001(self):
        # 退出登录、未登录页
        text = self.cms.quit_cms_login().go_cms_login().get_cms_login_text()
        assertUtils.assert_equals(text, '手机号登录')
        # 登录失败
        text = self.cms.go_cms_login().cms_login_fail('13647913494', '123')
        assertUtils.assert_equals(text, '你输入的密码有误，请重新输入')


if __name__ == '__main__':
    pytest.main(['test_cms.py', '-s'])
