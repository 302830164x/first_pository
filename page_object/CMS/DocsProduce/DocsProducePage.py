from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.DocsProduce.DocsExtract.BrandQualityPage2 import BrandQualityPage2
from page_object.CMS.DocsProduce.DocsExtract.BrandTotalPage2 import BrandTotalPage2
from page_object.CMS.DocsProduce.DocsExtract.CompleteManagePage import CompleteManagePage
from page_object.CMS.DocsProduce.DocsExtract.MyTaskPage2 import MyTaskPage2
from page_object.CMS.DocsProduce.DocsExtract.PreviewCountPage import PreviewCountPage
from page_object.CMS.DocsProduce.DocsExtract.PreviewDetailPage import PreviewDetailPage
from page_object.CMS.DocsProduce.DocsExtract.ReceiveManagePage import ReceiveManagePage
from page_object.CMS.DocsProduce.DocsExtract.TaskManagePage2 import TaskManagePage2
from page_object.CMS.DocsProduce.DocsExtract.TaskQualityPage import TaskQualityPage
from page_object.CMS.DocsProduce.DocsExtract.TaskReceivePage2 import TaskReceivePage2
from page_object.CMS.DocsProduce.DocsExtract.UnreceivedManagePage import UnreceivedManagePage
from page_object.CMS.DocsProduce.DocsKeyin.BrandQualityPage import BrandQualityPage
from page_object.CMS.DocsProduce.DocsKeyin.MyTaskPage import MyTaskPage
from page_object.CMS.DocsProduce.DocsKeyin.TaskManagePage import TaskManagePage
from page_object.CMS.DocsProduce.DocsKeyin.TaskReceivePage import TaskReceivePage
from page_object.CMS.DocsProduce.DocsKeyin.TskQualityPage import TskQualityPage
from page_object.CMS.DocsProduce.DocsManage.BatchManagementPage import BatchManagementPage
from page_object.CMS.DocsProduce.DocsManage.BrandTotalPage import BrandTotalPage
from page_object.CMS.DocsProduce.DocsManage.DocClaimPage import DocClaimPage
from page_object.CMS.DocsProduce.DocsManage.DocNotClaimPage import DocNotClaimPage
from page_object.CMS.DocsProduce.DocsManage.EcdocImportPage import EcdocImportPage
from page_object.CMS.DocsProduce.DocsManage.EcdocInvalidPage import EcdocInvalidPage
from page_object.CMS.DocsProduce.DocsManage.EcdocTypeBrandPage import EcdocTypeBrandPage
from page_object.CMS.DocsProduce.DocsManage.EcdocTypeManagePage import EcdocTypeManagePage
from page_object.CMS.DocsProduce.DocsManage.LabelPage import LabelPage
from page_object.CMS.DocsProduce.DocsManage.NewDocManagePage import NewDocManagePage
from page_object.CMS.DocsProduce.DocsManage.NewExtractInspTotalPage import NewExtractInspTotalPage
from page_object.CMS.DocsProduce.DocsManage.NewQualityInspTotalPage import NewQualityInspTotalPage
from page_object.CMS.DocsProduce.DocsManage.NotPublishPage import NotPublishPage
from page_object.CMS.DocsProduce.DocsManage.PublishPage import PublishPage
from page_object.CMS.DocsProduce.DocsManage.QualityInspTotalPage import QualityInspTotalPage
from page_object.CMS.DocsProduce.DocsTranslation.EcdocManagePage import EcdocManagePage
from page_object.CMS.DocsProduce.DocsTranslation.EcdocPublishPage import EcdocPublishPage
from page_object.CMS.DocsProduce.DocsTranslation.MyTaskPage3 import MyTaskPage3
from page_object.CMS.DocsProduce.DocsTranslation.TaskReceivePage3 import TaskReceivePage3
from page_object.CMS.DocsProduce.DocsTranslation.WaitDocTransPage import WaitDocTransPage
from page_object.CMS.DocsProduce.NewDocsKeyin.BatchSamplePage import BatchSamplePage
from page_object.CMS.DocsProduce.NewDocsKeyin.ExtractTaskReceivePage import ExtractTaskReceivePage
from page_object.CMS.DocsProduce.NewDocsKeyin.MyExtractTaskPage import MyExtractTaskPage
from page_object.CMS.DocsProduce.NewDocsKeyin.MyTaskQualityPage import MyTaskQualityPage
from page_object.CMS.DocsProduce.NewDocsKeyin.QualityBatchPage import QualityBatchPage
from page_object.CMS.DocsProduce.NewDocsKeyin.QualityTaskReceivePage import QualityTaskReceivePage
from page_object.CMS.DocsProduce.NewDocsKeyin.TaskQualityAuditPage import TaskQualityAuditPage

