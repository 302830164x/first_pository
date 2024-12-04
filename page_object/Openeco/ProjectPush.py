from selenium.webdriver import ActionChains, Keys

from page.basepage import BasePage
from common.readelement import Element
from time import sleep

sekorm = Element('OpenecoElement')


class ProjectPush(BasePage):

    def get_filter_value(self):
        text = self.element_text(sekorm['筛选项'])
        return text

    def click_select(self):
        self.is_click(('xpath', '//div[@title="推送给我的需求"]'))
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
