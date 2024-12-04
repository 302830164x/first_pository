import allure
import pytest

from common.readconfig import ini
from utils.assertUtils import assertUtils
from utils.times import sleep


@allure.epic('ECM')
@allure.feature('ECM检查')
class Test_ECM:

    # 初始化页面对象
    @pytest.fixture(autouse=True)
    def set_ecm_driver(self, ecm_driver):
        self.ecm = ecm_driver
        self.ecm.get_url(f'{ini.EcmUrl}/fixed/home/index.html')

    @allure.story('内容管理菜单检查')
    def test_002(self):
        self.ecm.click_content()
        assert_text = 'App启动广告'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('会员管理菜单检查')
    def test_003(self):
        self.ecm.click_member()
        assert_text = '注册会员列表'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('运营管理菜单检查')
    def test_004(self):
        self.ecm.click_operation()
        assert_text = '审核通过列表'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('交付管理菜单检查')
    def test_005(self):
        self.ecm.click_delivery()
        assert_text = '实物仓库'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    # @allure.story('数据管理菜单检查')
    # def test_006(self):
    #     self.ecm.click_statistics()
    #     assert_text = '手机邮箱修改统计'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('Q&A管理菜单检查')
    def test_007(self):
        self.ecm.click_qa()
        assert_text = '新增提问'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('基础资料菜单检查')
    def test_008(self):
        self.ecm.click_base()
        assert_text = 'ON待审核'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('服务商菜单检查')
    def test_009(self):
        self.ecm.click_provider()
        assert_text = '服务商管理'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('系统管理菜单检查')
    def test_010(self):
        self.ecm.click_system()
        assert_text = '用户管理'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text), assert_text)

    @allure.story('内容管理-广告管理-App启动广告')
    def test_011(self):
        self.ecm.click_content().go_WmsLoadimgList()
        assert_text = 'App启动广告', '广告名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-广告管理-Web右侧广告')
    def test_012(self):
        self.ecm.click_content().go_WmsAdvertList()
        assert_text = 'WEB右侧广告', '广告图名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-广告管理-Web左侧广告')
    def test_013(self):
        self.ecm.click_content().go_WmsAdvertLeftManageMain()
        assert_text = 'WEB左侧广告', '广告名称', '通栏广告'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('内容管理-广告管理-H5分享页广告图')
    def test_014(self):
        self.ecm.click_content().go_WmsH5AdvertMain()
        assert_text = 'H5分享页广告图', '广告图名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-广告管理-文字广告管理')
    def test_015(self):
        self.ecm.click_content().go_WmsTextadsList()
        assert_text = '文字广告管理', '标题名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-内容推广管理-展会管理')
    def test_016(self):
        self.ecm.click_content().go_WmsEcDataAdvert()
        assert_text = '展会管理', '新增展会'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('内容管理-内容推广管理-视频管理')
    def test_017(self):
        self.ecm.click_content().go_WmsVideo()
        assert_text = '视频管理', '视频ID', '生效'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('内容管理-资讯发布')
    def test_018(self):
        self.ecm.click_content().go_CmsEcnewMain()
        assert_text = '资讯发布', '标题', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-产品选型列表')
    def test_019(self):
        self.ecm.click_content().go_SeleDocManageList()
        assert_text = '产品选型列表', '资料编码', '修改推荐'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-资料导入')
    def test_020(self):
        self.ecm.click_content().go_EcdocImpt()
        assert_text = '资料导入', '资料发布名', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-产品选型管理')
    def test_021(self):
        self.ecm.click_content().go_SelectionEcdoc()
        assert_text = '产品选型管理', '资料编码', '发布成功'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('内容管理-资料预览配置')
    def test_022(self):
        self.ecm.click_content().go_CmsEcdocShow()
        assert_text = '资料预览配置', '用户类型', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-消息管理-APP消息推送')
    def test_023(self):
        self.ecm.click_content().go_WmsMobileMessageList()
        assert_text = '消息推送', '推送用户', '消息详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('内容管理-二维码管理')
    def test_024(self):
        self.ecm.click_content().go_BdmQrCodeMain()
        assert_text = '二维码管理', '生成二维码'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('button', assert_text[1]), assert_text[1])

    @allure.story('会员管理-会员列表-注册会员列表')
    def test_025(self):
        self.ecm.click_member().go_MemberMemRegMemMain()
        assert_text = '会员管理', '会员ID', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员列表-VIP认证会员列表')
    def test_026(self):
        self.ecm.click_member().go_MemberMemVipMemMain()
        assert_text = '会员管理', '会员ID', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员列表-服务商会员列表')
    def test_027(self):
        self.ecm.click_member().go_MemberMemSpMemMain()
        assert_text = '会员管理', '会员ID', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员列表-手机黑名单')
    def test_028(self):
        self.ecm.click_member().go_BlackListList()
        assert_text = '手机黑名单', '手机号', '解除黑名单'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员列表-潜在会员')
    def test_go_PotentialMember(self):
        self.ecm.click_member().go_PotentialMember()
        assert_text = '潜在会员', '手机号', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员分组-VIP认证会员分组')
    def test_029(self):
        self.ecm.click_member().go_ExpCredMem()
        assert_text = 'VIP认证会员分组', '会员类型', '成员管理'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-经验值等级头衔-经验值管理')
    def test_030(self):
        self.ecm.click_member().go_ExpExpManage()
        assert_text = '经验值管理', '成长值', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story('会员管理-经验值等级头衔-等级规则')
    def test_031(self):
        self.ecm.click_member().go_ExpGradeRule()
        assert_text = '会员等级', '系统等级', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-经验值等级头衔-等级头衔')
    def test_032(self):
        self.ecm.click_member().go_ExpGradeLabel()
        assert_text = '会员等级头衔', '头衔名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员产品-产品匹配')
    def test_033(self):
        self.ecm.click_member().go_MemberConcernConcernMain()
        assert_text = '会员产品匹配', '产品ID', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员产品-产品校正')
    def test_034(self):
        self.ecm.click_member().go_MemberConcernCheckMain()
        assert_text = '会员产品校正', '会员ID', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员产品-默认市场')
    def test_035(self):
        self.ecm.click_member().go_MemberConcernDefMarkMain()
        assert_text = '会员默认市场', '已匹配产品', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员产品-匹配日志')
    def test_036(self):
        self.ecm.click_member().go_MemberConcernLogMain()
        assert_text = '会员产品匹配日志', '产品名称', '产品子类'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员审核-会员信息审核')
    def test_037(self):
        self.ecm.click_member().go_MemberWorkWaitAssessVerify()
        assert_text = '会员信息审核', '手机号', '处理'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员审核-异常客户关联')
    def test_038(self):
        self.ecm.click_member().go_MemberWorkAbnormalList()
        assert_text = '异常客户关联', '手机号'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('会员管理-会员审核-通过审核的会员')
    def test_039(self):
        self.ecm.click_member().go_MemberWorkPass()
        assert_text = '通过审核的会员', '手机号', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-会员审核-不通过审核的会员')
    def test_040(self):
        self.ecm.click_member().go_MemberWorkNotPassMember()
        assert_text = '不通过审核的会员', '手机号', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-发现工作变更')
    def test_041(self):
        self.ecm.click_member().go_MemberChangeInfo()
        assert_text = '发现工作变更', '变更说明', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-头像审核')
    def test_042(self):
        num = self.ecm.click_member().go_MemberVerifyHead().get_MemberVerifyHead_num()
        assert_text = '头像审核', '检 索'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('会员管理-电商客户管理')
    def test_043(self):
        self.ecm.click_member().go_MemberEnterpriseEpinfo()
        sleep(10)
        assert_text = '电商客户管理', '电商客户', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-电商客户白名单')
    def test_044(self):
        self.ecm.click_member().go_WhiteListMain()
        assert_text = '电商白名单客户管理', '企业名称', '企业详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-手机过滤VIP会员')
    def test_045(self):
        self.ecm.click_member().go_MemberVipMemberFilter()
        assert_text = '手机过滤VIP会员', '过 滤'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('会员管理-邮箱过滤VIP会员')
    def test_046(self):
        self.ecm.click_member().go_MemberVipMemberFilter_Email()
        assert_text = '邮箱过滤VIP会员', '过 滤'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('会员管理-意见反馈')
    def test_047(self):
        self.ecm.click_member().go_MemberOpinionMain()
        assert_text = '意见反馈管理', '反馈来源', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-邮箱域名管理')
    def test_048(self):
        self.ecm.click_member().go_MemberEmailMain()
        assert_text = '邮箱域名管理', '邮箱域名后缀', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-验证工作邮箱')
    def test_049(self):
        self.ecm.click_member().go_VerifyVerifyHelp()
        assert_text = '验证工作邮箱', '验证密串', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('会员管理-自动注册会员-待注册记录')
    def test_050(self):
        num = self.ecm.click_member().go_AutoRegPending().get_AutoRegPending_list_num()
        assert_text = '待注册记录', '注册时间'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('会员管理-自动注册会员-完成注册记录')
    def test_051(self):
        self.ecm.click_member().go_AutoRegCompleted()
        assert_text = '完成注册记录', '注册时间', '会员详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-评论管理-审核通过列表')
    def test_052(self):
        self.ecm.click_operation().go_WmsCommentPass()
        assert_text = '审核通过列表', '评论类型', '回复'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-评论管理-审核不通过列表')
    def test_053(self):
        num = self.ecm.click_operation().go_WmsCommentNopass().get_WmsCommentNopass_list_num()
        assert_text = '审核不通过列表', '评论类型'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('运营管理-活动管理-发布活动')
    def test_054(self):
        self.ecm.click_operation().go_ActiActivity()
        assert_text = '发布活动', '活动ID', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-表单管理')
    def test_055(self):
        self.ecm.click_operation().go_ActiFormv()
        assert_text = '表单管理', '表单ID', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-活动报名管理')
    def test_056(self):
        self.ecm.click_operation().go_ActiEnroll()
        assert_text = '活动报名管理', '活动ID', '查看报名详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-活动数据统计')
    def test_057(self):
        self.ecm.click_operation().go_AtatActiStatToActiDataCount()
        assert_text = '活动数据统计', '活动ID', '报名'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-会员积分明细')
    def test_058(self):
        self.ecm.click_operation().go_ActiScoreStat()
        assert_text = '会员活跃指数明细', '会员ID', '修改'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-送鼠标报名统计')
    def test_059(self):
        self.ecm.click_operation().go_ActiMouseReceive()
        assert_text = '送鼠标报名统计', '会员ID', '备注'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-展会数据统计')
    def test_060(self):
        self.ecm.click_operation().go_StatMunichShowStat()
        assert_text = '展会数据统计', '姓名', '备注'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-实验室预订管理')
    def test_061(self):
        self.ecm.click_operation().go_ActiLabOrder()
        assert_text = '实验室预约管理', '姓名', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-研讨会管理')
    def test_062(self):
        self.ecm.click_operation().go_SemiNarSignListSeminarlist()
        assert_text = '研讨会管理', '研讨会名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-活动管理-研讨会签到')
    def test_063(self):
        self.ecm.click_operation().go_SemiNarSignList()
        assert_text = '研讨会签到', '会员ID', '服务记录'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), '  服务记录')

    @allure.story('运营管理-活动管理-抽奖管理')
    def test_064(self):
        self.ecm.click_operation().go_ActiLotteryList()
        assert_text = '抽奖管理', '中奖人数', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-出口管制-订单管制')
    def test_068(self):
        self.ecm.click_operation().go_PartnumberNewRestrictPool()
        assert_text = '订单管制池', '管制描述', '查看详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-出口管制-客户管制')
    def test_069(self):
        self.ecm.click_operation().go_PartnumberNewCustomerRestrictPool()
        assert_text = '客户管制池', '管制状态', '查看详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-出口管制-管制设置')
    def test_070(self):
        self.ecm.click_operation().go_PartnumberNewRestrictSetting()
        assert_text = '管制名称', '管制名称', '失效'
        assertUtils.assert_equals(self.ecm.get_assert_text('label', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-元件供应-元件供应')
    def test_071(self):
        self.ecm.click_operation().go_SupplyPartnumberSupply()
        sleep(15)
        assert_text = '元件供应', '型号', '有效'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('运营管理-元件供应-频道页排序')
    def test_072(self):
        self.ecm.click_operation().go_QuickPrhSupplySort()
        assert_text = '频道页排序', '操作人', '设置'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-元件供应-APP频道页配置')
    def test_073(self):
        self.ecm.click_operation().go_SupplyChannelConfig()
        assert_text = 'APP频道页配置', '配置行名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-商城管理-商城设置')
    def test_075(self):
        self.ecm.click_operation().go_MallManageMallConfiguration()
        assert_text = '电子商城', '亚洲商城'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[1]), assert_text[1])

    @allure.story('运营管理-商城管理-平台交易流水')
    def test_076(self):
        self.ecm.click_operation().go_MallManageOrderFlow()
        assert_text = '平台交易流水', '服务商名称', '世强先进(深圳)科技股份有限公司'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[2]), assert_text[2])

    @allure.story('运营管理-奖券管理-奖券管理')
    def test_077(self):
        self.ecm.click_operation().go_WmsCoupon()
        assert_text = '奖券列表', '奖券名称', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-奖券管理-奖券统计')
    def test_078(self):
        num = self.ecm.click_operation().go_WmsCouponDetail().get_WmsCouponDetail_list_num()
        assert_text = '奖券管理-奖券总数', '奖券名称'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('运营管理-品牌管理')
    def test_079(self):
        self.ecm.click_operation().go_WmsBrandLogo()
        assert_text = '品牌管理', '品牌名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索热词设置')
    def test_080(self):
        num = self.ecm.click_operation().go_WmsHotWord().get_WmsHotWord_list_num()
        assert_text = '搜索热词设置', '搜索热词'
        assertUtils.assert_equals(num, 5)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('运营管理-系统消息')
    def test_081(self):
        self.ecm.click_operation().go_WmsMessage()
        assert_text = '系统消息', '标题', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-VIP福利专区管理')
    def test_082(self):
        self.ecm.click_operation().go_WmsHomerecomVip()
        assert_text = 'VIP福利专区管理', '标题', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-首页轮播图管理')
    def test_083(self):
        self.ecm.click_operation().go_WmsHomebanner()
        assert_text = '首页轮播图管理', '广告图名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-首页楼层广告管理')
    def test_084(self):
        self.ecm.click_operation().go_WmsHomerecomHomeFloor()
        assert_text = '首页楼层广告图管理', '标题', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-元件供应管理')
    def test_085(self):
        self.ecm.click_operation().go_WmsHomerecomPartnumber()
        assert_text = '元件供应管理', '标题', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-英文版首页轮播图管理')
    def test_086(self):
        self.ecm.click_operation().go_WmsEnHomebanner()
        assert_text = '首页轮播图管理', '广告图名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-首页内容管理-首页商城厂牌')
    def test_087(self):
        self.ecm.click_operation().go_WmsGoodsBrand()
        assert_text = '商城厂牌管理', '商品分类', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-小量快购-快购管理')
    def test_088(self):
        self.ecm.click_operation().go_QuickPrhProgram()
        assert_text = '快购设置', '大额订单审核机制管理'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-快购对账-待确认收款')
    def test_089(self):
        assert_text = self.ecm.click_operation().go_QuickPrhPayManage().get_QuickPrhPayManage_text()
        assertUtils.assert_equals(assert_text[0], '待确认')
        assertUtils.assert_equals(assert_text[1], '订单号')

    @allure.story('运营管理-快购对账-已确认收款')
    def test_090(self):
        assert_text = self.ecm.click_operation().go_QuickPrhPaidManage().get_QuickPrhPaidManage_text()
        assertUtils.assert_equals(assert_text[0], '已确认')
        assertUtils.assert_equals(assert_text[1], '详情')

    @allure.story('运营管理-快购对账-财务对账')
    def test_091(self):
        num = self.ecm.click_operation().go_QuickPrhCheckAccount().get_QuickPrhCheckAccount_list_num()
        assert_text = '财务对账', '商户订单号'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索配置-溯源记录查询工具')
    def test_go_CompressString(self):
        self.ecm.click_operation().go_CompressString()
        assert_text = '溯源关系字符压缩工具', '查 询', '序号'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索配置-服务资源词库管理')
    def test_092(self):
        self.ecm.click_operation().go_SekWordServiceResource()
        assert_text = '服务资源词库管理', '关联系统资源', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索配置-关键词管理工具')
    def test_093(self):
        self.ecm.click_operation().go_SekWordKeyword()
        assert_text = '关键词管理工具', '关键词来源', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索配置-索引查询设置')
    def test_094(self):
        self.ecm.click_operation().go_SearchWeight()
        assert_text = '查询设置', '保 存'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索配置-同义词管理')
    def test_095(self):
        self.ecm.click_operation().go_SekWordSynonym()
        assert_text = '同义词管理工具', '来源', '失效'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索配置-词性管理')
    def test_096(self):
        num = self.ecm.click_operation().go_SearchWordType().get_SearchWordType_list_num()
        assert_text = '词性管理', 'ID'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索配置-自定义规则管理')
    def test_097(self):
        num = self.ecm.click_operation().go_SearchRule().get_SearchRule_list_num()
        assert_text = '自定义规则管理', 'ID'
        assertUtils.assert_greater_equal(num, 9)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-服务提醒管理')
    def test_098(self):
        self.ecm.click_operation().go_McomServiceReminder()
        assert_text = '服务提醒管理', '服务类型', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-搜索分析-分词分析')
    def test_099(self):
        self.ecm.click_operation().go_SearchAnalyzer()
        assert_text = '分词分析', '分 析'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-搜索分析')
    def test_100(self):
        self.ecm.click_operation().go_SearchDocManage()
        assert_text = '搜索分析', '场景分词结果'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('p', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-权重分析')
    def test_101(self):
        self.ecm.click_operation().go_SearchIndexManager()
        assert_text = '索引设置', '获取索引信息'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-评分对比')
    def test_102(self):
        self.ecm.click_operation().go_SearchDocManages()
        assert_text = '评分对比', '文档总得分:'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('p', assert_text[1]), assert_text[1])

    # RGC统计已停用
    # @allure.story('RGC分析管理菜单检查')
    # def test_103(self):
    #     self.ecm.click_operation().go_SekRgcKeyword()
    #     assert_text = 'rgc统计'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text

    @allure.story('运营管理-搜索分析-点击统计')
    def test_104(self):
        self.ecm.click_operation().go_SearchClicks()
        assert_text = '资源类型点击数量统计', '内容类型'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-搜索转化分析')
    def test_go_SearchConversion(self):
        self.ecm.click_operation().go_SearchConversion()
        assert_text = '搜索转化统计', '来源'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('label', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-关键词朔源查询')
    def test_105(self):
        self.ecm.click_operation().go_SekWordKeywordSource()
        assert_text = '关键词朔源查询', '来源类型'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-搜索分析-短型号词朔源查询')
    def test_106(self):
        self.ecm.click_operation().go_SekWordSignalSource()
        assert_text = '短型号朔源查询', '来源类型'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-ES自检-配置查询')
    def test_107(self):
        self.ecm.click_operation().go_SelfInspection()
        assert_text = '配置查询', '提 交'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-Redis自检-配置查询')
    def test_108(self):
        self.ecm.click_operation().go_RedisSelfInspection()
        assert_text = '配置查询', '查 询'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-推荐配置-推荐场景配置')
    def test_109(self):
        self.ecm.click_operation().go_RecomScene()
        assert_text = '推荐场景配置', '未登录-推荐规则', '保 存'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-未登录配置')
    def test_110(self):
        self.ecm.click_operation().go_RecomUnlogin()
        assert_text = '未登录推荐规则', '名字', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-已登录配置')
    def test_111(self):
        self.ecm.click_operation().go_RecomLogin()
        assert_text = '已登录推荐规则', '名字', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-未登录配置（新）')
    def test_112(self):
        self.ecm.click_operation().go_RecomRecomRuleUnloginNew()
        assert_text = '未登录推荐规则', '名字', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-区域规则配置')
    def test_113(self):
        self.ecm.click_operation().go_RecomAreaRule()
        assert_text = '区域推荐规则', '名字', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-运营规则配置')
    def test_114(self):
        self.ecm.click_operation().go_RecomOpera()
        assert_text = '运营推荐规则', '名字', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-自定义内容管理')
    def test_115(self):
        self.ecm.click_operation().go_RecomCustom()
        assert_text = '自定义内容管理', '名字', '修改'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-推荐配置-推荐帮助信息')
    def test_116(self):
        num = self.ecm.click_operation().go_RecomHelp().get_RecomHelp_list_num()
        assert_text = '推荐帮助信息', '未登录规则'
        assertUtils.assert_greater_equal(num, 17)
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-推荐配置-任务管理')
    def test_117(self):
        self.ecm.click_operation().go_RecomTaskManage()
        assert_text = '推荐缓存管理', '缓存刷新'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-推荐配置-二元关系图谱分析')
    def test_118(self):
        num = self.ecm.click_operation().go_KeywordGraphRelationList().get_KeywordGraphRelationList_list_num()
        assert_text = '二元关系图谱', '关键字'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-SEO文件生成')
    def test_119(self):
        self.ecm.click_operation().go_RestrictSiteMapImport()
        assert_text = '链接SEO数据导入', '提交人', '备注'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-英文站SEO链接')
    def test_120(self):
        self.ecm.click_operation().go_RestrictEnSitemap()
        assert_text = '英文链接SEO数据', '提交人', '普通链接'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('运营管理-内容运营功能-标识管理')
    def test_121(self):
        self.ecm.click_operation().go_MarkList()
        assert_text = '标识管理', '标识名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-内容运营功能-待处理内容')
    def test_122(self):
        num = self.ecm.click_operation().go_PendingList().get_PendingList_list_num()
        assert_text = '批量入库', '文章类型'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-内容运营功能-运营内容管理')
    def test_123(self):
        num = self.ecm.click_operation().go_OperateList().get_OperateList_list_num()
        assert_text = '运营内容管理', '文章类型'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-短链生成工具')
    def test_124(self):
        self.ecm.click_operation().go_WmsShortUrlToPage()
        assert_text = '生成短链'
        assertUtils.assert_equals(self.ecm.get_assert_text('button', assert_text), assert_text)

    @allure.story('运营管理-404链接生成')
    def test_125(self):
        self.ecm.click_operation().go_RestrictLapseSitemapMain()
        assert_text = '404链接数据', '记录数量', '普通链接'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    @allure.story('运营管理-公用通讯通道')
    def test_126(self):
        self.ecm.click_operation().go_CommunicationChannel()
        assert_text = '公用通讯通道', '检 索'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('运营管理-静态页刷新工具')
    def test_go_StaticRefresh(self):
        self.ecm.click_operation().go_StaticRefresh()
        assert_text = '去刷新'
        assertUtils.assert_equals(self.ecm.get_assert_text('button', assert_text), assert_text)

    @allure.story('运营管理-批量邮件发送工具')
    def test_127(self):
        self.ecm.click_operation().go_WmsEmailTool()
        assert_text = '批量邮件发送工具', '邮件通道', '查看名单'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('运营管理-会员拉新-邮件导出')
    def test_go_EmailSharing(self):
        self.ecm.click_operation().go_EmailSharing()
        assert_text = '导 出', '任务编码', '下载'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('交付管理-电商仓库-实物仓库')
    def test_128(self):
        self.ecm.click_delivery().go_GiftStock()
        assert_text = '实物仓库', '礼品名称', '查看详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), '查看详情   ')

    @allure.story('交付管理-电商仓库-奖券仓库')
    def test_129(self):
        self.ecm.click_delivery().go_WmsCouponGiftMain()
        assert_text = '奖券列表', '奖券名称', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('交付管理-电商仓库-经验值仓库')
    def test_130(self):
        self.ecm.click_delivery().go_GiftExpStock()
        assert_text = '经验值仓库', '礼品名称', '查看详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('交付管理-礼品发放-礼品发放需求管理')
    def test_131(self):
        self.ecm.click_delivery().go_GiftSubject()
        assert_text = '礼品发放需求管理', '礼品类型', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), '编辑 ')

    @allure.story('交付管理-礼品发放-奖品分组管理')
    def test_132(self):
        self.ecm.click_delivery().go_GiftPrizeGroupManagement()
        assert_text = '奖品分组管理', '奖品数量', '删除'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('交付管理-电商交付平台-电商发货管理')
    def test_133(self):
        self.ecm.click_delivery().go_GiftSend()
        assert_text = '礼品发放需求管理', '收货地址', '发货'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), '发货 ')

    # @allure.story('数据统计-会员统计-手机邮箱修改统计')
    # def test_134(self):
    #     num = self.ecm.click_statistics().go_MemModifyContactStat().get_MemModifyContactStat_list_num()
    #     assert_text = '手机邮箱修改次数统计', '会员ID'
    #     assertUtils.assert_equals(num, 20)
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
    #
    # @allure.story('数据统计-会员统计-经验值统计')
    # def test_135(self):
    #     self.ecm.click_statistics().go_StatExp()
    #     sleep(15)
    #     assert_text = '经验值统计', '会员ID', '系统'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[2]), assert_text[2])

    # @allure.story('数据统计-内容数据统计-资讯报表导出')
    # def test_136(self):
    #     self.ecm.click_statistics().go_StatEcnew()
    #     assert_text = '资讯报表导出', '报表ID', '编辑备注'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])
    #
    # @allure.story('数据统计-内容数据统计-PGC统计')
    # def test_137(self):
    #     self.ecm.click_statistics().go_StatPgc()
    #     assert_text = 'PGC统计', '报表ID', '编辑备注'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-新增提问')
    def test_138(self):
        num = self.ecm.click_qa().go_PgcPgcAuditQueAudit().get_PgcPgcAuditQueAudit_list_num()
        assert_text = '提问审核', '提问标题'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-新增回答')
    def test_139(self):
        self.ecm.click_qa().go_PgcPgcAuditAnsAudit()
        assert_text = '解答审核', '提问标题'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-运营类池-待处理问题')
    def test_140(self):
        self.ecm.click_qa().go_PgcOperationPool()
        assert_text = '运营待处理问题', '会员ID', '处理'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-技术类池-待认领问题')
    def test_141(self):
        self.ecm.click_qa().go_PgcUnreceive2()
        assert_text = '技术类池', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-技术类池-我的认领')
    def test_142(self):
        self.ecm.click_qa().go_PgcMyreceived2()
        assert_text = '我认领的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-技术类池-我处理的PGC')
    def test_143(self):
        self.ecm.click_qa().go_PgcMytreated2()
        assert_text = '我处理的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-技术类池-我下属处理的PGC')
    def test_144(self):
        self.ecm.click_qa().go_PgcSubtreated2()
        assert_text = '下属处理的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-技术类池-我的下属管理')
    def test_145(self):
        self.ecm.click_qa().go_PgcEmployeeRelation2()
        assert_text = '我的下属管理', '我的下属列表', '绑定下属'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-商务类池-待认领问题')
    def test_146(self):
        self.ecm.click_qa().go_PgcUnreceive3()
        assert_text = '商务类池', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-商务类池-我的认领')
    def test_147(self):
        self.ecm.click_qa().go_PgcMyreceived3()
        assert_text = '我认领的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-商务类池-我处理的PGC')
    def test_148(self):
        self.ecm.click_qa().go_PgcMytreated3()
        assert_text = '我处理的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-商务类池-我下属处理的PGC')
    def test_149(self):
        self.ecm.click_qa().go_PgcSubtreated3()
        assert_text = '下属处理的PGC', '会员ID'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('Q&A管理-商务类池-我的下属管理')
    def test_150(self):
        self.ecm.click_qa().go_PgcEmployeeRelation3()
        assert_text = '我的下属管理', '我的下属列表', '绑定下属'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-Q&A内容管理')
    def test_151(self):
        self.ecm.click_qa().go_PgcPubPrepareQueAnsPub()
        assert_text = '问答管理', '提问归类', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-Q&A服务管理')
    def test_152(self):
        self.ecm.click_qa().go_PgcPgcServiceList()
        assert_text = 'Q&A服务管理', '提问标题', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-通过的问答')
    def test_153(self):
        self.ecm.click_qa().go_PgcPubPreparePublished()
        assert_text = '通过的问答', '提问标题', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-不通过的问答')
    def test_154(self):
        self.ecm.click_qa().go_PgcPubPrepareAuditNotPass()
        assert_text = '不通过的问答', '会员ID', '查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('Q&A管理-邀请解答记录')
    def test_155(self):
        num = self.ecm.click_qa().go_PgcInviteAnswer().get_PgcInviteAnswer_list_num()
        assert_text = '发送日志', '提问标题'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-ON管理-ON待审核')
    def test_go_OnVerify(self):
        self.ecm.click_base().go_OnVerify()
        assert_text = '批量审核', '平台状态'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-ON管理-ON管理')
    def test_go_OnManageList(self):
        self.ecm.click_base().go_OnManageList()
        assert_text = '更多筛选', '平台审核时间', '查看详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story('基础资料-ON管理-ON参数校对审核')
    # def test_go_OnTranslationReview(self):
    #     self.ecm.click_base().go_OnTranslationReview()
    #     assert_text = '型号参数校对审核', '产品线', '不通过'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('p', assert_text[2]), assert_text[2])

    # @allure.story('基础资料-商品管理-型号管理')
    # def test_156(self):
    #     self.ecm.click_base().go_EcdmPartnumber()
    #     assert_text = '型号管理'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '型号'
    #     text = self.ecm.get_assert_text('th', assert_text)
    #     assert text == assert_text
    #
    # @allure.story('基础资料-商品管理-系列型号管理')
    # def test_157(self):
    #     self.ecm.click_base().go_EcdmSeriesType()
    #     assert_text = '系列型号管理'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '系列型号'
    #     text = self.ecm.get_assert_text('th', assert_text)
    #     assert text == assert_text
    #
    # @allure.story('基础资料-商品管理-系列管理')
    # def test_158(self):
    #     self.ecm.click_base().go_EcdmSeries()
    #     assert_text = '系列管理'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '系列型号'
    #     text = self.ecm.get_assert_text('th', assert_text)
    #     assert text == assert_text
    #
    # @allure.story('基础资料-商品分类-旧分类')
    # def test_159(self):
    #     self.ecm.click_base().go_EcdmGoodscategory1()
    #     assert_text = '旧商品分类'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '射频微波器件'
    #     text = self.ecm.get_assert_text('span', assert_text)
    #     assert text == assert_text
    #
    # @allure.story('基础资料-商品分类-新分类')
    # def test_160(self):
    #     self.ecm.click_base().go_EcdmGoodscategory()
    #     assert_text = '新商品分类'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '微控制器、微处理器，SOC，DSP'
    #     text = self.ecm.get_assert_text('span', assert_text)
    #     assert text == assert_text
    #
    # @allure.story('基础资料-市场应用')
    # def test_161(self):
    #     self.ecm.click_base().go_EcdmEleccategory()
    #     assert_text = '市场应用'
    #     text = self.ecm.get_assert_text('div', assert_text)
    #     assert text == assert_text
    #     assert_text = '工业电子'
    #     text = self.ecm.get_assert_text('span', assert_text)
    #     assert text == assert_text

    @allure.story('基础资料-资讯类型管理')
    def test_162(self):
        self.ecm.click_base().go_DdmEcNewSysCode()
        assert_text = '资讯类型管理', '中文类型名', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-资料类型管理')
    def test_163(self):
        self.ecm.click_base().go_DdmEcdocType()
        assert_text = '资料类型管理', '中文类型名', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-视频类型管理')
    def test_164(self):
        self.ecm.click_base().go_DdmVideoType()
        assert_text = '视频类型管理', '中文类型名', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-敏感词管理-敏感词库')
    def test_165(self):
        self.ecm.click_base().go_SensitiveWordsList()
        assert_text = '敏感词库', '序号', '删除'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-敏感词管理-敏感词日志')
    def test_166(self):
        num = self.ecm.click_base().go_SensitiveWordsLogList().get_SensitiveWordsLogList_list_num()
        assert_text = '敏感词日志', '序号'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-职位')
    def test_167(self):
        self.ecm.click_base().go_BdmPosition()
        assert_text = '职位', '职位名称', '修改'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-商品关键词管理-关键词管理')
    def test_168(self):
        self.ecm.click_base().go_CmsKeywordManage()
        assert_text = '商品关键词管理', '检索'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('基础资料-商品关键词管理-SEO管理')
    def test_169(self):
        self.ecm.click_base().go_CmsSEOManage()
        assert_text = '商品SEO管理', '检索'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('基础资料-商品关键词管理-关键词分解')
    def test_170(self):
        self.ecm.click_base().go_CmsKeywordAnalysisLog()
        assert_text = '商品关键词分解', '关键词', '分解'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-品类货架')
    def test_172(self):
        self.ecm.click_base().go_KeywordGoodsRack()
        assert_text = '全部展开', '关键词上架', '专用MCU'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story('基础资料-新品类货架')
    def test_173(self):
        self.ecm.click_base().go_KeywordNewGoodsRack()
        assert_text = '全部展开', '关键词上架', '集成电路'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[2]), assert_text[2])

    @allure.story('基础资料-DR表单管理')
    def test_174(self):
        self.ecm.click_base().go_SpmDrProjectSet()
        assert_text = '请选择厂牌：', '新增字段'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])

    @allure.story('基础资料-货架内容查看')
    def test_175(self):
        num = self.ecm.click_base().go_KeywordNewShelvesContent().get_KeywordNewShelvesContent_list_num()
        assert_text = '检 索', '连接关键词'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-展示货架')
    def test_176(self):
        self.ecm.click_base().go_WmsNavigationBarMenu()
        assert_text = '添加主货架', '世强硬创服务平台中文站(有效)'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-平台标签维护')
    def test_177(self):
        self.ecm.click_base().go_BdmLabelList()
        assert_text = '平台标签维护', '标签名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-货架表单管理')
    def test_go_ShelfConfigFormList(self):
        self.ecm.click_base().go_ShelfConfigFormList()
        assert_text = '新建表单', '表单名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-货架配置管理')
    def test_go_ShelfCenterList(self):
        self.ecm.click_base().go_ShelfCenterList()
        assert_text = '添加主货架', '原子服务货架'
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-新厂牌管理-待审核厂牌')
    def test_178(self):
        self.ecm.click_base().go_BrandWaitingApprovalList()
        assert_text = '新增厂牌', '品牌名', '处理'
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-新厂牌管理-品牌变更审核')
    def test_go_BrandChangeAuditList(self):
        self.ecm.click_base().go_BrandChangeAuditList()
        assert_text = '品牌变更审核', '变更前品牌名'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('基础资料-新厂牌管理-审核未通过')
    def test_179(self):
        self.ecm.click_base().go_BrandUnapprovedList()
        assert_text = '审核未通过', '品牌简介', '编辑品牌信息'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-新厂牌管理-品牌数据库')
    def test_180(self):
        self.ecm.click_base().go_BrandApprovedList()
        assert_text = '品牌数据库', '品牌名', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('基础资料-合作关系')
    def test_181(self):
        self.ecm.click_base().go_PartnershipList()
        assert_text = '合作关系', '签约主体', '新增'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-服务商-服务商管理')
    def test_182(self):
        self.ecm.click_provider().go_SpmSpManager()
        assert_text = '已入驻管理', '服务商', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-服务商-服务商客户管理')
    def test_183(self):
        self.ecm.click_provider().go_CustomerMain()
        assert_text = '服务商客户管理', '服务商客户', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-服务商-服务商功能管理')
    def test_184(self):
        self.ecm.click_provider().go_SpmFunction()
        assert_text = '服务商权限管理', '权限名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-服务商-投资孵化申请')
    def test_185(self):
        self.ecm.click_provider().go_SpmIncubator()
        assert_text = '投资孵化申请', '公司名称', '备注'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-服务费管理')
    def test_186(self):
        self.ecm.click_provider().go_SpmChargingMod()
        assert_text = '服务费管理', '企业ID', '设置服务费'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-商品管理-商品审核')
    def test_go_CommodityVerify(self):
        self.ecm.click_provider().go_CommodityVerify()
        assert_text = '商品审核', '店铺名称'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('服务商-商品管理-商品管理')
    def test_go_CommodityManageList(self):
        num = self.ecm.click_provider().go_CommodityManageList().get_CommodityManageList_num()
        assert_text = '商品管理', '世强先进（深圳）科技股份有限公司'
        assertUtils.assert_equals(num, 25)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('td', assert_text[1]), assert_text[1])

    @allure.story('服务商-商品管理-上架类别')
    def test_191(self):
        self.ecm.click_provider().go_PnOnManageOnSaleCategory()
        assert_text = '上架类别', '上架类别', '修改'
        assertUtils.assert_equals(self.ecm.get_assert_text('h3', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-商品管理-ON授权管理')
    def test_194(self):
        num = self.ecm.click_provider().go_AuthorizationManageList().get_AuthorizationManageList_num()
        assert_text = '搜 索', '品牌'
        assertUtils.assert_equals(num, 100)
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('服务商-B端企业信息')
    def test_195(self):
        self.ecm.click_provider().go_SpmEnt()
        assert_text = 'B台企业信息管理', '企业名称', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story('服务商-代销商品-未上线提醒')
    # def test_196(self):
    #     self.ecm.click_provider().go_OfflineRemainderList()
    #     assert_text = '未上线提醒', '生产料号'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #
    # @allure.story('服务商-代销商品-代销商品管理')
    # def test_197(self):
    #     self.ecm.click_provider().go_SaleProxyList()
    #     assert_text = '代销商品管理', '显示商城'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #
    # @allure.story('服务商-代销商品-厚声物料表')
    # def test_198(self):
    #     num = self.ecm.click_provider().go_HsMaterialsInfoList().get_HsMaterialsInfoList_num()
    #     assert_text = '厚声物料表', '厚声生产料号'
    #     assertUtils.assert_equals(num, 20)
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    # @allure.story('服务商-商品标签管理-服务商授权管理')
    # def test_199(self):
    #     self.ecm.click_provider().go_WmsLabelManageSpManage()
    #     assert_text = '服务商授权管理', '服务商名称', '授权管理'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])
    #
    # @allure.story('服务商-商品标签管理-标签库')
    # def test_200(self):
    #     self.ecm.click_provider().go_WmsLabelManage()
    #     assert_text = '商品标签管理', '标签名称', '设置'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story('服务商-商品标签管理(新)-标签库')
    # def test_go_LabelList(self):
    #     self.ecm.click_provider().go_LabelList()
    #     assert_text = '标签样式', '设置'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[1]), assert_text[1])
    #
    # @allure.story('服务商-商品标签管理(新)-店铺标签授权管理')
    # def test_go_LabelAuthcList(self):
    #     self.ecm.click_provider().go_LabelAuthcList()
    #     assert_text = '店铺标签授权管理', '服务商名称', '授权管理'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-团队管理')
    def test_201(self):
        self.ecm.click_provider().go_SpmEpServiceTeam()
        assert_text = '团队管理', '服务商', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('服务商-公有企业数据库')
    def test_202(self):
        self.ecm.click_provider().go_SpmEnterprise()
        assert_text = '企业数据 ( 严格 )', '企业名称', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-用户管理')
    def test_203(self):
        self.ecm.click_system().go_EcpUser()
        assert_text = '用户管理', '用户ID', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-角色管理')
    def test_204(self):
        self.ecm.click_system().go_EcpRole()
        assert_text = '角色管理', '角色名称', '成员管理'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-功能管理')
    def test_205(self):
        self.ecm.click_system().go_EcpFunc()
        assert_text = '功能管理', '功能ID', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-机构管理')
    def test_206(self):
        self.ecm.click_system().go_EcpOrgan()
        assert_text = '机构管理', '机构ID', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-日志管理-内部内容访问日志')
    def test_207(self):
        num = self.ecm.click_system().go_StatSensitiveData().get_StatSensitiveData_num()
        assert_text = '内部内容访问日志', '内容标题'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('系统管理-日志管理-定时任务日志')
    def test_208(self):
        self.ecm.click_system().go_BdmTaskLog()
        assert_text = '定时任务运行日志', '任务名称', '异常信息过长请点击查看'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-日志管理-App崩溃日志')
    def test_209(self):
        self.ecm.click_system().go_BdmSysDown()
        assert_text = 'App崩溃日志', '崩溃日志编号', '查看详细日志'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-日志管理-发送日志')
    def test_210(self):
        self.ecm.click_system().go_BdmSendLog()
        assert_text = '发送日志', '发送类型', '详情'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-日志管理-操作日志')
    def test_211(self):
        self.ecm.click_system().go_BdmOperateLog()
        assert_text = '操作日志', '操作类型', '查看详细日志'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-省市区')
    def test_212(self):
        self.ecm.click_system().go_BdmCountry()
        assert_text = '省市区', '北京市'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('系统管理-APP版本管理')
    def test_213(self):
        self.ecm.click_system().go_BdmAppv()
        assert_text = '版本发布', '版本名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-数据字典管理-字典类型')
    def test_214(self):
        self.ecm.click_system().go_EcpParamterType()
        assert_text = '字典类型', '参数类型编码', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-数据字典管理-字典数据')
    def test_215(self):
        self.ecm.click_system().go_EcpParam()
        assert_text = '字典数据', '参数ID', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    # @allure.story('系统管理-任务管理')
    # def test_216(self):
    #     self.ecm.click_system().go_EcpTask()
    #     assert_text = '手动执行定时任务列表', '任务名称', '执行'
    #     assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
    #     assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-邮件提醒')
    def test_217(self):
        self.ecm.click_system().go_BdmRemind()
        assert_text = '邮件提醒', '提醒名称', '修改'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-调度中心-任务调度管理')
    def test_218(self):
        self.ecm.click_system().go_EcpTaskSchedulerJob()
        assert_text = '任务调度管理', '任务编码', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-调度中心-任务调度日志')
    def test_219(self):
        num = self.ecm.click_system().go_EcpTaskJobTrigger().get_EcpTaskJobTrigger_num()
        assert_text = '任务调度日志', '任务ID'
        assertUtils.assert_equals(num, 20)
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('th', assert_text[1]), assert_text[1])

    @allure.story('系统管理-WEB端限流配置-父类限流配置')
    def test_220(self):
        self.ecm.click_system().go_LimitParentList()
        assert_text = '父类限流配置页', '项目名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-WEB端限流配置-WEB方法限流配置')
    def test_221(self):
        self.ecm.click_system().go_LimitMethodList()
        assert_text = 'web方法限流配置页', '项目名称', '编辑'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])
        assertUtils.assert_equals(self.ecm.get_assert_text('a', assert_text[2]), assert_text[2])

    @allure.story('系统管理-WEB端限流配置-WEB登陆用户限流策略')
    def test_222(self):
        self.ecm.click_system().go_LimitUserList()
        assert_text = 'web登陆用户限流策略页', '限流频率'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story('系统管理-WEB端限流配置-WEB登陆用户的方法限流配置')
    def test_223(self):
        self.ecm.click_system().go_LimitUserMethodList()
        assert_text = 'web登陆用户的方法限流配置页', '应用名称'
        assertUtils.assert_equals(self.ecm.get_assert_text('div', assert_text[0]), assert_text[0])
        assertUtils.assert_equals(self.ecm.get_assert_text('span', assert_text[1]), assert_text[1])

    @allure.story("退出登录、未登录页、登录检查")
    def test_001(self):
        # 退出登录、未登录页
        text = self.ecm.quit_ecm_login().go_ecm_login().get_ecm_login_text()
        assertUtils.assert_equals(text, '电商后台管理系统')
        # 登录失败
        text = self.ecm.go_ecm_login().ecm_login_fail('123', '123')
        assertUtils.assert_equals(text, '你输入的账号或密码错误，请重新输入！')