sekorm = Element('CmsElement')


class DocsProducePage(BasePage):
    """资料生产"""

    def go_TaskReceivePage(self):
        """资料生产-资料KEYIN-领取任务"""
        self.is_click(sekorm['资料生产-资料KEYIN'])
        self.is_click(sekorm['资料生产-资料KEYIN-领取任务'])
        return TaskReceivePage(self.driver)

    def go_MyTaskPage(self):
        """资料生产-资料KEYIN-我的任务"""
        self.is_click(sekorm['资料生产-资料KEYIN'])
        self.is_click(sekorm['资料生产-资料KEYIN-我的任务'])
        return MyTaskPage(self.driver)

    def go_TskQualityPage(self):
        """资料生产-资料KEYIN-质检"""
        self.is_click(sekorm['资料生产-资料KEYIN'])
        self.is_click(sekorm['资料生产-资料KEYIN-质检'])
        return TskQualityPage(self.driver)

    def go_BrandQualityPage(self):
        """资料生产-资料KEYIN-按厂牌质检"""
        self.is_click(sekorm['资料生产-资料KEYIN'])
        self.is_click(sekorm['资料生产-资料KEYIN-按厂牌质检'])
        return BrandQualityPage(self.driver)

    def go_TaskManagePage(self):
        """资料生产-资料KEYIN-任务管理"""
        self.is_click(sekorm['资料生产-资料KEYIN'])
        self.is_click(sekorm['资料生产-资料KEYIN-任务管理'])
        return TaskManagePage(self.driver)

    def go_EcdocImportPage(self):
        """资料生产-资料KEYIN-任务管理"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-新增资料'])
        return EcdocImportPage(self.driver)

    def go_NewDocManagePage(self):
        """资料生产-资料KEYIN-新资料管理"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-新资料管理'])
        return NewDocManagePage(self.driver)

    def go_DocNotClaimPage(self):
        """资料生产-资料KEYIN-待领取资料"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-待领取资料'])
        return DocNotClaimPage(self.driver)

    def go_DocClaimPage(self):
        """资料生产-资料KEYIN-已领取资料"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-已领取资料'])
        return DocClaimPage(self.driver)

    def go_BatchManagementPage(self):
        """资料生产-资料KEYIN-批次管理"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-批次管理'])
        return BatchManagementPage(self.driver)

    def go_NotPublishPage(self):
        """资料生产-资料KEYIN-未发布资料"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-未发布资料'])
        return NotPublishPage(self.driver)

    def go_PublishPage(self):
        """资料生产-资料KEYIN-已发布资料"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-已发布资料'])
        return PublishPage(self.driver)

    def go_EcdocTypeManagePage(self):
        """资料生产-资料KEYIN-资料类型管理"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-资料类型管理'])
        return EcdocTypeManagePage(self.driver)

    def go_LabelPage(self):
        """资料生产-资料KEYIN-标签规则设置"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-标签规则设置'])
        return LabelPage(self.driver)

    def go_EcdocTypeBrandPage(self):
        """资料生产-资料KEYIN-厂牌/类型匹配设置"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-厂牌/类型匹配设置'])
        return EcdocTypeBrandPage(self.driver)

    def go_EcdocInvalidPage(self):
        """资料生产-资料KEYIN-作废文档管理"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-作废文档管理'])
        return EcdocInvalidPage(self.driver)

    def go_BrandTotalPage(self):
        """资料生产-资料KEYIN-资料KEYIN总览"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-资料KEYIN总览'])
        return BrandTotalPage(self.driver)

    def go_QualityInspTotalPage(self):
        """资料生产-资料KEYIN-质检数据总览"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-质检数据总览'])
        return QualityInspTotalPage(self.driver)

    def go_NewQualityInspTotalPage(self):
        """资料生产-资料KEYIN-新质检数据总览"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-新质检数据总览'])
        return NewQualityInspTotalPage(self.driver)

    def go_NewExtractInspTotalPage(self):
        """资料生产-资料KEYIN-新提取数据总览"""
        self.is_click(sekorm['资料生产-资料管理'])
        self.is_click(sekorm['资料生产-资料管理-新提取数据总览'])
        return NewExtractInspTotalPage(self.driver)

    def go_ExtractTaskReceivePage(self):
        """资料生产-新资料KEYIN-领取提取任务"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-领取提取任务'])
        return ExtractTaskReceivePage(self.driver)

    def go_MyExtractTaskPage(self):
        """资料生产-新资料KEYIN-我的提取"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-我的提取'])
        return MyExtractTaskPage(self.driver)

    def go_QualityBatchPage(self):
        """资料生产-新资料KEYIN-质检分批"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-质检分批'])
        return QualityBatchPage(self.driver)

    def go_BatchSamplePage(self):
        """资料生产-新资料KEYIN-批次抽样"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-批次抽样'])
        return BatchSamplePage(self.driver)

    def go_QualityTaskReceivePage(self):
        """资料生产-新资料KEYIN-领取质检任务"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-领取质检任务'])
        return QualityTaskReceivePage(self.driver)

    def go_MyTaskQualityPage(self):
        """资料生产-新资料KEYIN-我的质检"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-我的质检'])
        return MyTaskQualityPage(self.driver)

    def go_TaskQualityAuditPage(self):
        """资料生产-新资料KEYIN-平台审核"""
        self.is_click(sekorm['资料生产-新资料KEYIN'])
        self.is_click(sekorm['资料生产-新资料KEYIN-平台审核'])
        return TaskQualityAuditPage(self.driver)

    def go_TaskReceivePage2(self):
        """资料生产-资料二次提取-领取任务"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-领取任务'])
        return TaskReceivePage2(self.driver)

    def go_MyTaskPage2(self):
        """资料生产-资料二次提取-我的任务"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-我的任务'])
        return MyTaskPage2(self.driver)

    def go_TaskQualityPage(self):
        """资料生产-资料二次提取-质检"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-质检'])
        return TaskQualityPage(self.driver)

    def go_BrandQualityPage2(self):
        """资料生产-资料二次提取-按厂牌质检"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-按厂牌质检'])
        return BrandQualityPage2(self.driver)

    def go_TaskManagePage2(self):
        """资料生产-资料二次提取-任务管理"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-任务管理'])
        return TaskManagePage2(self.driver)

    def go_ReceiveManagePage(self):
        """资料生产-资料二次提取-已领取资料"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-已领取资料'])
        return ReceiveManagePage(self.driver)

    def go_UnreceivedManagePage(self):
        """资料生产-资料二次提取-待领取资料"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-待领取资料'])
        return UnreceivedManagePage(self.driver)

    def go_CompleteManagePage(self):
        """资料生产-资料二次提取-已完成资料"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-已完成资料'])
        return CompleteManagePage(self.driver)

    def go_PreviewDetailPage(self):
        """资料生产-资料二次提取-预览日志明细"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-预览日志明细'])
        return PreviewDetailPage(self.driver)

    def go_PreviewCountPage(self):
        """资料生产-资料二次提取-预览次数/分钟"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-预览次数/分钟'])
        return PreviewCountPage(self.driver)

    def go_BrandTotalPage2(self):
        """资料生产-资料二次提取-二次提取总览"""
        self.is_click(sekorm['资料生产-资料二次提取'])
        self.is_click(sekorm['资料生产-资料二次提取-二次提取总览'])
        return BrandTotalPage2(self.driver)

    def go_WaitDocTransPage(self):
        """资料生产-资料翻译-待确认资料"""
        self.is_click(sekorm['资料生产-资料翻译'])
        self.is_click(sekorm['资料生产-资料翻译-待确认资料'])
        return WaitDocTransPage(self.driver)

    def go_TaskReceivePage3(self):
        """资料生产-资料翻译-领取资料"""
        self.is_click(sekorm['资料生产-资料翻译'])
        self.is_click(sekorm['资料生产-资料翻译-领取资料'])
        return TaskReceivePage3(self.driver)

    def go_MyTaskPage3(self):
        """资料生产-资料翻译-我的资料"""
        self.is_click(sekorm['资料生产-资料翻译'])
        self.is_click(sekorm['资料生产-资料翻译-我的资料'])
        return MyTaskPage3(self.driver)

    def go_EcdocManagePage(self):
        """资料生产-资料翻译-翻译资料管理"""
        self.is_click(sekorm['资料生产-资料翻译'])
        self.is_click(sekorm['资料生产-资料翻译-翻译资料管理'])
        return EcdocManagePage(self.driver)

    def go_EcdocPublishPage(self):
        """资料生产-资料翻译-翻译资料发布"""
        self.is_click(sekorm['资料生产-资料翻译'])
        self.is_click(sekorm['资料生产-资料翻译-翻译资料发布'])
        return EcdocPublishPage(self.driver)