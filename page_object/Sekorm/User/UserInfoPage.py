from page.basepage import BasePage
from utils.times import sleep

Locator = {
    '头像': ('xpath', "//span[@id='logined_user']//img"),
    '账户设置': ('xpath', "//a[contains(text(),'账户设置')]"),
    '用户名': ('xpath', "//p[@class='sk-fs24 color-main-gray bold']"),
    '会员等级': ('xpath', "//p[@class='sk-fs16 mb15 ln16']"),
    '企业信息': ('xpath', "//div[@class='member-header-center ml20']"),
    '修改企业信息': ('xpath', "//a[contains(text(),'修改企业信息')]"),
    '经验值': ('xpath', "//div[@class='grade-box']"),
    '做任务': ('xpath', "//a[contains(text(),'做任务')]"),
    '订单搜索框': ('xpath', "//input[@class='member-search sk-fs14']"),
    '订单搜索按钮': ('xpath', "//button[contains(text(),'搜索')]"),
    '订单列表': ('xpath', "//div[@class='member-order-item']"),
    '订单时间': ('xpath', "//div[@class='member-order-item']/div/div/span[1]"),
    '订单类型': ('xpath', "//div[@class='member-order-item']/div/div/a"),
    '订单号': ('xpath', "//div[@class='member-order-item']/div/div/span[2]"),
    '厂牌': ('xpath', "//td[@class='brandName-img']"),
    '型号': ('xpath', "//td[@class='brandName-img']/following-sibling::td[1]"),
    '单价': ('xpath', "//span[@class='bold']"),
    '查看详情': ('xpath', "//a[contains(text(),'查看详情')]"),
    '查看更多': ('xpath', "//div[@class='expandMore']"),
    '历史记录': ('xpath', "//div[@class='history-record-title']"),
    '历史记录列表': ('xpath', "//div[@class='history-list']/div/div"),
    '历史记录-查看更多': ('xpath', "//a[contains(text(),'查看更多')]"),
    '更多选型': ('xpath', "//div[@class='expand-service-type']"),


    '批量询价': ('xpath', "//div[contains(text(),'询价')]"),
    '交期查询': ('xpath', "//div[contains(text(),'询交期')]"),
    '技术问题': ('xpath', "//div[contains(text(),'技术问题')]"),
    '我的资料': ('xpath', "//div[@id='logined_user_box']//li[4]"),
    '我的资料-我的下载': ('xpath', "//a[contains(text(),'我的下载')]"),
    '我的资料-我的收藏': ('xpath', "//a[contains(text(),'我的收藏')]"),
    '我的资料-历史记录': ('xpath', "//a[contains(text(),'历史记录')]"),
    '我的收藏': ('xpath', "//div[@id='logined_user_box']//li[2]"),
    '我的消息': ('xpath', "//div[@id='logined_user_box']//li[3]"),

    '账号注销': ('xpath', "//a[contains(text(),'如何注销账号？')]"),
    '修改密码': ('xpath', "//a[@id='changePwd']"),
    '账号设置': ('xpath', "//a[contains(text(),'账户设置')]"),
    '个人信息': ('xpath', "//a[contains(text(),'个人信息')]"),
    '账号安全': ('xpath', "//a[contains(text(),'账号安全')]"),
    '收货地址': ('xpath', "//a[contains(text(),'收货地址')]"),
    '发票抬头管理': ('xpath', "//a[contains(text(),'发票抬头管理')]"),
}


class UserInfoPage(BasePage):
    """用户信息页"""

    def check_user_info(self):
        """检查用户信息页布局"""
        for elm in Locator:
            # 遍历检查每次页面元素是否存在
            self.move_to_element(Locator[elm])
            if elm == '历史记录-查看更多':
                break

    def click_user_info(self, elm):
        """点击用户信息页布局"""
        self.move_to_element(Locator['头像'])
        self.is_click(Locator[elm])
        self.switch_window()
        sleep()
        return self

    def check_businessCard(self):
        """电子名片"""
        self.is_click(Locator['电子名片'])
        self.move_to_element(Locator['电子名片-姓名'])
        self.move_to_element(Locator['电子名片-图片'])
        self.move_to_element(Locator['电子名片-分享按钮'])
        self.move_to_element(Locator['电子名片-保存图片'])
        return self.element_text(Locator['电子名片-公司'])

    def check_search(self, text):
        """检查类型搜索"""
        self.input_text(Locator['订单搜索框'], text)
        self.is_click(Locator['订单搜索按钮'])
        return self

    def check_list_num(self):
        """检查列表数量"""
        return self.elements_num(Locator['订单列表'])
