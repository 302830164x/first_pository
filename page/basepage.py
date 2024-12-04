"""
selenium基类
本文件存放了selenium基类的封装方法
"""
import io
import json

import pyautogui
import requests
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from config.conf import cm
from utils.logger import log
from utils.times import sleep
from utils.xpath_change import xpath_change


class BasePage(object):
    """selenium基类"""

    def __init__(self, base_driver: WebDriver = None, ):
        """
        没有传入webdriver时设置浏览器driver，有传入webdriver则不初始化
        :param base_driver: 传入当前webdriver
        """

        if base_driver is None:
            # 加启动配置
            options = webdriver.ChromeOptions()
            options.add_experimental_option("prefs", {
                # 禁用“保存密码”弹出窗口
                "credentials_enable_service": False,
                # 禁用“保存密码”弹出窗口
                "profile.password_manager_enabled": False,
                # 禁止显示“请停用以开发者……”
                "useAutomationExtension": False,
            })
            # 禁止显示“Chrome正受到自动化软件的控制”
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            # 无头模式
            # options.add_argument('--headless')
            # 指定屏幕分辨率
            driver_width, driver_height = pyautogui.size()
            options.add_argument(f'--window-size={driver_width}x{driver_height}')
            # options.add_argument("--window-size=1920,1080")
            options.add_argument('--start-maximized')
            # 添加请求头
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 sekorm-agent")
            self.driver = webdriver.Chrome(options=options)
            self.wait = WebDriverWait(self.driver, 10)
        else:
            self.driver = base_driver
            self.wait = WebDriverWait(self.driver, 10)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return BasePage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return BasePage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    # 关闭浏览器
    def quit_driver(self):
        self.driver.quit()

    # 关闭当前浏览器标签
    def close_driver(self):
        num_windows = len(self.driver.window_handles)
        if num_windows == 1:
            return self
        else:
            self.driver.close()
            self.switch_window()
            return self

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        ele = self.find_element(locator)
        ele.send_keys(Keys.CONTROL, 'a')
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.element_move_to_center(locator)
        self.find_element(locator).click()
        sleep(0.2)
        log.info("点击元素：{}".format(locator))

    def mouse_click(self, locator):
        """点击"""
        self.element_move_to_center(locator)
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).click().perform()
        sleep(0.2)
        log.info("点击元素：{}".format(locator))

    def js_click(self, locator):
        """JS点击"""
        self.element_move_to_center(locator)
        self.driver.execute_script("arguments[0].click();", self.find_element(locator))
        sleep(0.2)
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        element = self.find_element(locator)
        if element.is_displayed():
            _text = element.text
        else:
            _text = element.get_attribute('textContent')
        log.info("获取文本：{}".format(_text))
        return _text

    def elements_text(self, locator):
        """获取多个相同元素的text"""
        elements = self.find_elements(locator)
        elem_text = []
        for elem in elements:
            if elem.is_displayed():
                _text = elem.text
                elem_text.append(_text.strip())
            else:
                _text = elem.get_attribute('textContent')
                elem_text.append(_text.strip())
        log.info("获取文本：{}".format(elem_text))
        return elem_text

    def go_to_element(self, locator):
        """滑动滚动条将元素滑到最顶部"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        log.info("滚动条滚动到指定元素：{}".format(locator))

    def element_move_to_center(self, locator):
        """滑动滚动条将元素滑到中间"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        log.info("滑动滚动条将元素：{}滑到中间".format(locator))

    def scroll_to_top(self):
        # 使用JavaScript将页面滚动到顶部
        self.driver.execute_script("window.scrollTo(0, 0);")
        log.info("滚动条滚动到顶部")

    def scroll_to_bottom(self):
        # 使用JavaScript将页面滚动到底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.info("滚动条滚动到底部")

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        log.info('刷新页面成功！')
        return self

    def move_to_element(self, locator):
        """移动至目标元素悬停"""
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.info("移动至目标元素悬停：{}".format(locator))

    @property
    def get_source(self):
        """获取页面源代码（已转义）"""
        # log.info("获取页面源码：{}".format(self.driver.page_source))
        return self.driver.page_source

    def get_assert_text(self, kind, text):
        """根据标签类型（kind）和标签包含文本（text）组建xpath，根据xpath定位元素获取文本并返回"""
        assert_text = self.element_text(xpath_change(kind, text))
        return assert_text

    def switch_window(self, path=-1):
        """
        切换窗口：切换成最新窗口不用传参，切换成上一个窗口传入-2
        """
        # 获取所有窗口的句柄
        windows = self.driver.window_handles
        # 切换到新的窗口
        self.driver.switch_to.window(windows[path])
        log.info("切换窗口")
        return self

    def get_title(self):
        """获取当前浏览器页面的标题"""
        title = self.driver.title
        log.info(f"获取当前浏览器页面title:{title}")
        return title

    def get_back(self):
        """回退"""
        self.driver.back()
        sleep()

    def get_attribute_value(self, locator, attribute_name):
        """获取指定元素的某个属性的值"""
        element = self.find_element(locator)
        attribute_value = element.get_attribute(attribute_name)
        log.info(f"获取元素属性值:{attribute_value}")
        return attribute_value

    def img_show(self, locator):
        """判断图片是否正常显示"""
        img_element = self.find_element(locator)
        self.element_move_to_center(locator)
        sleep()
        # 获取图片地址
        img_src = img_element.get_attribute('src')
        log.info(f"获取图片地址:{img_src}")
        try:
            # 下载图片并打开进行检测
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 sekorm-agent',
            }
            img_data = requests.get(img_src, headers=headers, stream=True).content
            image = Image.open(io.BytesIO(img_data))
            # 获取图像的大小和尺寸
            size = image.size
            log.info(f"获取图片大小:{size}")
            return size
        except Exception as e:
            log.info(f"加载图片失败:{e}")
            return 0, 0

    def get_position(self):
        # 执行 JavaScript 代码来获取当前页面的滚动位置
        scroll_position = self.driver.execute_script("return [window.pageXOffset, window.pageYOffset];")
        log.info(f"当前页面位置:{scroll_position}")
        return scroll_position

    def switch_to_iframe(self, locator):
        """切换至iframe"""
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)
        return self

    def switch_to_content(self):
        """切换回主页面"""
        self.driver.switch_to.default_content()
        return self

    def is_displayed(self, locator):
        """判断元素是否可见，如果元素可见，则返回 True，否则返回 False"""
        return self.find_element(locator).is_displayed()

    def is_existence(self, locator):
        """判断元素是否存在，如果元素存在，则返回 True，否则返回 False"""
        script = f"return document.evaluate({json.dumps(locator[1])}, " \
                 f"document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null;"
        if self.driver.execute_script(script):
            log.info("目标元素存在：{}".format(locator))
            return True
        else:
            log.info("目标元素不存在：{}".format(locator))
            return False


if __name__ == "__main__":
    geturl = BasePage()
