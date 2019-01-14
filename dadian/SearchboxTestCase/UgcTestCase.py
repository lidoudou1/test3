#coding=utf-8
import shutil

__author__ = 'lixuefang'

from appium import webdriver
import unittest
import time
from utils import PublicFunction
# import HTMLTestRunner
# import os


class UgcTestCase(unittest.TestCase):

    #执行在每个case之前，用于启动手百
    def setUp(self):
        self.driver = PublicFunction.appium_start()

    #执行每个case之后运行，用于退出
    def tearDown(self):
        self.driver.quit()

    def test_Publish_593_1(self):
        print("ugc1 - 593")
        # 点击关注tab，切换到关注tab下
        # self.driver.find_element_by_xpath("//android.widget.TextView").click()
        time.sleep(3)
        PublicFunction.rightslide(self)
        PublicFunction.rightslide(self)
        # 等待10秒，待元素加载完成
        time.sleep(30)
        # 点击发文字，进入发布界面，触发打点时机，type=show
        self.driver.find_element_by_android_uiautomator("text(\"发文字\")").click()
        time.sleep(3)
        # self.driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.TextView[1]").click()
        # 点击表情入口，调起表情键盘，触发打点时机，type=emoji_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_emoij").click()
        time.sleep(3)
        # 点击图片入口，调起相册，触发打点时机，type=photo_click (图片入口的点击)
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_pic_entrance").click()
        time.sleep(3)
        # 点击取消按钮，返回发布器
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_cancel").click()
        time.sleep(3)
        # 点击@入口，调起联系人选择页，触发打点时机，type=at_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_at").click()
        # 点击物理返回键
        self.driver.press_keycode(4)
        # 点击#入口，调起话题聚合页，触发打点时机，page=topic_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_topic").click()
        # 等待1秒，待话题加载完成
        time.sleep(1)
        # 点击物理返回键
        self.driver.press_keycode(4)
        # 在发布器内输入文字
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_edittext").send_keys("demo")
        # 点击发布按钮，触发打点时机，type=pub_click ( 发布按钮的点击)
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_publish").click()

    def test_Publish_Forward_593_2(self):
        print("ugc2 - 593")
        # app启动后等待3秒，方便元素加载完成
        time.sleep(3)
        # 点击置顶新闻，进入落地页
        # self.driver.find_element_by_id("com.baidu.searchbox:id/feed_content").click()
        # self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]").click()
        self.driver.find_element_by_id("com.baidu.searchbox:id/feed_template_base_title_id").click()
        # 等待5秒，点击分享icon（进入落地页直接点击会提示"加载中，请稍后尝试"）
        time.sleep(40)
        # 点击分享icon，调起分享面板
        self.driver.find_element_by_id("com.baidu.searchbox:id/common_tool_item_share").click()
        time.sleep(10)
        # 点击转发按钮，进入发布界面，触发打点时机，type=show
        self.driver.find_element_by_id("com.baidu.searchbox:id/sharemenugrid_iconview").click()
        time.sleep(3)
        # 点击表情入口，调起表情键盘，触发打点时机，type=emoji_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_emoij").click()
        time.sleep(3)
        # 点击@入口，调起联系人选择页，触发打点时机，type=at_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_at").click()
        time.sleep(3)
        # 点击物理返回键
        self.driver.press_keycode(4)
        # 点击#入口，调起话题聚合页，触发打点时机，page=topic_click
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_topic").click()
        # 等待1秒，待话题加载完成
        time.sleep(1)
        # 点击物理返回键
        self.driver.press_keycode(4)
        # 点击发布按钮，触发打点时机，type=pub_click ( 发布按钮的点击)，ext中含有:is_comment(0-无评论、1-勾选评论、2-未勾选评论）
        self.driver.find_element_by_id("com.baidu.searchbox:id/ugc_publish").click()

if __name__ == "__main__":
    unittest.main()
