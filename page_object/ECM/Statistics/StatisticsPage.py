from common.readelement import Element
from page.basepage import BasePage
from page_object.ECM.Statistics.ContentStatistics.StatEcnew import StatEcnew
from page_object.ECM.Statistics.ContentStatistics.StatPgc import StatPgc
from page_object.ECM.Statistics.MemberStatistics.MemModifyContactStat import MemModifyContactStat
from page_object.ECM.Statistics.MemberStatistics.StatExp import StatExp

sekorm = Element('EcmElement')


class StatisticsPage(BasePage):
    """数据统计页"""

    # 手机邮箱修改统计
    def go_MemModifyContactStat(self):
        self.is_click(sekorm['数据统计-会员统计-手机邮箱修改统计'])
        return MemModifyContactStat(self.driver)

    # 经验值统计
    def go_StatExp(self):
        self.is_click(sekorm['数据统计-会员统计-经验值统计'])
        return StatExp(self.driver)

    # 资讯报表导出
    def go_StatEcnew(self):
        self.is_click(sekorm['数据统计-内容数据统计'])
        self.is_click(sekorm['数据统计-内容数据统计-资讯报表导出'])
        return StatEcnew(self.driver)

    # PGC统计
    def go_StatPgc(self):
        self.is_click(sekorm['数据统计-内容数据统计'])
        self.is_click(sekorm['数据统计-内容数据统计-PGC统计'])
        return StatPgc(self.driver)



