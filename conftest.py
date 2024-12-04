import json
import re
import allure
import pytest
from filelock import FileLock
from selenium.webdriver.chrome.webdriver import WebDriver
from common.readconfig import ini
from page_object.B.BIndexPage import BIndexPage
from page_object.B.BLoginPage import BLoginPage
from page_object.CMS.CmsIndexPage import CmsIndexPage
from page_object.CMS.CmsLoginPage import CmsLoginPage
from page_object.ECM.EcmIndexPage import EcmIndexPage
from page_object.ECM.EcmLoginPage import EcmLoginPage
from page_object.Openeco.OpenecoLoginPage import OpenecoLoginPage
from page_object.Sekorm.SekormIndexPage import SekormIndexPage
from utils.logger import log
from utils.send import send_start, send_ending
from utils.times import timestamp, calculate_duration

ECM_driver = None  # 用于判断和调用截图的标识
SEKORM_driver = None  # 用于判断和调用截图的标识
CMS_driver = None  # 用于判断和调用截图的标识
B_driver = None  # 用于判断和调用截图的标识
Open_driver = None
ecm_page = None  # 页面对象，返回给用例
sekorm_page = None  # 页面对象，返回给用例
cms_page = None  # 页面对象，返回给用例
b_page = None  # 页面对象，返回给用例
open_page = None
total_testcase = None  # 用例总数
start_time = None  # 测试开始时间


# 初始化ECM页面对象、driver
@pytest.fixture()
def ecm_driver():
    global ECM_driver
    global ecm_page
    if ecm_page is None:
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                ecm_page = EcmLoginPage()
                ecm_page.get_url(f'{ini.EcmUrl}/ecp/mac/login')
                ecm_page = ecm_page.ecm_login('Blue_cen', 'Z?12qwpears')
                ecm_page.get_ecm_index_text()
                # 如果成功执行，退出循环
                break
            except Exception as e:
                log.info(f"ECM登录失败报错: {str(e)}")
                ecm_page = 'ECM登录失败'
                retries += 1
    ECM_driver = ecm_page.driver
    return ecm_page


# 初始化Sekorm页面对象、driver
@pytest.fixture(scope='class')
def sekorm_driver():
    global SEKORM_driver
    global sekorm_page
    if sekorm_page is None:
        sekorm_page = SekormIndexPage()
        sekorm_page.get_url(ini.SekormUrl)
    SEKORM_driver = sekorm_page.driver
    return sekorm_page


# 初始化CMS页面对象、driver
@pytest.fixture()
def cms_driver():
    global CMS_driver
    global cms_page
    if cms_page is None:
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                cms_page = CmsLoginPage()
                cms_page.get_url(f'{ini.CmsUrl}/content/login')
                cms_page = cms_page.cms_login('15913623753', '12qwblue')
                # cms_page = cms_page.cms_login('15913623753', '123456')
                cms_page.get_cms_index_text()
                # 如果成功执行，退出循环
                break
            except Exception as e:
                log.info(f"CMS登录失败报错: {str(e)}")
                cms_page = 'CMS登录失败'
                retries += 1
    CMS_driver = cms_page.driver
    return cms_page


# 初始化B台页面对象、driver
@pytest.fixture()
def b_driver(request):
    global B_driver
    global b_page
    if b_page is None:
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                # 执行需要重试的代码
                b_page = BLoginPage()
                b_page.get_url(f'{ini.B_Url}/content/login')
                b_page = b_page.b_login('15913623753', '12qwblue')
                # b_page = b_page.b_login('15913623753', '123456')
                b_page.get_b_index_text()
                # 如果成功执行，退出循环
                break
            except Exception as e:
                log.info(f"B台登录失败报错: {str(e)}")
                b_page = 'B台登录失败'
                retries += 1
    B_driver = b_page.driver
    return b_page

@pytest.fixture()
def openeco_driver():
    global Open_driver
    global open_page
    if open_page is None:
        max_tries = 3
        retries = 0
        while retries < max_tries:
            try:
                open_page = OpenecoLoginPage()
                open_page.get_url(f'{ini.Openeco_Url}/content/login')
                open_page = open_page.openeco_login('15766139640', '15766139640')

                break
            except Exception as e:
                log.info(f'业务合作伙伴平台登录失败：{str(e)}')
                open_page = '登录失败'
                retries += 1
    Open_driver = open_page.driver
    return open_page


# 关闭driver
@pytest.fixture(scope='class', autouse=True)
def quit_driver():
    yield
    global sekorm_page
    global SEKORM_driver
    global ecm_page
    global cms_page
    global b_page
    if isinstance(sekorm_page, SekormIndexPage):
        sekorm_page.driver.quit()
    if isinstance(ecm_page, EcmIndexPage):
        ecm_page.driver.quit()
    if isinstance(cms_page, CmsIndexPage):
        cms_page.driver.quit()
    if isinstance(b_page, BIndexPage):
        b_page.driver.quit()
    sekorm_page = None
    SEKORM_driver = None
    ecm_page = None
    cms_page = None
    b_page = None


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    """
    global ECM_driver
    global SEKORM_driver
    global CMS_driver
    global B_driver
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" or report.when == "setup":
        if report.failed:
            log.info(f'失败用例名称为：{item.name}')
            if isinstance(SEKORM_driver, WebDriver):
                allure.attach(SEKORM_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            if isinstance(ECM_driver, WebDriver):
                allure.attach(ECM_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            if isinstance(CMS_driver, WebDriver):
                allure.attach(CMS_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            if isinstance(B_driver, WebDriver):
                allure.attach(B_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    if report.when == "teardown":
        ECM_driver = None
        CMS_driver = None
        B_driver = None


def pytest_configure(config):
    # 主线程获取开始时间，用于计算脚本执行时长
    if not hasattr(config, 'workeroutput'):
        global start_time
        start_time = timestamp()


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config, items):
    """
    修改用例名称中文乱码
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
    # 在收集完所有用例后调用该函数,将用例总数保存下来用于开始和结束发送通知
    global total_testcase
    total_testcase = len(items)


# 开始执行用例之前，通知企业微信群
@pytest.fixture(scope="session", autouse=True)
def send_notification(tmp_path_factory, worker_id):
    if worker_id == "master":
        # 单进程运行
        # send_start(total_testcase)
        pass
    else:
        # 分布式运行
        # 获取所有子节点共享的临时目录，无需修改【不可删除、修改】
        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if not fn.is_file():  # 只有第一个进来的进程会执行
                fn.write_text(json.dumps(total_testcase))  # 新建缓存文件
                send_start(total_testcase)


# 收集用例通过、失败的条数用于通知企业微信群
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    text = str(terminalreporter._session)  # 获取包含全量用例的字符串
    pattern = r"testscollected=(\d+)"  # 正则表达式
    match = re.search(pattern, text)  # 通过正则表达式与字符串匹配
    total = int(match.group(1))  # 将匹配到的值转化成整形
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    # 当启动多线程时，限制只有当主线程才能根据统计数据发送通知到企业微信群
    if not hasattr(config, 'workeroutput'):
        end_time = timestamp()
        cost_time = calculate_duration(start_time, end_time)
        send_ending(cost_time, total, passed, failed, error)
