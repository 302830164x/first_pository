from common.readelement import Element
from page.basepage import BasePage
from page_object.CMS.VideoManage.VideoMaterialManagePage import VideoMaterialManagePage
from page_object.CMS.VideoManage.VideoProductManagePage import VideoProductManagePage

sekorm = Element('CmsElement')


class VideoManagePage(BasePage):
    """视频管理"""

    def go_VideoMaterialManagePage(self):
        """视频管理-视频素材管理"""
        self.is_click(sekorm['视频管理-视频素材管理'])
        return VideoMaterialManagePage(self.driver)

    def go_VideoProductManagePage(self):
        """视频管理-视频素材管理"""
        self.is_click(sekorm['视频管理-视频成品管理'])
        return VideoProductManagePage(self.driver)