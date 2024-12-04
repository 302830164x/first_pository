from page.basepage import BasePage
from page_object.Openeco.ProjectPush import ProjectPush
from common.readelement import Element
from time import sleep

sekorm = Element('OpenecoElement')


class OpenecoIndexpage(BasePage):

    # 获取其他信息提示信息
    def get_bubble_text(self):
        self.move_to_element(sekorm['其他信息'])
        sleep(1)
        text = self.element_text(sekorm['首页-气泡'])
        return text

    def click_editbutton(self):
        self.is_click(sekorm['首页-编辑按钮'])
        sleep(1)
        self.is_click(sekorm['首页-取消按钮'])

    def go_openeco_index(self):
        self.is_click(sekorm['首页'])
        return OpenecoIndexpage(self.driver)

    def go_projectpush(self):
        self.is_click(sekorm['项目推送'])
        return ProjectPush(self.driver)
